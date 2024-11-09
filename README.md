# notes_app

Django Notes Project
Project Overview
This project is a backend API built with Django and Django REST Framework to create, view, update, and delete notes.

Prerequisites
Python (>=3.8)
Django (>=3.x)
PostgreSQL database (configured in .env file)
Install dependencies listed in requirements.txt
Setup Instructions
Clone the Repository

bash
Copy code
git clone https://github.com/username/notes_app.git
cd notes_app
Create a Virtual Environment

bash
Copy code
python -m venv .venv
source .venv/bin/activate  # For Windows: .venv\Scripts\activate
Install Dependencies

Copy code
pip install -r requirements.txt
Environment Variables Create a .env file in the root directory with the following settings:

makefile
Copy code
SECRET_KEY=your_secret_key
DATABASE_URL=your_database_url
DEBUG=True
Run Migrations

Copy code
python manage.py migrate
Run the Development Server

Copy code
python manage.py runserver
API Endpoints

---API Endpoints

          Create a New Note (POST)
                Request: POST https://notes-app-epds.onrender.com/api/note/
                Body:
                
                json
                Copy code
                {
                  "title": "First Note",
                  "body": "This is the body of the first note."
                }
                Response:
                
                json
                Copy code
                {
                  "id": 1,
                  "title": "First Note",
                  "body": "This is the body of the first note.",
                  "created_at": "2024-11-09T12:00:00Z",
                  "updated_at": "2024-11-09T12:00:00Z"
                }
          Get All Notes (GET)
                  Request: GET https://notes-app-epds.onrender.com/api/notes/
                  Response:
                  
                  json
                  Copy code
                  [
                    {
                      "id": 1,
                      "title": "First Note",
                      "body": "This is the body of the first note.",
                      "created_at": "2024-11-09T12:00:00Z",
                      "updated_at": "2024-11-09T12:00:00Z"
                    },
                    {
                      "id": 2,
                      "title": "Second Note",
                      "body": "This is the body of the second note.",
                      "created_at": "2024-11-10T12:00:00Z",
                      "updated_at": "2024-11-10T12:00:00Z"
                    }
                  ]


          Get a Single Note by ID (GET)
                      Request: GET https://notes-app-epds.onrender.com/api/note/1/
                      Response:
                      
                      json
                      Copy code
                      {
                        "id": 1,
                        "title": "First Note",
                        "body": "This is the body of the first note.",
                        "created_at": "2024-11-09T12:00:00Z",
                        "updated_at": "2024-11-09T12:00:00Z"
                      }


          Update a Note (PUT)
                      Request: PUT https://notes-app-epds.onrender.com/api/note/update/1/
                      Body:
                      
                      json
                      Copy code
                      {
                        "title": "Updated First Note",
                        "body": "This is the updated body of the first note."
                      }
                      Response:
                      
                      json
                      Copy code
                      {
                        "id": 1,
                        "title": "Updated First Note",
                        "body": "This is the updated body of the first note.",
                        "created_at": "2024-11-09T12:00:00Z",
                        "updated_at": "2024-11-10T14:30:00Z"
                      }


          Delete a Note (DELETE)
                      Request: DELETE https://notes-app-epds.onrender.com/api/note/delete/1/
                      Response:
                      
                      json
                      Copy code
                      {
                        "message": "Note deleted successfully"
                      }

Ensure you have requirements.txt and .env configured.
Connect your repository to Render and follow their deployment instructions.
Future Work
This project will later integrate a React frontend for user interaction with the notes API.
