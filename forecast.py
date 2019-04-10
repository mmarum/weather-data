import requests
import time

api = 'https://api.darksky.net/forecast'

# To-do: Move this key to a separate file
# So it can stay out of repo
key = '45d226bdc214d623a167eb061edf85c0'

# To-do: Eventually replace this with more choices
latlong = '40.669079,-74.117180'

response = requests.get(f'{api}/{key}/{latlong}')
currently = response.json()['currently']

class Current:
    def __init__(self, currently):
        self.time = currently['time']
        self.summary = currently['summary']
        self.icon = currently['icon']
        self.nearestStormDistance = currently['nearestStormDistance']
        self.nearestStormBearing = currently['nearestStormBearing']
        self.precipIntensity = currently['precipIntensity']
        self.precipProbability = currently['precipProbability']
        self.temperature = currently['temperature']
        self.apparentTemperature = currently['apparentTemperature']
        self.dewPoint = currently['dewPoint']
        self.humidity = currently['humidity']
        self.pressure = currently['pressure']
        self.windSpeed = currently['windSpeed']
        self.windGust = currently['windGust']
        self.windBearing = currently['windBearing']
        self.cloudCover = currently['cloudCover']
        self.uvIndex = currently['uvIndex']
        self.visibility = currently['visibility']
        self.ozone = currently['ozone']

def readable_time(this_time):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(this_time))

c = Current(currently)

print(c.time)