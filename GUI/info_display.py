#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

from Tkinter import *
import time
from WeatherAPI import weather_API
from News_API import news_API
from circuit_interface import circuit_interface

class info_display(Tk):
    def __init__(self,parent):
        Tk.__init__(self,parent)
        self.parent = parent
        self.weather_API = weather_API()
        self.news_API = news_API()
        self.circuit = circuit_interface()
        self.visible = True
        self.focus_force()
        self.bind('<Escape>', self.close)
        self.initialize()

    def initialize(self):
        self.set_fullScreen()
        self.get_data()
        self.grid()

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.init_datetime()
        self.init_local_weather()
        self.init_room_temperature()

        self.init_headlines()

        self.draw()

    def draw(self):
        if self.visible:
            self.draw_datetime()
            self.draw_local_weather()
            self.draw_room_temperature()

            self.draw_headlines()
        else:
            # Delete all contents so nto visible
            self.datetime_w.delete(ALL)
            self.local_weather.delete(ALL)
            self.room_temperature.delete(ALL)

            self.headlines.delete(ALL)

        self.after(1000, self.draw) # refresh every 1000ms (1s)

    def set_fullScreen(self):
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.overrideredirect(1)
        self.geometry("%dx%d+0+0" % (w, h))

    def get_data(self):
        self.weather_data = self.weather_API.get_current_conditions()[0]
        self.news_data = self.news_API.get_the_next_web_articles()
        self.temperature = self.circuit.get_temperature()

        print self.circuit.get_temperature()

    def init_datetime(self):
        width = 400
        height = 90

        self.datetime_w = Canvas(self, width=width, height=height)
        self.datetime_w.grid(column=0, row=0, sticky='NW')

    def draw_datetime(self):
        self.datetime_w.delete(ALL)

        current_date = time.strftime("%d/%m/%Y")
        current_time = time.strftime("%H:%M:%S")

        self.datetime_w.create_rectangle(4, 4, 400+1, 90+1) # borders

        # Time and date
        self.datetime_w.create_text(20, 30, text="Päivä ja aika", anchor="w")
        datetime = current_date + " " + current_time
        self.datetime_w.create_text(20, 52, text=datetime, font=(None, 24), anchor="w")

    def init_local_weather(self):
        width = 400
        height = 170

        self.local_weather = Canvas(self, width=width, height=height)
        self.local_weather.grid(column=0, row=1, sticky='NW')

    def draw_local_weather(self):
        self.local_weather.delete(ALL)

        width = 400
        height = 170

        self.local_weather.create_rectangle(4, 4, width+1, height+1) # borders

        # City label
        self.local_weather.create_text(20, 30, text="Kaupunki", anchor="w")
        self.local_weather.create_text(20, 52, text="Turku", font=(None, 24), anchor="w")

        # Current temp
        self.local_weather.create_text(20, 92, text="Lämpötila ulkona nyt", anchor="w")
        temp = self.weather_data["Temperature"]["Metric"]["Value"]
        formatted_temp = str(temp) + " C"
        self.local_weather.create_text(20, 124, text=formatted_temp, font=(None, 40), anchor="w")

    def init_room_temperature(self):
        width = 400
        height = 100

        self.room_temperature = Canvas(self, width=width, height=height)
        self.room_temperature.grid(column=0, row=2, sticky='NW')

    def draw_room_temperature(self):
        self.room_temperature.delete(ALL)

        width = 400
        height = 100

        self.room_temperature.create_rectangle(4, 4, width+1, height+1) # borders

        # Temp label
        self.room_temperature.create_text(20, 30, text="Lämpötila huoneessa", anchor="w")
        temp = self.temperature
        formatted_temp = str(temp) + " C"
        self.room_temperature.create_text(20, 62, text=formatted_temp, font=(None, 40), anchor="w")

    def init_headlines(self):
        width = 400
        height = self.winfo_screenheight()

        self.headlines = Canvas(self, width=width, height=height)
        self.headlines.grid(column=1, row=0, rowspan=4, sticky='NE')

    def draw_headlines(self):
        self.headlines.delete(ALL)

        width = 400
        height = self.winfo_screenheight()

        self.headlines.create_rectangle(4, 4, width+1, height+1) # borders

        # Label for source
        self.headlines.create_text(20, 30, text="Uusimat otsikot The Next Web julkaisusta", anchor="w")

        article_height = 60

        for i, article in enumerate(self.news_data["articles"]):
            x = article_height
            title = article["title"]

            text = self.headlines.create_text(20, x, text=title, anchor="w", width=360, font=(None, 15))

            bounds = self.headlines.bbox(text)
            height = bounds[3] - bounds[1]

            if i == 0:
                padding = 20 # + padding
            else:
                padding = 10

            article_height += height + padding

    def show(self):
        self.visible = True

    def hide(self):
        self.visible = False

    def close(self):
        print("called")
        self.destroy()
