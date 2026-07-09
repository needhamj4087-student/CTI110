"""
===============================================================================
Weather Dashboard
Author: ChatGPT
Description:
    A simple weather dashboard that displays:
        - Current weather
        - 3-day forecast
        - Live time
        - Current date
        - Moon phase
        - Refreshes automatically every hour

Libraries Used:
    tkinter
    urllib
    json
    datetime
    math
    threading

API:
    Open-Meteo (Free - No API Key Required)

===============================================================================
PSEUDOCODE

START PROGRAM

Create application window

Create all labels
    Clock
    Date
    Moon Phase
    Weather
    Forecast

Wait for user ZIP Code

When Search button pressed
    Convert ZIP -> Latitude/Longitude
    Download weather
    Display weather

Every second
    Update clock

Every hour
    Refresh weather automatically

END PROGRAM

===============================================================================
"""

# ============================================================================
# IMPORTS
# ============================================================================

import tkinter as tk
from tkinter import messagebox

import urllib.request
import urllib.parse
import json

import math
import threading

from datetime import datetime


# ============================================================================
# COLOR THEME
# ============================================================================

BACKGROUND = "#35265D"      # Purple
FRAME = "#4361EE"           # Blue
BUTTON = "#F77F00"          # Orange

TEXT = "white"

FONT_TITLE = ("Arial", 22, "bold")
FONT_HEADER = ("Arial", 16, "bold")
FONT_NORMAL = ("Arial", 12)


# ============================================================================
# WEATHER APP CLASS
# ============================================================================

