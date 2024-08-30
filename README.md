# Flask-OpenAI-Chatbot

This repository contains a simple but powerful web application that leverages the OpenAI GPT-4 model to create an AI-powered chatbot. The application is built with Flask and provides an easy-to-use interface where users can interact with the AI.

## Features

- **AI-Powered Chat:** The app uses OpenAI's GPT-4 model to generate human-like responses to user input.
- **Responsive Design:** The frontend is designed to be clean and responsive, making it accessible across devices.
- **Easy Setup:** The project is simple to set up, with clear instructions provided for getting started.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- Pip (Python package installer)
- Flask
- OpenAI Python client library

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/Flask-OpenAI-Chatbot.git
    cd Flask-OpenAI-Chatbot
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up OpenAI API key:**

    Replace `"your-openai-api-key"` in `app.py` with your actual OpenAI API key.

4. **Run the application:**

    ```bash
    python app.py
    ```

5. **Access the app:**

    Open your web browser and go to `http://localhost:8080`.

## Usage

Once the app is running, you can interact with the AI by typing a message in the input box and clicking "Send." The AI will respond in the chat window.

## Folder Structure

```plaintext
.
├── app.py              # Main application file
├── templates
│   └── index.html      # HTML template for the frontend
├── requirements.txt    # List of dependencies
└── README.md           # Project documentation
