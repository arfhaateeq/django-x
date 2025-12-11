


# Django-X  
A clean, modern, fully functional Django social app featuring user authentication, profile management, posts feed, and follower system.

---

## 🚀 Features

### 🔐 **User & Authentication**
- User registration & login  
- Email & username-based authentication  
- Edit profile (username, email, password, profile picture)

### 📝 **Feed / Posts**
- Create posts  
- View posts feed  
- Post detail page  
- Auto timestamps  
- Rich UI using TailwindCSS

### 🧍 **Profiles**
- User profile page  
- Profile picture upload  
- Edit profile info  
- Change password

### ➕ **Followers System**
- Follow / unfollow users  
- Count followers & following  
- Simple social network mechanics

---

## 🛠️ Tech Stack

- **Backend:** Django 4+  
- **Frontend:** TailwindCSS  
- **Database:** SQLite (default)  
- **Auth:** Django AllAuth  
- **Media:** Django file uploads  
- **Version Control:** Git & GitHub  

---

## 📂 Project Structure

```

django-x/
│── feed/              # Posts app
│── followers/         # Follow system
│── profiles/          # User profiles
│── frontend/          # JS frontend
│── media/             # User uploaded files
│── static/            # Static assets
│── templates/         # HTML templates
│── db.sqlite3         # Database (ignored in Git)
│── manage.py

````

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/django-x.git
cd django-x
````

### 2️⃣ Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run migrations

```bash
python manage.py migrate
```

### 5️⃣ Start the server

```bash
python manage.py runserver
```

---


## 📝 Environment Variables

Create a `.env` file:

```
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

---


## 🤝 Contributing

Contributions are welcome!
Please open a pull request or an issue.

---

## 📄 License

This project is licensed under the **MIT License**.

---

## ⭐ Support

If you like this project, consider giving it a **star on GitHub** ⭐
It helps the project grow!
