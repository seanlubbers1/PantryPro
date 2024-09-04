# PantryPro: A Serverless GenAI Recipe Bot with OpenAI and App Engine

This repository contains a simple yet powerful web application called **PantryPro**, which leverages the OpenAI GPT-4 model to generate recipes based on user-supplied ingredients. The application is built with Flask and provides an easy-to-use interface where users can input ingredients and receive creative recipe suggestions.

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

## Replacing Images Using DALL-E via ChatGPT

To replace an image in your web app using DALL-E through ChatGPT, follow these steps:

1. **Generate an Image with DALL-E in ChatGPT:**

   Use ChatGPT to generate an image using DALL-E. Describe the image you want to create, and ChatGPT will generate it for you.

   Example prompt:

   ```text
   Create an image of a futuristic cityscape at sunset with flying cars and neon lights.
   ```

2. **Download the Generated Image:**

   After ChatGPT generates the image, download it to your computer.

3. **Save the Image to Your Project:**

   Place the downloaded image in the `static/images` directory of your project.

4. **Update the HTML File:**

   Replace the image source in your `index.html` with the path to your new image.

   ```html
   <img
     src="{{ url_for('static', filename='images/your_image_name.png') }}"
     alt="Your New Image"
   />
   ```

## Deploying to Google App Engine

### 1. Set Up Your Google Cloud Project

- If you don't already have a Google Cloud project, create one in the [Google Cloud Console](https://console.cloud.google.com/).
- Make sure App Engine is enabled in your project.

### 2. Create `app.yaml` for App Engine

In the root directory of your project, create a file named `app.yaml` with the following content:

```yaml
runtime: python39

entrypoint: python app.py

handlers:
  - url: /static
    static_dir: static

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

This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/licenses/MIT) file for details.

## Acknowledgments

- [OpenAI](https://openai.com/) for the GPT-4 API
- [Flask](https://flask.palletsprojects.com/) for the web framework
- [Google Cloud](https://cloud.google.com/) for hosting the app
