# Weather Web App

This project is a simple **Python web application** that fetches real-time weather information for a city using an API and displays it on a web page.

The application connects a **frontend interface (HTML + Bootstrap)** with a **Python backend using Flask**.

---

## How the Application Works

The system works in the following flow:

Browser (User Interface)
↓
Flask Server (Python Backend)
↓
Weather API (Internet)
↓
Flask Processes Data
↓
HTML Page Displays Result

### Step-by-step Flow

1. The user opens the web page in a browser.
2. The user enters a city name in the input field.
3. The form sends the request to the Flask server.
4. Flask receives the city name.
5. Flask calls the weather API to get weather data.
6. The API returns JSON data.
7. Flask extracts temperature and weather description.
8. Flask sends the data back to the HTML template.
9. The web page displays the weather result.

---

## What is Flask?

Flask is a **Python web framework** that allows Python programs to run as web applications.

Without Flask, a Python program normally runs in the terminal:

Example:

Enter city name: Delhi
Temperature: 31°C

Only the terminal user can interact with the program.

With Flask, the program runs as a **web server** and users interact through a browser.

Example:

User opens website → enters city → clicks button → weather appears on the page.

Flask acts as the **bridge between the frontend (HTML/CSS)** and the **backend logic (Python code)**.

---

## Technologies Used

* Python
* Flask
* HTML
* CSS
* Bootstrap
* Weather API
* Requests library

---

## Project Structure

weather-web-app/

app.py
templates/
  index.html
README.md

---

## How to Run the Application

1. Make sure Python is installed.

2. Install required libraries:

pip install flask
pip install requests

3. Run the application:

python app.py

4. Open the browser and go to:

http://127.0.0.1:5000

---

## Example Usage

User enters:

Mumbai

The application displays:

City: Mumbai
Temperature: 30°C
Weather: Light rain

---

## Future Improvements

Possible upgrades for this project:

* Add weather icons
* Show humidity and wind speed
* Add 5-day weather forecast
* Improve UI design using Bootstrap cards

---

## Author

Sweata
