🧙‍♂️ FLASK PROFILE ENDPOINT
📋 Overview

This is the Stage 0 Task for the Backend Wizards Internship.
The goal is to build a dynamic Flask API endpoint that returns a JSON response containing profile information and computes the current datetime in UTC.

🚀 Features

A single GET endpoint (/me)
1. Returns a JSON response with:

2. status

3. Timestamp in iso format

4. user information includiing:
* email
* name
* tech stack

🧩 Example Response
{
  "fact": "Most cats adore sardines.",
  "status": "success",
  "timestamp": "2025-10-18T16:15:17.713Z",
  "user": {
    "email": "adefioye.ayomidej@gmail.com",
    "name": "Adefioye Ayomide James",
    "stack": "Python/Flask"
  }
}

🛠️ Tech Stack

Python 3.x

Flask — for creating the web server

Flask-CORS — to handle cross-origin requests

Werkzeug — Flask’s built-in utility library

⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/Ayomidejames/Flask-profile-endpoint.git
cd backend-wizards-stage0

2️⃣ Create a Virtual Environment
python -m venv env

3️⃣ Activate the Environment

On Windows:

env\Scripts\activate


On macOS/Linux:

source env/bin/activate

4️⃣ Install Dependencies
pip install -r requirements.txt

5️⃣ Run the App
python app.py


Then visit:
👉 http://127.0.0.1:5000/me

🌐 Deployment

The app can be deployed on Render, Railway, or Heroku using the included Procfile.

🧠 Author

Name: Adefioye Ayomide
Track: Backend Development
Slack Username: ayomide_adefioye

📎 Links

🗂️ GitHub Repo:  https://github.com/Ayomidejames/Flask-profile-endpoint

📄 Main File: app.py