class WeatherApp:
    """
    Main application class.

    Responsible for:
        • Creating the interface
        • Updating time
        • Getting weather
        • Automatic refresh
    """

    def __init__(self, root):

        self.root = root

        self.root.title("Weather Dashboard")

        self.root.geometry("700x650")

        self.root.configure(bg=BACKGROUND)

        self.last_zip = ""

        self.create_widgets()

        self.update_clock()


    # ========================================================================
    # CREATE USER INTERFACE
    # ========================================================================

    def create_widgets(self):
        """
        PSEUDOCODE

        Create title

        Create clock

        Create date

        Create moon phase

        Create ZIP entry

        Create search button

        Create current weather section

        Create forecast section
        """

        # ------------------------------------------------------------
        # TITLE
        # ------------------------------------------------------------

        tk.Label(
            self.root,
            text="Weather Dashboard",
            bg=BACKGROUND,
            fg="white",
            font=FONT_TITLE
        ).pack(pady=10)


        # ------------------------------------------------------------
        # CLOCK
        # ------------------------------------------------------------

        self.clock_label = tk.Label(
            self.root,
            text="",
            bg=BACKGROUND,
            fg="white",
            font=("Arial", 18)
        )

        self.clock_label.pack()


        # ------------------------------------------------------------
        # DATE
        # ------------------------------------------------------------

        self.date_label = tk.Label(
            self.root,
            text="",
            bg=BACKGROUND,
            fg="white",
            font=FONT_NORMAL
        )

        self.date_label.pack()


        # ------------------------------------------------------------
        # MOON PHASE
        # ------------------------------------------------------------

        self.moon_label = tk.Label(
            self.root,
            text="",
            bg=BACKGROUND,
            fg="white",
            font=FONT_NORMAL
        )

        self.moon_label.pack(pady=5)


        # ------------------------------------------------------------
        # ZIP INPUT
        # ------------------------------------------------------------

        input_frame = tk.Frame(
            self.root,
            bg=BACKGROUND
        )

        input_frame.pack(pady=15)

        tk.Label(
            input_frame,
            text="ZIP Code:",
            bg=BACKGROUND,
            fg="white",
            font=FONT_NORMAL
        ).pack(side=tk.LEFT)

        self.zip_entry = tk.Entry(
            input_frame,
            width=12,
            font=FONT_NORMAL
        )

        self.zip_entry.pack(side=tk.LEFT, padx=8)

        tk.Button(
            input_frame,
            text="Get Weather",
            bg=BUTTON,
            fg="white",
            command=self.start_weather_thread
        ).pack(side=tk.LEFT)


        # ------------------------------------------------------------
        # CURRENT WEATHER FRAME
        # ------------------------------------------------------------

        self.current_frame = tk.Frame(
            self.root,
            bg=FRAME,
            padx=15,
            pady=15
        )

        self.current_frame.pack(fill="x", padx=25, pady=20)

        tk.Label(
            self.current_frame,
            text="Current Weather",
            bg=FRAME,
            fg="white",
            font=FONT_HEADER
        ).pack()

        self.weather_output = tk.Label(
            self.current_frame,
            text="Enter a ZIP Code",
            justify="left",
            bg=FRAME,
            fg="white",
            font=FONT_NORMAL
        )

        self.weather_output.pack(pady=10)


        # ------------------------------------------------------------
        # FORECAST FRAME
        # ------------------------------------------------------------

        self.forecast_frame = tk.Frame(
            self.root,
            bg=FRAME,
            padx=15,
            pady=15
        )

        self.forecast_frame.pack(fill="x", padx=25)

        tk.Label(
            self.forecast_frame,
            text="3-Day Forecast",
            bg=FRAME,
            fg="white",
            font=FONT_HEADER
        ).pack()

        self.forecast_output = tk.Label(
            self.forecast_frame,
            text="Forecast unavailable",
            justify="left",
            bg=FRAME,
            fg="white",
            font=FONT_NORMAL
        )

        self.forecast_output.pack(pady=10)


    # ========================================================================
    # UPDATE CLOCK
    # ========================================================================

    def update_clock(self):
        """
        Update the clock once every second.

        Also updates:
            • Date
            • Moon phase
        """

        now = datetime.now()

        self.clock_label.config(
            text=now.strftime("%I:%M:%S %p")
        )

        self.date_label.config(
            text=now.strftime("%A, %d %B %Y")
        )

        self.moon_label.config(
            text="Moon Phase: " + self.get_moon_phase()
        )

        # Update again in one second
        self.root.after(1000, self.update_clock)


    # ========================================================================
    # MOON PHASE
    # ========================================================================

    def get_moon_phase(self):
        """
        Calculate the moon phase.

        Returns:
            String containing the phase name.
        """

        today = datetime.now()

        year = today.year
        month = today.month
        day = today.day

        if month < 3:
            year -= 1
            month += 12

        month += 1

        c = 365.25 * year
        e = 30.6 * month

        jd = c + e + day - 694039.09
        jd /= 29.5305882

        phase = jd - int(jd)

        index = round(phase * 8)

        if index >= 8:
            index = 0

        phases = [
            "New Moon",
            "Waxing Crescent",
            "First Quarter",
            "Waxing Gibbous",
            "Full Moon",
            "Waning Gibbous",
            "Last Quarter",
            "Waning Crescent"
        ]

        return phases[index]


    # ========================================================================
    # START WEATHER THREAD
    # ========================================================================

    def start_weather_thread(self):
        """
        Runs the weather download on another thread so the GUI
        remains responsive.
        """

        threading.Thread(
            target=self.get_weather,
            daemon=True
        ).start()


    # ========================================================================
    # GET WEATHER (Placeholder)
    # ========================================================================

    def get_weather(self):
   
        """
        Downloads current weather and a 3-day forecast from OpenWeatherMap.
        """

        # Save ZIP code for automatic refresh
        self.last_zip = self.zip_entry.get().strip()

        if self.last_zip == "":
            messagebox.showerror("Error", "Please enter a ZIP Code.")
            return

        # **********************************************
        # ENTER YOUR OPENWEATHERMAP API KEY HERE
        # **********************************************
        API_KEY = "ac8a37ae01aa786a862a3ba89c2574a5"

        # Build URLs
        current_url = (
            f"https://api.openweathermap.org/data/2.5/weather?"
            f"zip={self.last_zip},US&units=imperial&appid={API_KEY}"
        )

        print(current_url)

        forecast_url = (
            f"https://api.openweathermap.org/data/2.5/forecast?"
            f"zip={self.last_zip},US&units=imperial&appid={API_KEY}"
        )

        try:

            # --------------------------------------------
            # CURRENT WEATHER
            # --------------------------------------------
            with urllib.request.urlopen(current_url) as response:
                current_data = json.loads(response.read())

            weather_text = (
                f"Location: {current_data['name']}\n\n"
                f"Temperature: {current_data['main']['temp']} °F\n"
                f"Feels Like: {current_data['main']['feels_like']} °F\n"
                f"Condition: {current_data['weather'][0]['description'].title()}\n"
                f"Humidity: {current_data['main']['humidity']}%\n"
                f"Wind Speed: {current_data['wind']['speed']} mph"
            )

            self.weather_output.config(text=weather_text)

            # --------------------------------------------
            # FORECAST
            # --------------------------------------------
            with urllib.request.urlopen(forecast_url) as response:
                forecast_data = json.loads(response.read())

            forecast_text = ""

            days_added = []

            for item in forecast_data["list"]:

                date = item["dt_txt"].split()[0]

                if date not in days_added:
                    days_added.append(date)

                    forecast_text += (
                        f"{date}\n"
                        f"High: {item['main']['temp_max']} °F\n"
                        f"Low : {item['main']['temp_min']} °F\n"
                        f"{item['weather'][0]['description'].title()}\n\n"
                    )

                if len(days_added) == 3:
                    break

            self.forecast_output.config(text=forecast_text)

            # --------------------------------------------
            # Refresh automatically in one hour
            # --------------------------------------------
            self.root.after(3600000, self.auto_refresh)

        except Exception as error:
        
            import traceback

            traceback.print_exc()

            messagebox.showerror(
                "Weather Error",
                f"{type(error).__name__}\n\n{error}"
            )
    
    # ========================================================================
    # AUTO REFRESH
    # ========================================================================

    def auto_refresh(self):
        """
        Refresh the weather every hour.
        """

        if self.last_zip != "":
            threading.Thread(
                target=self.get_weather,
                daemon=True
            ).start()

        # Schedule the next refresh
        self.root.after(3600000, self.auto_refresh)    


# ============================================================================
# START PROGRAM
# ============================================================================

root = tk.Tk()

app = WeatherApp(root)

root.mainloop()