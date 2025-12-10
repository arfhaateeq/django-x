from django.contrib.auth.models import User
from django.views.generic import DetailView, View, FormView
from feed.models import Post
from followers.models import Follower
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponseBadRequest
from .forms import EditProfileForm
from django.urls import reverse

class ProfileDetailView(DetailView):
    http_method_names = ["get"]
    model = User
    template_name = "profiles/detail.html"
    context_object_name = "user"
    slug_field = "username"
    slug_url_kwarg = "username"

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        user = self.get_object()
        context = super().get_context_data(**kwargs)
        context['total_posts'] = Post.objects.filter(author=user).count()
        context['total_followers'] = Follower.objects.count()
        if self.request.user.is_authenticated:
            context['you_follow'] = Follower.objects.filter(following=user, followed_by=self.request.user).exists()
        return context

class EditProfile(LoginRequiredMixin, FormView):
    form_class = EditProfileForm
    template_name = "profiles/edit_profile.html"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.request.user  # editing logged-in user
        return kwargs

    def form_valid(self, form):
        user = form.save(commit=False)

        # Handle password change
        new_password = form.cleaned_data.get("password1")
        if new_password:
            user.set_password(new_password)

        user.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse("profiles:edit_profile", kwargs={"username": self.request.user.username})

    
class FollowView(LoginRequiredMixin, View):
    http_method_names = ["post"]

    def post(self, request, *args, **kwargs):
        data = request.POST.dict()

        if "action" not in data or "username" not in data:
            return HttpResponseBadRequest("Missing data")
        
        try:
            other_user = User.objects.get(username = data['username'])
        except User.DoesNotExist:
            return HttpResponseBadRequest("missing user")
        
        if data['action'] == "follow":
            follower, created = Follower.objects.get_or_create(
                followed_by = request.user,
                following = other_user
            )
        else:
            try:
                follower = Follower.objects.get(
                    followed_by = request.user,
                    following = other_user
                )
            except follower.DoesNotExist:
                follower = None
            
            if follower:
                follower.delete()

        return JsonResponse({
            "success": True,
            "wording": "Unfollow" if data['action'] == "follow" else "Follow"
        })