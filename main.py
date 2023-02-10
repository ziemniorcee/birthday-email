import smtplib
import datetime as dt
import random
import csv

now = dt.datetime.now()
day = now.day
month = now.month

with open("birthdays.csv") as f:
    data = list(csv.reader(f))
data = data[1:]

for person in data:
    if (int(person[3]) != month) or (int(person[4]) != day):
        data.remove(person)


for person in data:
    my_email = "sapkowskiandrzej5@gmail.com"
    print(person[0])
    password = "udkeglhqksxrfbpj"
    with open("quotes.txt", 'r') as f:
        all_quotes = f.readlines()
    quote = random.choice(all_quotes)
    with open("card.txt") as f:
        card = f.readlines()
    card = ''.join(card)
    card = card.replace("[NAME]", person[0])
    card = card.replace("xaxa123", quote)
    print(card)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=person[1],
                            msg=f"Subject:Happy birthday\n\n {card}.")
        connection.close()

