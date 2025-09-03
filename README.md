# defect_tracker

Bug tracking web app, written in Django with a Vue.js frontend.

## Prerequisites

- Python 3.8+
- Node.js 14+
- pip
- npm

## How to Run

### Backend (Django)

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/AfoD3V/defect_tracker.git
    cd defect_tracker
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
    The backend will be running at `http://127.0.0.1:8000/`.

### Frontend (Vue.js)

1.  **Navigate to the `frontend` directory:**
    ```bash
    cd frontend
    ```

2.  **Install the required packages:**
    ```bash
    npm install
    ```

3.  **Run the development server:**
    ```bash
    npm run dev
    ```
    The frontend will be running at `http://localhost:5173/`.
