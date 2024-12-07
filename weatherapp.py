import requests

api_key = "c27e5f11b8fb7e0e1327549d5f43fc1e"

city= input("Enter your city: ")


weather_data = requests.get(
f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")

if weather_data.status_code==200:
  temp= weather_data.json()['main']['temp']
  des= weather_data.json()['weather'][0]['main']
  print(f"The weather of city {city}: {temp}° and {des}")
else:
  print(f"{city} city not found")
