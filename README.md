# Flask ChatGPT App

This is a Flask application that connects to the ChatGPT API. It provides a simple interface for users to interact with the ChatGPT model.

## Project Structure

```
flask-chatgpt-app
├── app
│   ├── __init__.py
│   ├── routes.py
│   └── templates
│       └── index.html
├── config.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd flask-chatgpt-app
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Configuration

Before running the application, you need to set up your API keys in `config.py`. Make sure to replace the placeholder values with your actual API keys.

## Usage

To run the application, use the following command:
```
flask run
```

Visit `http://127.0.0.1:5000` in your web browser to access the application.

## License

This project is licensed under the MIT License.