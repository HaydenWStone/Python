"""
This script gets the daily high tempature, converts it to color, and sends it to a Kasa smartbulb to turn on and display in the morning
"""

import requests
import kasa
import time
import asyncio


###GET TEMP AND COLOR##

#Params here
API_KEY = "OWM API Key Here"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
LAT = "38.9072"
LON = "-77.0369"

#Declare temp variable
f_max = 0

#Color HSV values
colors = {
    "DARK_RED": (346, 100, 64.7),
    "LIGHT_RED": (3, 81.9, 84.3),
    "DARK_ORANGE": (14, 72.5, 95.7),
    "LIGHT_ORANGE": (30, 61.7, 99.2),
    "DARK_YELLOW": (44, 43.3, 99.6),
    "LIGHT_YELLOW": (60, 25.1, 100),
    "LIGHT_BLUE": (193, 9.7, 97.3),
    "MED_BLUE": (195, 26.6, 91.4),
    "DARK_BLUE": (203, 44.5, 82.0),
    "V_DARK_BLUE": (214, 61.7, 70.6),
    "VV_DARK_BLUE": (237, 67.1, 58.4)
}

#API call params
weather_params = {
    "lat":LAT,
    "lon":LON,
    "appid":API_KEY
}

#Call weather API and get max temp
def get_max_temp():
    global f_max

    #Get response
    response = requests.get(OWM_Endpoint,params=weather_params).json()

    #Get max temp
    k_max = response["main"]["temp_max"]

    #Convert Kelvin to F
    f_max = round(((k_max - 273.15)*1.8 + 32),)

    print(f"Max temp will be {f_max} F")

#Get Color
def get_color():
    if f_max <=10:
        color = "VV_DARK_BLUE"
    elif f_max <=20:
        color = "V_DARK_BLUE"
    elif f_max <=30:
        color = "DARK_BLUE"
    elif f_max <=40:
        color = "MED_BLUE"
    elif f_max <=50:
        color = "LIGHT_BLUE"
    elif f_max <=60:
        color = "LIGHT_YELLOW"
    elif f_max <=70:
        color = "DARK_YELLOW"
    elif f_max <=80:
        color = "LIGHT_ORANGE"
    elif f_max <=90:
        color = "DARK_ORANGE"
    elif f_max <100:
        color = "LIGHT_RED"
    elif f_max >=100:
        color = "DARK_RED"

    #Get color HSV code
    color_hsv = colors[color]
    hue, saturation, value = color_hsv
    # Round saturation and value to the nearest integers
    rounded_hsv = (hue, round(saturation), round(value))
    print(color)
    print(rounded_hsv)
    return rounded_hsv

#Get max temp and convert to color
get_max_temp()
hsv = get_color()

##SEND TO BULB##
#Make sure port fowarding is enabled for the bulb on your router - try port 9999
def change_bulb(hsv):
    #IP address of your smart bulb
    ip_address = "Bulb IP address here"

    #Create a SmartBulb object with the specified IP address
    bulb = kasa.SmartBulb(ip_address)

    # On/off function
    async def lightswitch():
        await bulb.update()
        if bulb.is_on:
            await bulb.turn_off()
        if bulb.is_off:
            await bulb.update()
            await bulb.turn_on()

    #Color change function
    async def colorswitch(hsv):
        await bulb.update()
        hue, saturation, value = hsv
        await bulb.set_hsv(hue, saturation, value)

    #Turn on bulb
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(lightswitch())

    #Change color
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(colorswitch(hsv))

    #Wait 4 hours
    time.sleep(4*60*60)

    #Turn off bulb
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(lightswitch())

#Driver
change_bulb(hsv)

