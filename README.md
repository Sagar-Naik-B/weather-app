##Prerequisites
Before getting started, make sure you have the following software installed on your machine:

Node.js: You can download it from the official website (https://nodejs.org).
Python: Visit the official Python website (https://www.python.org) and install the latest version.

demo: https://sagar-naik-b.github.io/weather-app/

## Backend Setup (Django)

1.Open a terminal and navigate to the "weather" directory within the project.

```bash
cd weather-app
```

2.Create a new virtual environment (optional but recommended).

```bash
python3 -m venv myenv
```

3.Activate the virtual environment.

- For macOS/Linux:

  ```bash
  source myenv/bin/activate
  ```

- For Windows (PowerShell):

  ```bash
  .\myenv\Scripts\Activate.ps1
  ```

- For Windows (Command Prompt):

  ```bash
  .\myenv\Scripts\activate.bat
  ```

---

4.Install the required Python packages.

```bash
pip install -r requirements.txt
```

5.Start the Django development server.

```bash
python manage.py runserver
```

The Django server should now be running at http://localhost:8000/.

---

## Frontend Setup (React)

1.Open a new terminal and navigate to the "client" directory within the project.

```bash
cd client
```

2.Install the required Node.js packages.

```bash
npm install
```

3.Start the React development server.

```bash
npm start
```

The React server should now be running at http://localhost:3000/.
