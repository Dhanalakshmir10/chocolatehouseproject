Chocolate House Application
This is a Python-based application for a fictional chocolate house to manage:

Seasonal flavor offerings
Ingredient inventory
Customer flavor suggestions and allergy concerns
The application uses Flask for the backend, HTML/CSS for the frontend, and SQLite as the database.

Features
1. Home Page: Welcome screen with navigation to other sections.
2. Flavor Offerings: View and manage seasonal flavors.
3. Ingredient Inventory: Manage stock of ingredients used.
4. Customer Suggestions: Add and view customer flavor suggestions and allergy concerns.

Prerequisites
Python 3.12+
Docker 
VS Code 

Step 1: Clone the Repository
git clone https://github.com/Dhanalakshmir10/chocolateHouseproject.git
cd chocolate-house

Step 2: Create a Virtual Environment
python -m venv venv
venv\Scripts\activate     # On Windows

Step 3: Install Dependencies
pip install -r requirements.txt

Step 4: Set Up the Database
Run the following script to initialize the SQLite database:
python setup_db.py


Running the Application Locally
Start the Flask development server:
python run.py
Open your browser and visit: http://127.0.0.1:5000/

File Structure
chocolate-house/
├── app/                     # Main application folder
│   ├── templates/           # HTML templates
│   │   ├── base.html        # Base template
│   │   ├── index.html       # Home page
│   │   ├── flavors.html     # Flavors page
│   │   └── inventory.html   # Inventory page
│   ├── static/              # CSS and JS files
│   │   └── styles.css       # Stylesheet
│   ├── __init__.py          # Flask app initialization
│   └── routes.py            # Application routes
├── run.py                   # Application entry point
├── setup_db.py              # Script to initialize the database
├── requirements.txt         # Python dependencies
├── Dockerfile               # Docker configuration
└── README.md                # Project documentation


