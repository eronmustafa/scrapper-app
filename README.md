#scrapper-app

A React and Flask-based web application for managing and displaying scraped character data, featuring CRUD operations, Axios-powered API integration, and UI with search functionality and detailed views. The app includes a cron schedule using Celery and Redis to continuously update the database.

Note: If the cron schedule is not required, you can skip steps 1-3 in the backend setup and directly run the Flask backend (python main.py). This will allow the server to function without continuous updates to the database.

Setup and Run Instructions:

Backend Setup:

Step 1 - Install and start Redis server (ensure Redis is downloaded and accessible) - Run command on terminal: 
redis-server --port 6380

Step 2 - Start the Celery worker: 
celery -A app.celery_app worker --loglevel=info --pool=solo

Step 3 - Start the Celery beat scheduler: 
celery -A celery_config beat --loglevel=info

Step 4 - Run the Flask backend: 
python main.py

Frontend Setup:

Step 5 - Navigate to the frontend directory and install dependencies: 
npm i

Step 6 - Start the frontend development server: 
npm run dev

Deployed link:https://scrapper-app-task.web.app/