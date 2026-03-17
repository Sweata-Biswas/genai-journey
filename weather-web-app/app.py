from flask import Flask , request, render_template
import requests
#create flask server
app = Flask(__name__)
#Python program → becomes a web server
@app.route("/", methods=["GET","POST"])
# When user visits "/" , run this function
#http://127.0.0.1:5000 this is homepage
def index():
    weather = None
    error = None
    if request.method == "POST":
        city = request.form["city"]
        url = f"https://wttr.in/{city}?format=j1"
        try:
            response = requests.get(url)
            if response.status_code != 200:
                raise Exception("API request failed")
            data = response.json()
            temperature = data['current_condition'][0]['temp_C']
            humidity = data['current_condition'][0]['humidity'] 
            weather_desc = data['current_condition'][0]['weatherDesc'][0]["value"]
            description_lower = weather_desc.lower()
            if "rain" in description_lower:
                weather_icon = "🌧️"

            elif "cloud" in description_lower:
                weather_icon = "☁️"

            elif "sun" in description_lower or "clear" in description_lower:
                weather_icon = "☀️"

            elif "haze" in description_lower or "mist" in description_lower:
                weather_icon = "🌫️"

            elif "storm" in description_lower or "thunder" in description_lower:
                weather_icon = "⛈️"

            else:
                weather_icon = "🌍"
            weather={
                'city': city,
                'temperature':temperature,
                'humidity': humidity,
                'description': weather_desc,
                'icon': weather_icon
            }
        except Exception as e:
            error={
                'city': city,
                'description': "Enter city name doesn't exists" 
            }
    return render_template('index.html', weather=weather,error= error)
#This starts the server.
if __name__=='__main__':
    app.run(debug=True)