import requests
city = input("Enter the city name: ")
# here f means we are taking the input and converting them into string. 
url = f"https://wttr.in/{city}?format=j1"
url_response  = requests.get(url)
if url_response.ok == True:
    data = url_response.json()
else:
    print("Error fecthing the weather data")    
temperature = data['current_condition'][0]['temp_C']
humidity = data['current_condition'][0]['humidity']
weather_desc = data['current_condition'][0]['weatherDesc'][0]["value"]


print("City: "+city)
print("Temperature: ",temperature,"C")
print("Humidity: ",humidity)
print("Weather: ",weather_desc)