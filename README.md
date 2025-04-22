🌍 Travel Booking System
A full-stack travel booking platform where users can search, book, and manage trips, with separate backend and frontend services. Each component is containerized using Docker for smooth development and deployment.

🎯 Objective
To develop a scalable, modular travel booking system that:

Allows users to browse, search, and book travel packages.

Provides admins with the ability to manage bookings, destinations, and user data.

Uses REST APIs to communicate between frontend and backend.

Is fully containerized using Docker for easy deployment.

🛠️ Technology Stack
Frontend
Framework: React.js

Styling: Tailwind CSS / Bootstrap

HTTP Client: Axios

Routing: React Router DOM

Backend
Language: Python

Framework: FastAPI

Database: PostgreSQL / SQLite (for dev)

ORM: SQLAlchemy

Authentication: JWT

Documentation: Swagger UI (auto from FastAPI)

DevOps
Containerization: Docker

Orchestration: Docker Compose

Environment Config: .env files

📁 Project Structure
pgsql
Copy
Edit
travel-booking-system/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── database.py
│   │   ├── crud.py
│   │   ├── schemas.py
│   │   └── routers/
│   │       ├── bookings.py
│   │       ├── users.py
│   │       └── packages.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.js
│   │   ├── components/
│   │   ├── pages/
│   │   └── services/
│   ├── Dockerfile
│   └── package.json
│
├── docker-compose.yml
└── README.md
🚀 How to Run the Project
Step 1: Backend Setup
bash
Copy
Edit
cd backend
docker build -t travel-backend .
Step 2: Frontend Setup
bash
Copy
Edit
cd frontend
docker build -t travel-frontend .
Step 3: Combined Docker Compose
Create docker-compose.yml at the root:

yaml
Copy
Edit
version: '3'
services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    volumes:
      - ./backend:/app
    env_file:
      - ./backend/.env

  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    volumes:
      - ./frontend:/app
    stdin_open: true
    tty: true
Run:

bash
Copy
Edit
docker-compose up --build
🌐 API Endpoints
Auth
POST /auth/login – Login user

POST /auth/register – Register new user

Users
GET /users/me – Get logged-in user info

Packages
GET /packages – List all travel packages

POST /packages – Add a package (admin)

Bookings
POST /bookings – Book a travel package

GET /bookings – User’s bookings

✨ Features
JWT-based login and registration

Travel package browsing and booking

Role-based access control (admin/user)

Fully dockerized microservices

Auto-generated API docs via Swagger

🧪 Future Enhancements
Payment gateway integration

Review and rating system

Email notifications

Admin dashboard with analytics

Submitted By: Rubab Arshad
Submitted To: Mr Faisal Shehzad
