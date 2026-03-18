from flask import Flask , request, render_template
import requests
#create flask server
app = Flask(__name__)
search_history=[]
def get_background(description):

    description = description.lower()

    if "rain" in description:
        return "bg-dark text-white"
    elif "cloud" in description:
        return "bg-secondary text-white"
    elif "clear" in description or "sun" in description:
        return "bg-warning"
    elif "haze" in description or "mist" in description:
        return "bg-light"
    else:
        return "bg-info text-white"
    
def get_weather_symbol(description):
    description_lower = description.lower()
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
    elif "snow" in description_lower:
        weather_icon = "❄️"
    else:
        weather_icon = "🌍"
    return weather_icon
#Python program → becomes a web server
@app.route("/", methods=["GET","POST"])
# When user visits "/" , run this function
#http://127.0.0.1:5000 this is homepage

def index():
    weather = None
    error = None
    global search_history
    if request.method == "POST":
        city = request.form["city"]
        url = f"https://wttr.in/{city}?format=j1"
        search_history.append(city)
        if len(search_history)>5:
            search_history.pop(0)
        try:
            response = requests.get(url)
            if response.status_code != 200:
                raise Exception("API request failed")

            data = response.json()['data']
            if "current_condition" in data:
                current_data =data['current_condition'][0]
                temperature = current_data.get('temp_C','N/A')
                humidity = current_data.get('humidity','N/A')
                weather_desc = current_data.get('weatherDesc',[{}])[0].get("value",'N/A')
                weather={
                    'city': city,
                    'temperature':temperature,
                    'humidity': humidity,
                    'description': weather_desc,
                    'icon': get_weather_symbol(weather_desc),
                    'background':get_background(weather_desc)
                    
                }

            else:
                raise Exception("Weather Data not found")
        except Exception as e:
            error={
                'city': city,
                'description': "Weather data not available" 
            }
    return render_template('index.html', weather=weather,error= error,history=search_history)


#This starts the server.
if __name__=='__main__':
    app.run(debug=True)

