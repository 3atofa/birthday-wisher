import smtplib
import datetime as dt 
import pandas as pd


now = dt.datetime.now()
month = now.month
day = now.day
 
date_now = f"{month}/{day}"

def sendemail(name, email):
    my_email = "omaratef.212109@gmail.com"
    my_password = "zsoglgzrvmqhrnke"
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:

        connection.starttls()

        connection.login(user=my_email, password=my_password)
    
         
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=f"hello {name}\n\n happy birthday\n\n"
            )

csv_data = pd.read_csv("br.csv")

birthday_dict = {data_row["birthdate"]:data_row for(index, data_row) in csv_data.iterrows()}

if date_now in birthday_dict:
    person = birthday_dict[date_now]
    print(person["name"])
    print(person["email"])
    sendemail(person["name"], person["email"])

    








