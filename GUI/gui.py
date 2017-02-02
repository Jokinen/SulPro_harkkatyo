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
        self.initialize()

    def initialize(self):
        self.set_fullScreen()
        self.get_data()
        self.grid()

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.init_datetime()
        self.draw_datetime()
        self.draw_local_weather()
        self.draw_room_temperature()

        self.draw_headlines()

    def set_fullScreen(self):
        w, h = self.winfo_screenwidth() - 100, self.winfo_screenheight() - 100
        self.overrideredirect(1)
        self.geometry("%dx%d+0+0" % (w, h))

    def get_data(self):
        self.weather_data = self.weather_API.get_current_conditions()[0]
        self.news_data = self.news_API.get_the_next_web_articles()
        self.display_on = self.circuit.movement_detected
        self.temperature = self.circuit.temperature

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

        self.after(1000, self.draw_datetime) # refresh every 1000ms (1s)

    def draw_local_weather(self):
        width = 400
        height = 170

        w = Canvas(self, width=width, height=height)
        w.grid(column=0, row=1, sticky='NW')

        w.create_rectangle(4, 4, width+1, height+1) # borders

        # City label
        w.create_text(20, 30, text="Kaupunki", anchor="w")
        w.create_text(20, 52, text="Turku", font=(None, 24), anchor="w")

        # Current temp
        w.create_text(20, 92, text="Lämpötila ulkona nyt", anchor="w")
        temp = self.weather_data["Temperature"]["Metric"]["Value"]
        formatted_temp = str(temp) + " C"
        w.create_text(20, 124, text=formatted_temp, font=(None, 40), anchor="w")

    def draw_room_temperature(self):
        width = 400
        height = 100

        w = Canvas(self, width=width, height=height)
        w.grid(column=0, row=2, sticky='NW')

        w.create_rectangle(4, 4, width+1, height+1) # borders

        # Temp label
        w.create_text(20, 30, text="Lämpötila huoneessa", anchor="w")
        temp = self.temperature
        formatted_temp = str(temp) + " C"
        w.create_text(20, 62, text=formatted_temp, font=(None, 40), anchor="w")

    def draw_headlines(self):
        width = 400
        height = 520

        w = Canvas(self, width=width, height=height)
        w.grid(column=1, row=0, rowspan=4, sticky='NE')

        w.create_rectangle(4, 4, width+1, height+1) # borders

        # Label for source
        w.create_text(20, 30, text="Uusimat otsikot The Next Web julkaisusta", anchor="w")

        article_height = 60

        for i, article in enumerate(self.news_data["articles"]):
            x = article_height
            title = article["title"]

            text = w.create_text(20, x, text=title, anchor="w", width=360, font=(None, 15))

            bounds = w.bbox(text)
            height = bounds[3] - bounds[1]

            if i == 0:
                padding = 20 # + padding
            else:
                padding = 10

            article_height += height + padding

    def quit(self):
        self.destroy()
