
import requests
import matplotlib.pyplot as plt
import seaborn as sns
import datetime


API_KEY = "2097cc643f5192d37baca2ac0a3d315e"  
CITY = input("Enter the City Name: ")       


URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"


response = requests.get(URL)
data = response.json()

dates = []
temperatures = []
humidities = []

for entry in data['list']:
    dt = datetime.datetime.fromtimestamp(entry['dt'])  
    temp = entry['main']['temp']
    humidity = entry['main']['humidity']

    dates.append(dt)
    temperatures.append(temp)
    humidities.append(humidity)

plt.figure(figsize=(14, 6))
sns.set(style="whitegrid")

plt.subplot(1, 2, 1)
sns.lineplot(x=dates, y=temperatures, color="red")
plt.title(f"Temperature Forecast for {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)

plt.subplot(1, 2, 2)
sns.lineplot(x=dates, y=humidities, color="blue")
plt.title(f"Humidity Forecast for {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Humidity (%)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
