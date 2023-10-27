# EKiti-Rental-Hub
This is the backend branch for this project.

## Installation

To clone and run this application, you'll need [Python](https://www.python.org/downloads/release/python-3111/) (which comes with [pip](https://pip.pypa.io/en/stable/) by default) installed on your PC. 

This app uses the default SQLite database for testing purposes for now.

We'll be using MySQL / PostgreSQL on production.

From your command line:
```bash
# Clone this repository
$ git clone https://github.com/Mikealson-1/EKiti-Rental-Hub

# Go into the repository
$ cd EKiti-Rental-Hub

# Create a virtual environment, replace env with your desired name
$ python3 -m venv env

# Activate the virtual environment 
$ source env/bin/activate

# Install dependencies
(env) $ pip install -r requirements.txt

# Run migrations
(env) $ python3 manage.py makemigrations
(env) $ python3 manage.py migrate

# Run the server
(env) $ python3 manage.py runserver
```
> **Note**
> If you're using Windows OS use `python` or `py` instead of `python3` from the command prompt.

## Usage
Navigate to http://localhost:8000/ on your browser to see the app in action.
If everything goes right, you'll see the welcome page.

# Contributing
- Michael Olukoyade [@Mikaelson-1](https://github.com/Mikaelson-1) <br>
- Chris Adebiyi  [@Chris-ade](https://github.com/chris-ade)

# License

MIT

---
> LinkedIn [@Chris Adebiyi](https://www.linkedin.com/in/chris-adebiyi-266639189) <br>
> GitHub [@Chris-ade](https://github.com/chris-ade) <br>
> Twitter [@chris_adeh](https://twitter.com/chris_adeh)
