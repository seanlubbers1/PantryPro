# Serverlesss GenAI Chatbot with OpenAI and App Engine

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
- Google Cloud SDK (for deploying to App Engine)

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

4. **Run the application locally:**

   ```bash
   python app.py
   ```

5. **Access the app:**

   Open your web browser and go to `http://localhost:8080`.

## Deploying to Google App Engine

### 1. Set Up Your Google Cloud Project

- If you don't already have a Google Cloud project, create one in the [Google Cloud Console](https://console.cloud.google.com/).
- Make sure App Engine is enabled in your project.

### 2. Create `app.yaml` for App Engine

In the root directory of your project, create a file named `app.yaml` with the following content:

```yaml
runtime: python310  # or your specific Python runtime version

instance_class: F2  # Optional: Specify instance class (e.g., F1, F2)

handlers:
- url: /.*
    script: auto
```

### 3. Deploy the Application

Authenticate your Google Cloud account:

```bash
gcloud auth login
```

Set your project ID:

```bash
gcloud config set project YOUR_PROJECT_ID
```

Deploy the app:

```bash
gcloud app deploy
```

This command will deploy your application to Google App Engine. Follow the prompts and confirm when asked.

### 4. Access Your Deployed App

Once the deployment is complete, you can access your app at:

```bash
https://YOUR_PROJECT_ID.appspot.com
```

## Usage

Once the app is deployed, users can interact with the AI by typing a message in the input box and clicking "Send." The AI will respond in the chat window.

## Folder Structure

```plaintext
.
├── app.py              # Main application file
├── app.yaml            # App Engine configuration file
├── templates
│   └── index.html      # HTML template for the frontend
├── requirements.txt    # List of dependencies
└── README.md           # Project documentation
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [OpenAI](https://openai.com/) for the GPT-4 API
- [Flask](https://flask.palletsprojects.com/) for the web framework
- [Google Cloud](https://cloud.google.com/) for hosting the app
