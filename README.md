# Django Project Setup (from ZIP file)

Quick setup guide for the Django project on Windows and Linux.

## Prerequisites

- Python 3.8+
- pip

## Windows Setup

1. **Extract the ZIP file** to your desired location.

2. **Open Command Prompt** and navigate to the extracted folder:
   ```
   cd path\to\extracted\folder
   ```

3. **Create and activate a virtual environment**:
   ```
   python -m venv myenv
   myenv\Scripts\activate
   ```

4. **Install requirements**:
   ```
   pip install -r requirements.txt
   ```

5. **Run migrations and start the server**:
   ```
   python manage.py migrate
   python manage.py runserver
   ```

## Linux Setup

1. **Extract the ZIP file**:
   ```
   unzip project.zip -d server_detail
   cd server_detail
   ```

2. **Create and activate a virtual environment**:
   ```
   python3 -m venv myenv
   source myenv/bin/activate
   ```

3. **Install requirements**:
   ```
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```
   python manage.py migrate
   ```

5. **Start the development server**:
   ```
   python manage.py runserver
   ```

Access the application at: http://127.0.0.1:8000/