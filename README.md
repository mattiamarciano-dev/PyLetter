# PyLetter 📧

PyLetter is an automated newsletter system written in Python that sends personalized daily emails containing news based on the user's selected category and delivery time.

To work correctly the system should be always running to be sure of sending every email.

The system allows users to configure their email address, preferred news category, and the hour at which they want to receive their daily newsletter.

---

## 🚀 Features

- 📩 Automatic daily newsletter delivery
- 👤 User management
- 📰 News retrieval through News API
- 🕒 Personalized delivery time for each user
- 🗂️ Category-based news selection
- 🗄️ SQLite database storage
- 📝 Automatic activity logging
- 🔐 Environment variable configuration

---

## 🏗️ Project Structure

```text
PyLetter/
│
├── src/
│   ├── Main application files
│   └── Project logic
│
├── database/
│   └── SQLite database (generated automatically)
│
├── logs/
│   └── Daily system logs (generated automatically)
│
├── tests/
│   └── Project tests
│
├── .env.example
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/mattiamarciano-dev/PyLetter.git
```

Enter the project folder:

```bash
cd PyLetter
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

### Windows

```bash
.venv\Scripts\activate
```

### macOS/Linux

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Configuration

Create a `.env` file in the project root using `.env.example` as a template.

Example:

```env
SENDER=your_email@example.com
APIKEY=your_news_api_key
EMAIL_PASSWORD=your_email_password
```

The `.env` file contains sensitive information and must not be uploaded to GitHub.

---

## ▶️ Running the Application

Start PyLetter:

```bash
python src/PyLetter.py
```

The application will:

1. Load registered users
2. Check their delivery time
3. Retrieve news based on category
4. Generate the newsletter
5. Send the email
6. Save activity logs

---

## 🗄️ Database

PyLetter uses SQLite to store user information.

The database contains:

- User email
- Preferred news category
- Delivery hour
- Sending information

The database is created automatically when the application starts.
To add or edit users you can use a ìn external SQLite DB viewer or editor.

---

## 📝 Logs

PyLetter automatically generates daily log files.

Logs contain information about:

- Newsletter sending
- Errors
- System activities

They are stored inside the `logs` folder.

---

## 🛠️ Technologies

- Python
- SQLite
- News API
- SMTP Email
- Requests
- python-dotenv

---

## 📌 Future Improvements

Possible future improvements:

- Web interface
- Better email templates
- User authentication
- Docker support
- More news providers
- Automated deployment

---

## 👨‍💻 Author

Created by Mattia Marciano
