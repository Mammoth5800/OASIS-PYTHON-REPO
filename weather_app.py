import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
import io

# Your WeatherAPI key
API_KEY = "9f7b10dc722e4a78b27113605261503"


# -----------------------------
# GET WEATHER DATA
# -----------------------------
def get_weather():

    city = city_entry.get()

    if city == "":
        messagebox.showerror("Error", "Please enter a city name")
        return

    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"

    try:
        response = requests.get(url)
        data = response.json()

        if "error" in data:
            messagebox.showerror("Error", data["error"]["message"])
            return

        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        wind = data["current"]["wind_kph"]
        humidity = data["current"]["humidity"]
        icon_url = "https:" + data["current"]["condition"]["icon"]

        temperature_label.config(text=f"Temperature: {temp} °C")
        wind_label.config(text=f"Wind Speed: {wind} km/h")
        humidity_label.config(text=f"Humidity: {humidity}%")
        condition_label.config(text=f"Condition: {condition}")

        show_icon(icon_url)

    except:
        messagebox.showerror("Error", "Network error")


# -----------------------------
# DISPLAY WEATHER ICON
# -----------------------------
def show_icon(url):

    response = requests.get(url)
    image_data = response.content

    image = Image.open(io.BytesIO(image_data))
    photo = ImageTk.PhotoImage(image)

    icon_label.config(image=photo)
    icon_label.image = photo


# -----------------------------
# MAIN WINDOW
# -----------------------------
root = tk.Tk()
root.title("Weather App")
root.geometry("420x420")
root.resizable(False, False)

title = tk.Label(root, text="Weather Application", font=("Arial", 18, "bold"))
title.pack(pady=10)


# CITY INPUT
city_label = tk.Label(root, text="Enter City Name:", font=("Arial", 12))
city_label.pack()

city_entry = tk.Entry(root, font=("Arial", 12))
city_entry.pack(pady=5)


# SEARCH BUTTON
search_button = tk.Button(
    root,
    text="Get Weather",
    font=("Arial", 12),
    bg="blue",
    fg="white",
    command=get_weather
)

search_button.pack(pady=10)


# WEATHER ICON
icon_label = tk.Label(root)
icon_label.pack()


# WEATHER DATA
temperature_label = tk.Label(root, text="", font=("Arial", 14))
temperature_label.pack(pady=5)

wind_label = tk.Label(root, text="", font=("Arial", 14))
wind_label.pack(pady=5)

humidity_label = tk.Label(root, text="", font=("Arial", 14))
humidity_label.pack(pady=5)

condition_label = tk.Label(root, text="", font=("Arial", 14))
condition_label.pack(pady=5)


# FOOTER
footer = tk.Label(root, text="Powered by WeatherAPI", fg="gray")
footer.pack(side="bottom", pady=10)


root.mainloop()
