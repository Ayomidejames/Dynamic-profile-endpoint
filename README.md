🧙‍♂️ Backend Wizards — Stage 0: Dynamic Profile Endpoint
📋 Overview

This is the Stage 0 Task for the Backend Wizards Internship.
The goal is to build a dynamic Flask API endpoint that returns a JSON response containing profile information and computes the current datetime in UTC.

🚀 Features

A single GET endpoint (/api/profile/<username>)

Returns a JSON response with:

slack_name

current_day

utc_time (ISO 8601 format, ending with Z)

track

github_file_url

github_repo_url

status_code (200)

🧩 Example Response
{
  "slack_name": "Adefioye Ayomide",
  "current_day": "Wednesday",
  "utc_time": "2025-10-15T18:30:00Z",
  "track": "Backend",
  "github_file_url": "https://github.com/your-username/backend-wizards-stage0/blob/main/app.py",
  "github_repo_url": "https://github.com/your-username/backend-wizards-stage0",
  "status_code": 200
}

🛠️ Tech Stack

Python 3.x

Flask — for creating the web server

Flask-CORS — to handle cross-origin requests

Werkzeug — Flask’s built-in utility library

⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/your-username/backend-wizards-stage0.git
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
👉 http://127.0.0.1:5000/api/profile/
<your_slack_name>

🌐 Deployment

The app can be deployed on Render, Railway, or Heroku using the included Procfile.

🧠 Author

Name: Adefioye Ayomide
Track: Backend Development
Slack Username: ayomide_adefioye

📎 Links

🗂️ GitHub Repo: https://github.com/your-username/backend-wizards-stage0

📄 Main File: app.py