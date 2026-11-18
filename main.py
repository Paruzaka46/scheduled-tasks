import os
import pandas as pd
import datetime as dt
import smtplib
from random import randint
data = pd.read_csv("birthdays.csv")
data_dict = data.to_dict("records")

my_email = "raython48@gmail.com"
old_email = "rayhanfallah29@gmail.com"
password = "wralurxmlskeiqad"
subject = "Happy Birthday!"

now = dt.datetime.now()
this_month = now.month
today_date = dt.datetime.today().strftime('%Y-%m-%d').split("-")[2]

for i in range(len(data_dict)):
    if data_dict[i]["month"] == this_month and data_dict[i]["day"] == today_date:
        name = data_dict[i]["name"]
        email = data_dict[i]["email"]
        letter_num = randint(1, 3)
        with open(f"letter_templates/letter_{letter_num}.txt", "r") as file:
            letter = file.read()

        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=email,
                                msg=f"Subject:{subject}\n\n{letter.replace("[NAME]", name)}")
