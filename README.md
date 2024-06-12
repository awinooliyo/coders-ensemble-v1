# Coders Ensemble Portfolio Project

CodersEnsemble is a collaborative platform designed to connect coding enthusiasts worldwide. It provides an environment for learning, sharing knowledge, and working on projects together. This README provides an overview of the project, setup instructions, and other relevant information.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

CodersEnsemble is a full-stack web application built to foster collaboration among developers. Users can create profiles, join projects, and collaborate on coding tasks. The project emphasizes security, user experience, and community engagement.

## Features

- **User Authentication**: Secure registration and login using Bcrypt for password hashing and Flask-Login for session management.
- **Profile Management**: Users can create and update their profiles, showcasing their skills and projects.
- **Project Collaboration**: Users can create, join, and collaborate on projects.
- **Responsive Design**: The application is accessible on both desktop and mobile devices.

## Technologies Used

- **Backend**: Python, Flask, SQLAlchemy
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: PostgreSQL
- **Authentication**: Flask-Login, Bcrypt
- **Deployment**: Docker, Gunicorn, Nginx

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/awinooliyo/coders-ensemble-v1.git
    cd coders-ensemble-v1
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Initialize the database:
    ```bash
    flask db init
    flask db migrate
    flask db upgrade
    ```

5. Run the application:
    ```bash
    flask run
    ```

## Contributing

**Erick O. Awino
Benedict Ndigirigi Gichuhi

## Usage

- Visit `http://127.0.0.1:5000` in your web browser.
- Register for a new account or log in with existing credentials.
- Create or join projects and start collaborating with other users.
