import csv, smtplib, ssl

message = """Subject: Test

Hi {name}, how are you today? This should be sending one email to multiple people"""
from_address = "amfmftime@gmail.com"
password = input("Type your password and press enter: ")

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(from_address, password)
    with open("contacts_file.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for name, email in reader:
            server.sendmail(
                from_address,
                email,
                message.format(name=name),
            )