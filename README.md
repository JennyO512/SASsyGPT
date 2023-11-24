# Flask SASGPT
Conversational SASGPT for assistance in IBM SAS JCL Mainframe program development. 

## Overview
This Flask SASGPT application is a web-based chat interface that utilizes OpenAI's GPT models to provide responses to user queries, specifically focusing on IBM SAS JCL Mainframe programming. The application features user authentication and a chat interface where authenticated users can ask programming-related questions.

## Features
- User Registration and Authentication
- Secure Login System
- Interactive Chat Interface
- Integration with OpenAI's GPT models for automated responses
- Database storage for user credentials and chat history

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.6+
- Flask
- SQLAlchemy
- OpenAI API Key

## Installation and Setup
1. **Clone the Repository**
   ```sh
   git clone https://github.com/your-repository/FlaskChatGPT.git
   cd FlaskChatGPT
   ```

2. **Set Up a Virtual Environment (Optional)**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Packages**
   ```sh
   pip install -r requirements.txt
   ```

4. **Environment Variables**
   - Rename `.env.example` to `.env`.
   - Add your OpenAI API Key and other configuration settings in the `.env` file.

5. **Initialize the Database**
   ```sh
   flask db upgrade
   ```

6. **Run the Application**
   ```sh
   flask run
   ```

## Usage
After starting the application, navigate to `http://localhost:5000` in your web browser. You can register a new user account, log in, and start interacting with the ChatGPT interface.

## API Reference
This application uses the OpenAI API to generate responses. Ensure you have a valid OpenAI API key configured in your `.env` file.

## Contributing
Contributions to the Flask ChatGPT application are welcome. Please follow these steps:
1. Fork the repository.
2. Create a new branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`.
4. Push to the original branch: `git push origin <project_name>/<location>`.
5. Create the pull request.

Alternatively, see the GitHub documentation on [creating a pull request](https://help.github.com/articles/creating-a-pull-request/).

## License
This project is licensed under the [MIT License](LICENSE).

## Contact
For support or queries, please contact us at `your-email@example.com`.


# Python Flask Example

This is a [Flask](https://flask.palletsprojects.com/en/1.1.x/) app that serves a simple JSON response.

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/zUcpux)

## ✨ Features

- Python
- Flask

## 💁‍♀️ How to use

- Install Python requirements `pip install -r requirements.txt`
- Start the server for development `python3 main.py`
