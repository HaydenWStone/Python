"""
The script gets the ground position of the ISS, calculates the distance from a viewing location, and sends an email if it is likely within view
"""


import requests
import math
import time


#Set viewer location here
VIEWER_LAT = 38.889248
VIEWER_LONG = -77.050636
CITY = "Washington, DC"

iss_lat = 0
iss_long = 0

#Calulate ground distance to ISS location
def calc_distance():
    global iss_lat
    global iss_long

    #ISS location  API call
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    #Get ISS lat long
    iss_lat = float(data["iss_position"]["latitude"])
    iss_long = float(data["iss_position"]["longitude"])

    #Calc difs in lat long degrees
    lat_dif = (iss_lat - VIEWER_LAT)
    long_dif = (iss_long - VIEWER_LONG)

    #Convert degrees to miles and find total distance
    lat_dist = 69.172 * math.cos(lat_dif)
    long_dist = long_dif * math.pi/180.0 * 3963.1676 * math.cos(iss_lat * math.pi/180.0)
    total_dist = math.sqrt(lat_dist**2 + long_dist**2)
    return total_dist

#Get bearing from viewing location to ISS
def get_bearing(lat1, long1, lat2, long2):
    #Convert to radians
    lat1 = math.radians(lat1)
    long1 = math.radians(long1)
    lat2 = math.radians(lat2)
    long2 = math.radians(long2)

    #Calculate differences
    dLong = long2 - long1
    dLat = lat2 - lat1

    #Calculate bearing
    y = math.sin(dLong) * math.cos(lat2)
    x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(dLong)
    angle = math.atan2(y, x)

    #Convert to degrees and adjust for quadrant
    bearing = math.degrees(angle)
    if bearing < 0:
        bearing += 360

    return bearing

def send_email():

    #Get bearing
    bearing = round(get_bearing(VIEWER_LAT, VIEWER_LONG, iss_lat, iss_long))

    # Configure email send
    import smtplib, ssl
    from email.mime.multipart import MIMEMultipart
    from email.mime.application import MIMEApplication
    from email.mime.text import MIMEText
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "email here"
    receiver_email = "email here"
    password = "password here"
    message = MIMEMultipart()
    message["Subject"] = f"ISS Alert"
    message["From"] = sender_email
    message["To"] = receiver_email
    body = MIMEText(
        f"The ISS is within 500 miles of {CITY}\nIf you look up at a bearing of {bearing} degrees, you may be able to see it!")

    # Attach the attachment to the email message
    message.attach(body)

    # Convert the email message to bytes
    message = message.as_bytes()

    # Send Email
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

#Driver
while True:

    #Send email if distance is less than 500 miles
    if calc_distance() <500:
        send_email()
        time.sleep(3600)

    #Check again in 5 minutes
    time.sleep(300)


