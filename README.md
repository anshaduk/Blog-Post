### Blog Post with Country-Based Filtering ###
This Django-based application displays blog posts and allows users to toggle between viewing all posts and those filtered by the user's country. The country-based filtering is achieved by determining the user's country from their IP address.

###Features###

Displays blog posts in a responsive, grid layout with hover effects.

Users can toggle between:
    Viewing all blog posts.
    Viewing blog posts filtered by their country.

Modern, mobile-friendly design using Tailwind CSS.
Interactive user interface powered by JavaScript for dynamic view switching.

###Technologies Used###

Backend: Django, SQLite (default database)
Frontend: HTML, Tailwind CSS, JavaScript
Database: SQLite (default for Django)
Utilities: Custom utility function to detect the user's country based on their IP address.

###Setup and Installation###
Follow these steps to get the application running locally on your machine.

###Prerequisites###
Before you begin, make sure you have the following installed:

    Python 3.x
    A virtual environment tool like venv or virtualenv
    Django

###Installation###
Clone the repository to your local machine:
    https://github.com/anshaduk/Blog-Post.git
    cd Blogtask/Blog

Create and activate a virtual environment:
    python -m venv venv
    source venv/bin/activate  # For Linux/Mac
    venv\Scripts\activate     # For Windows

Install the required dependencies:
    pip install -r requirements.txt

Apply database migrations:
    python manage.py migrate

Start the development server:
    python manage.py runserver

Open your browser and navigate to:
    http://127.0.0.1:8000/

