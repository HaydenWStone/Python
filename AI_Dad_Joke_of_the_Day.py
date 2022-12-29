"""
Asks the OpenAI GPT-3 AI to write a new dad joke and then emails it
"""

import openai

# Set your OpenAI API key
openai.api_key = "api key here"

# Create a Completion object using the GPT-3 model
completion = openai.Completion.create(
    engine="text-davinci-003",
    prompt="Write a new dad joke",
    temperature = 1,
    max_tokens=1024,
    n=1,
)

# Print the response from the GPT-3 model
print(completion.choices[0].text)
response = completion.choices[0].text

#Get Date
from datetime import date
today = date.today()
# Textual month, day and year
d2 = today.strftime("%B %d, %Y")

#Configure email send
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "intel@southwestimpact.com"
receiver_email = "sramigstone@gmail.com"
password = "Riptide21!"
message = MIMEMultipart()
message["Subject"] = f"AI Dad Joke of the Day {d2}"
message["From"] = "AI Dad"
message["To"] = receiver_email
body = MIMEText(f"{response}")

# Attach the body to the email message
message.attach(body)

# Convert the email message to bytes
message = message.as_bytes()

#Send Email
context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

#Configure email send
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "address here"
receiver_email = "address here"
password = "password here!"
message = MIMEMultipart()
message["Subject"] = f"AI Dad Joke of the Day {d2}"
message["From"] = "AI Dad"
message["To"] = receiver_email
body = MIMEText(f"{response}")

# Attach the body to the email message
message.attach(body)

# Convert the email message to bytes
message = message.as_bytes()

#Send Email
context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)