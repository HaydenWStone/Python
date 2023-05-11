import tweepy
import time
import csv
import openai

openai.api_key = "key here"

def riptide():
#Create an API client
    client = tweepy.Client(
        consumer_key="key here",
        consumer_secret="key here",
        access_token="key here",
        access_token_secret="key here")
    # Set the search term
    SEARCH_TERM = 'Search term here'
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
        with open("output.csv", "w", encoding="utf-8") as f:
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
        with open('output.csv', 'r', encoding='utf-8') as in_file, open('master.csv', 'w', encoding='utf-8') as out_file:
        #with open('output.csv', 'r') as in_file, open('master.csv', 'a') as out_file:
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
        with open("output.csv", "a", encoding="utf-8") as f:
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
            seen = set()
            for line in in_file:
                if line in seen:
                    continue
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

    #AI parser function
    def ai_parse(list):
        out_result = []
        for item in list:
            question = f"Please check if the following tweet is related to X. If related, return 'FLAG'. If not relevent, return 'NA'. Please only return one of these two values and no other text. Tweet here: {item}"
            # Create a Completion object using the GPT-3 model
            completion = openai.Completion.create(
                engine="text-davinci-003",
                prompt=question,
                temperature=1,
                max_tokens=1024,
                n=1, )
            response = completion.choices[0].text
            to_append = (response + " " + str(item))
            print(to_append)
            print()
            out_result.append(to_append)
            time.sleep(1)
        return out_result

#Config email send
    def riptide_send(tweets):
        #Get Date
        from datetime import date
        today = date.today()
        # Textual month, day and year
        d2 = today.strftime("%B %d, %Y")

        #Parse items with AI
        ai_parsed = ai_parse(tweets)

        #Create seperated list and format to print to email body
        final_tweets_sep_modified = '\n'.join([tweet + '\n' if i % 2 == 0 else tweet for i, tweet in enumerate(ai_parsed)])
        #Remove extraneous blank lines
        final_tweets_sep_modified = '\n\n'.join(filter(lambda x: x.strip(), final_tweets_sep_modified.split('\n')))
        #Remove brackets
        final_tweets_sep_modified = final_tweets_sep_modified.replace('[', '').replace(']', '')
        #Break up lines
        #final_tweets_sep_modified = final_tweets_sep_modified.replace(", '", ",\n'")

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
        message["Subject"] = f"Subject X Twitter Daily AI Screen {d2}"
        message["From"] = sender_email
        message["To"] = receiver_email
        body = MIMEText(f"Email sent by Python.\n \nTweet Digest:\n \n{final_tweets_sep_modified}")

        # Create the attachment
        attachment = MIMEApplication(open("riptide_test.csv", "rb").read())

        #Add the necessary headers to the attachment
        attachment.add_header("Content-Disposition", "attachment", filename="riptide_test.csv")

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
    if count == 3:
        riptide_send(final_tweets)

#Driver code
count = 0
while count <= 3:
    riptide()
    count +=1
    time.sleep(10800)


