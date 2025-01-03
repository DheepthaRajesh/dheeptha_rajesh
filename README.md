# 50.046-Cloud-Project

# Smart desk occupancy monitoring system

An IoT and cloud-based system to optimize shared workspace usage by detecting desk occupancy in real-time. Utilizes **PIR and HC-SR501 sensors with ESP32** for hardware interfacing, **Angular** for frontend, **Node.js/Express** for backend, **Amazon RDS** for database management, and **Docker** for scalable deployment. 

The ESP32 and sensors transmit data via serial communication to the backend, which processes it, updates the database, and serves API requests for the frontend. The user-friendly interface allows users to select a facility (e.g., Library), view total available seats and seats per level, and access a real-time desk dashboard with green (available) and red (occupied) desks, updated dynamically based on sensor data.

Project done in Term 7 SUTD - 2024

## Starting the Application using Docker:

1. Navigate to the project directory where docker-compose.yml is located

2. Run the following command to start all services:
```bash
docker-compose up -d
```
## Instructions to run the frontend and backend:

**To install the packages:**

npm install --legacy-peer-deps

**To start the frontend application:**

ng serve or npm start

**To start the backend application:**

npm start

