# OpenShare Backend (Django)

OpenShare is an open-source event photo management platform built for photographers and guests.  
This repository contains the backend service developed using **Django** and **Django REST Framework**.

## 🚀 Features

- Event creation (Public / Private)
- Photographer photo & video uploads
- Guest high-quality photo downloads
- AI Face Recognition based photo access (planned)
- Optional paid or free downloads (planned)
- Designer workflow support (planned)

## 🛠 Tech Stack

- Python 3
- Django
- Django REST Framework
- PostgreSQL (recommended)
- Cloud Storage Support (AWS S3 planned)

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/c4d1/openshare.git
cd openshare
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Start Development Server

```bash
python manage.py runserver
```

Backend will be available at:

```
http://127.0.0.1:8000/
```

## 📌 Project Status

OpenShare is currently under active development.
More features like AI face recognition, payment integration, and designer collaboration will be added soon.

## 📄 License

This project is open-source under the **[Your License Here]** license.

---

### 🤝 Contributing

Contributions are welcome!
Feel free to open issues or submit pull requests.

---

### Contact

For questions or collaboration, reach out via GitHub Issues.