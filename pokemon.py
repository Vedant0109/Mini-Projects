import requests

choice= int(input("Enter pokemon ID: "))

data= requests.get(f"https://pokeapi.co/api/v2/pokemon/{choice}/")

if data.status_code==200:
  info= data.json()
  print(f"The pokemon is {info.get('name')}")
else:
  print("Pokemon not found")