import requests

from api_key import api_key

location = input('Enter city name: ')

'''base URL'''

url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}'

response = requests.get(url)

'''converting kelvin to degrees'''  

def temp_conversion(kelvin):
  celcius = kelvin - 273.14
  
  return celcius
  

''''fetch response from API'''

  
if response.status_code == 200:
  result = response.json() #this allows us to treat the fetched data as a dictionary
  temp = result['main']['temp']
  temp_celcius = temp_conversion(temp)
  desc = result['weather'][0]['description']
  hum = result['main']['humidity']
  print(f'Temperature: {temp} K')
  print(f'Temperature in degrees is {temp_celcius:.2f}')
  print(f'Description: {desc}')
  print(f'Humidity: {hum}')
  
  
else:
  print('Error data not found')



  
