import datetime as dt
import random
import smtplib

import pandas as pd


def get_data():
    data = pd.read_csv("birthdays.csv").to_dict(orient='records')
    day = dt.datetime.now().day
    month = dt.datetime.now().month
    for i in data:
        if i['month'] == month and i['day'] == day:
            return i


def letter_template():
    data = get_data()
    num = random.randint(1, 3)
    with open(f"letter_templates/letter_{num}.txt") as f:
        content = f.readlines()
    return "".join(content).replace("[NAME]", data["name"])


def send_mail():
    from_email = "learnPython11111@gmail.com"
    from_pwd = "hqgbrgytwpgbxkju"
    to_email = "anuj.nits@gmail.com"
    gmail_conn = "smtp.gmail.com"
    message = letter_template()
    subject = "Subject:Happy Birthday!"
    conn = smtplib.SMTP(gmail_conn)
    conn.starttls()
    conn.login(user=from_email, password=from_pwd)
    conn.sendmail(from_addr=from_email, to_addrs=to_email, msg=f"{subject}\n\n{message}")
    conn.close()


if __name__ == '__main__':
    send_mail()
