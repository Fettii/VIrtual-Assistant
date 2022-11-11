import requests
def weather():
  city = input('Enter your city: ')
  state = input('Enter your state: ')
  country = input('Enter your country: ')
  api_key = 'f2f54d52a411ff8b6ab105df1e06e72f'
  
  api = f"https://api.openweathermap.org/data/2.5/weather?q={city},{state},{country}&appid={api_key}"
  json_data = requests.get(api).json()
  condition = json_data['weather'][0]['main']
  temp = int((json_data['main']['temp'] - 273.15) * (9/5) + 32)
  final_info = condition + "\n" + str(temp) + "°F"
  return final_info
print(weather())