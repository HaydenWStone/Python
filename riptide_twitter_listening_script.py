"""
This listening script conducts a twitter API query repeatedly at desired intervals and sends a summary email with a CSV attachment with unique relevent tweets after a desired time
v1.1
Jan 2, 2023
"""

import tweepy
import time
import csv

def riptide():
#Create an API client
    client = tweepy.Client(
        consumer_key="consumer_key_here",
        consumer_secret="consumer_secret_here",
        access_token="access_token_here",
        access_token_secret="access_token_secret_here")
    # Set the search term
    SEARCH_TERM = 'Set search term here using twitter search syntax'
    # Set the number of tweets to return
    MAX_TWEETS = 100
    # Search for tweets containing the search term
    results = client.search_recent_tweets(SEARCH_TERM, max_results=MAX_TWEETS,
    user_auth=True)

#Parse results from API
    #Convert results into string
    results_string = str(results)
    #Remove trailing metadata from string
    results_string = results_string[:-191]
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

#Dedup results and write to a CSV
    # Open a new file in write mode if first run
    if count == 0:
        with open("output.csv", "w") as f:
            # Create a CSV writer object
            writer = csv.writer(f)
            # Write the output to the file
            for item in split_results:
                #Split tweet URL from tweet text
                part1 = str(item[:49])
                part2 = str(item[49:])
                writer.writerow([part1, part2])
        # Create a set to store the unique values in the second column
        seen = set()
        with open('output.csv', 'r') as in_file, open('master.csv', 'w') as out_file:
            # Create a CSV reader object
            reader = csv.reader(in_file)
            # Create a CSV writer object
            writer = csv.writer(out_file)
            # Iterate over the rows in the output CSV file
            for row in reader:
                # Skip rows with a duplicate value in the second column
                if row[1] in seen:
                    continue
                seen.add(row[1])
                # Write the row to the master CSV file
                writer.writerow(row)
    # Open a new file in append mode if not first run
    elif count != 0:
        with open("output.csv", "a") as f:
            # Create a CSV writer object
            writer = csv.writer(f)
            # Write the output to the file
            for item in split_results:
                #Split tweet URL from tweet text
                part1 = str(item[:49])
                part2 = str(item[49:])
                writer.writerow([part1, part2])
        # Create a set to store the unique values in the second column
        seen = set()
        with open('output.csv', 'r') as in_file, open('master.csv', 'a') as out_file:
            # Create a CSV reader object
            reader = csv.reader(in_file)
            # Create a CSV writer object
            writer = csv.writer(out_file)
            # Iterate over the rows in the output CSV file
            for row in reader:
                # Skip rows with a duplicate value in the second column
                if row[1] in seen:
                    continue
                seen.add(row[1])
                # Write the row to the master CSV file
                writer.writerow(row)
        #Remove duplicates in master file
        with open('master.csv', 'r') as in_file, open('riptide.csv', 'w') as out_file:
            seen = set() # set for fast O(1) amortized lookup
            for line in in_file:
                if line in seen: continue # skip duplicate
                seen.add(line)
                out_file.write(line)

    # Create an empty list to store the deduped tweets
    data = []
    # Open the CSV file for reading
    with open('riptide.csv', 'r') as csvfile:
        # Create a CSV reader object
        reader = csv.reader(csvfile)
        # Iterate over the rows in the CSV file
        for row in reader:
            # Add the row to the data list
            data.append(row)
    final_tweets = data

    #Seperate items and print to console
    final_tweets_flat = []
    for item in final_tweets:
        final_tweets_flat.extend(item)
        print(item)
        print()
    #Create seperated list to print to email body
    final_tweets_sep_modified = '\n'.join([tweet if i % 2 == 0 else tweet + '\n' for i, tweet in enumerate(final_tweets_flat)])

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
        sender_email = "email here"
        receiver_email = "email here"
        password = "password here"
        message = MIMEMultipart()
        message["Subject"] = f"Listening Script Output {d2}"
        message["From"] = sender_email
        message["To"] = receiver_email
        body = MIMEText(f"Email sent by Python.\nRiptide listening script developed by Southwest Impact LLC \n intel@southwestimpact.com \n \n {final_tweets_sep_modified}")

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
    #Set count to number of times for script to run (default is 3)
    if count == 3:
        riptide_send()

#Driver code
count = 0
#Set count to number of times for script to run (default is 3)
while count <= 3:
    riptide()
    count +=1
    #Set sleep time in seconds to period between script runs (default is 1 hour i.e. 3600 seconds)
    time.sleep(3600)

