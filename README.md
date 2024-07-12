# Plug-n-Cook
Generates recipe based on your ingredients

## Prerequisites

- Python 3.7+
- pip (Python package installer)

## Setup

1. Clone this repository:
`git clone https://github.com/nimoes/plug-n-cook.git`
`cd plug-n-cook`

2. Install dependencies:

Using pip:
`pip install fastapi uvicorn`

Using poetry:
Install poetry if you haven't: `curl -sSL https://install.python-poetry.org | python3 -`
`poetry install`

3. Start the backend server

Using pip:
`uvicorn app.main:app --reload -port 8888`

Using poetry:
`poetry run uvicorn app.main:app --reload --port 8888`

4. Serve html page


## How to Use

1. Enter ingredients you have in your fridge or pantry one at a time.
2. Click "Add" after each ingredient.
3. When you've added all your ingredients, click "Generate Recipe".
(in progress)
4. The application will display a recipe based on your ingredients.

## File Structure

- `app/main.py`: FastAPI backend code
- `index.html`: Frontend HTML/CSS/JavaScript
- `pyproject.toml`: Poetry configuration file and dependency specifications

