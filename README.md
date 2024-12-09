# Scrapper-App

A React and Flask-based web application for managing and displaying scraped character data. The application supports CRUD operations, Axios-powered API integration, and a user-friendly UI with search functionality and detailed views. It features a robust backend using Celery and Redis to continuously update the database with scraped data.

---

## **Deployed Application**
- **Frontend URL:** [https://scrapper-app-task.web.app/](https://scrapper-app-task.web.app/)
    Note: The data is not displayed on the frontend due to a missing SSL certificate on the backend API.
          This causes mixed content issues when attempting to fetch data from an HTTP API on an HTTPS site.
          You can access the data directly via the backend API:
- **Backend URL:** [http://16.171.165.80:5000/](http://16.171.165.80:5000/)

---

## **End-to-End Pipeline**
### Overview
The application implements an automated scraping pipeline integrated with a robust backend system. Below is a description of the pipeline:

1. **Scraping:**
   - Two scraping tasks (`scrape_and_store_vikings` and `scrape_and_store_norsemen`) run as Celery tasks.
   - These tasks fetch data from respective sources and store it in a PostgreSQL database, avoiding duplicate entries by using `ON CONFLICT DO NOTHING`.

2. **Data Update Frequency:**
   - Scraping tasks are scheduled using **Celery Beat** with a configurable interval (default: every hour).

3. **Error Handling:**
   - **Scraping Failures:** Errors during scraping are logged, and tasks automatically retry with exponential backoff (configurable with Celery).
   - **Data Quality Issues:** The pipeline validates incoming data for required fields (e.g., `character_name`, `actor_name`) before storing.

4. **Scheduling and Robustness:**
   - Celery workers and beat schedulers are backed by Redis as the broker.
   - Redis ensures task queues are persistent, enabling tasks to retry on failures.
   - Database operations (inserts) avoid duplication by checking existing data via `ON CONFLICT` clauses in SQL.

5. **Frontend Integration:**
   - A React-based frontend fetches data from the Flask API and displays it with search and detail views.
   - The frontend provides a responsive and intuitive interface for end-users.

---

## **Public Git Repository**
The complete codebase, including scraped data, scripts, and web application code, is available in this public repository:

- **GitHub Repository:** [https://github.com/eronmustafa/scrapper-app](https://github.com/eronmustafa/scrapper-app)

---

## **Project Contents**
1. **Scraped Data:**
   - All scraped data is included in the `data/` directory in JSON format for reproducibility.

2. **Database Table Scripts:**
   - SQL scripts to recreate the database tables are in the `db_scripts/` directory.

3. **Web Application Code:**
   - The full source code for the backend (Flask + Celery) and frontend (React) is included.

4. **README:**
   - Setup and usage instructions for deploying and running the application.

---

## **Setup and Run Instructions**

### **Backend Setup**
1. **Install Redis:**
   Ensure Redis is installed and accessible on your machine. Start the Redis server with:
   ```bash
   redis-server --port 6380

2. **Start the Celery Worker:**
   celery -A app.celery_app worker --loglevel=info --pool=solo

3. **Start the Celery Beat Scheduler:**
   celery -A celery_config beat --loglevel=info

4. **Run the Flask Backend:**
   python main.py

### **Frontend Setup**
5. **Navigate to the Frontend Directory and Install Dependencies**
   npm i

6. **Start the Frontend development server**
   npm run dev
