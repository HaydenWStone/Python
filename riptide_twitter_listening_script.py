"""
This listening script conducts a twitter API query every hour and sends a summary email with a CSV attachment with all relevent tweets from a 24 hour period
"""

import tweepy
import time

def riptide():
#Create an API client
    client = tweepy.Client(
        consumer_key="consumer_key",
        consumer_secret="consumer_secret",
        access_token="access_token",
        access_token_secret="access_token_secret")
    # Set the search term
    SEARCH_TERM = 'Enter search terms here'
    # Set the number of tweets to return
    MAX_TWEETS = 100
    # Search for tweets containing the search term
    results = client.search_recent_tweets(SEARCH_TERM, max_results=MAX_TWEETS,
    user_auth=True)

#Parse results from API
    #Convert results into string
    results_string = str(results)
    # Split string into list
    split_results = results_string.split(">, ")
    # iterate over the list of strings
    for i, tweet in enumerate(split_results):
    # find the index of "<Tweet id="
        start_index = tweet.index("<Tweet id=")
    # insert "https://twitter.com/i/status/" at the start index
        split_results[i] = tweet[:start_index] + "https://twitter.com/i/status/" + tweet[start_index:]
    # delete "<Tweet id=" from the string
        split_results[i] = split_results[i].replace("<Tweet id=", "")
    # delete "Response(data=[" from the string
        split_results[i] = split_results[i].replace("Response(data=[", "")
    # delete "text=" from the string
        split_results[i] = split_results[i].replace("text=", "")
    #seperate the list with blank lines
        split_results_sep = '\n''\n'.join(split_results)
    # Print tweets from list
    for item in split_results:
        print(item + '\n' + '\n')

#Dedup results and write to a CSV
    # Open a new file in write mode if first run
    if count == 0:
        with open("output.csv", "w") as f:
            # Write the output to the file
            for item in split_results:
                f.write(item + '\n')
        #Remove duplicates and write to new file
        with open('output.csv', 'r') as in_file, open('master.csv', 'w') as out_file:
            seen = set() # set for fast O(1) amortized lookup
            for line in in_file:
                if line in seen: continue # skip duplicate
                seen.add(line)
                out_file.write(line)
        #Remove duplicates in master file
        with open('master.csv', 'r') as in_file, open('riptide.csv', 'w') as out_file:
            seen = set() # set for fast O(1) amortized lookup
            for line in in_file:
                if line in seen: continue # skip duplicate
                seen.add(line)
                out_file.write(line)

    # Open a new file in append mode if not first run
    elif count != 0:
        with open("output.csv", "a") as f:
            # Write the output to the file
            for item in split_results:
                f.write(item + '\n')
        #Remove duplicates and append to new file
        with open('output.csv', 'r') as in_file, open('master.csv', 'a') as out_file:
            seen = set() # set for fast O(1) amortized lookup
            for line in in_file:
                if line in seen: continue # skip duplicate
                seen.add(line)
                out_file.write(line)
        #Remove duplicates in master file
        with open('master.csv', 'r') as in_file, open('riptide.csv', 'w') as out_file:
            seen = set() # set for fast O(1) amortized lookup
            for line in in_file:
                if line in seen: continue # skip duplicate
                seen.add(line)
                out_file.write(line)

#Config email send
    def riptide_send():
        #Get Date
        from datetime import date
        today = date.today()
        # Textual month, day and year
        d2 = today.strftime("%B %d, %Y")

        #Configure email send
        import smtplib, ssl
        from email.mime.multipart import MIMEMultipart
        from email.mime.application import MIMEApplication
        from email.mime.text import MIMEText
        port = 587  # For starttls
        smtp_server = "smtp.gmail.com"
        sender_email = "sender@sender.com"
        receiver_email = "receiver@receiver.com"
        password = "password"
        message = MIMEMultipart()
        message["Subject"] = f"Riptide Output {d2}"
        message["From"] = sender_email
        message["To"] = receiver_email
        body = MIMEText(f"Email sent by Python.\nRiptide listening script developed by Southwest Impact\nintel@southwestimpact.com \n \n {split_results_sep}")

        # Create the attachment
        attachment = MIMEApplication(open("riptide.csv", "rb").read())

        #Add the necessary headers to the attachment
        attachment.add_header("Content-Disposition", "attachment", filename="riptide.csv")

        # Attach the attachment to the email message
        message.attach(body)
        message.attach(attachment)

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

    #If end of day, send email
    if count == 24:
        riptide_send()

#Driver code
count = 0
while count <= 24:
    riptide()
    count +=1
    time.sleep(3600)

