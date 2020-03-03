import smtplib, ssl


port = 465 
smtp_server = "smtp.gmail.com"
sender_email = "Amfmftime@gmail.com"
receiver_email = "morgan.hess86@gmail.com"
password = input("Type password: ")
message = """\
Subject: Hi there

This message is sent from Python."""




# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("Amfmftime@gmail.com", password)
    server.sendmail(sender_email, receiver_email, message)
    # TODO: Send email here