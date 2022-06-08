import requests
from pprint import pprint
API_Key = "9875aab48daaefc418c1ab052bf932c6"
city:str
city = input("Digite a cidade")
base_url = "http://api.openweathermap.org/data/2.5/weathe?appid="+API_Key+"&Q=city"
weather_data = requests.get(base_url).json()
pprint(weather_data)