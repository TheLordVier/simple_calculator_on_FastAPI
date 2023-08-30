# Simple Calculator Web App using FastAPI

This is a simple web application that allows users to perform arithmetic calculations through a web interface. The application is built using FastAPI and Jinja2Templates for rendering HTML templates.

## Features

- Input an arithmetic expression and receive the result or an error message.
- Supports addition, subtraction, multiplication, and division operations.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/TheLordVier/simple_calculator_on_FastAPI

2. Create and activate virtual environment:

   ```bash
   python3 -m venv venv
   .venv/bin/activate (for Linux)
   venv\Scripts\activate (for Windows)

3. Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt

## Usage

1. Start the FastAPI application:

      ```bash
      uvicorn calculator:app --reload
   
2. Open your web browser and navigate to http://127.0.0.1:8000 to access the calculator web app.

## Testing

This project includes unit tests to ensure the correctness of the application's behavior.

1. Open a terminal and from the root of the project, run the following command to run the tests:

      ```bash
      python -m unittest tests/test_calculator.py
   
Or just run the tests from the test_calculator.py file located in the tests directory.
   
## License

This project is licensed under the MIT License.
