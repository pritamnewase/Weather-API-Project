import requests
import matplotlib.pyplot as plt
import seaborn as sns

API_KEY = "a4a4960a9c230cbd33b153185f3e9f3a"

city = "Pune"

url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()


if response.status_code != 200:
    print("Error:", data)
    exit()

dates = []
temperatures = []

for item in data["list"][:8]:
    dates.append(item["dt_txt"])
    temperatures.append(item["main"]["temp"])

sns.set_style("darkgrid")
plt.figure(figsize=(10,5))
plt.plot(dates, temperatures, marker='o')

plt.xticks(rotation=45)
plt.title(f"Temperature Forecast for {city}")
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.tight_layout()

plt.show()
