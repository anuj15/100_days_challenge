import datetime
import math
import smtplib

import urllib3

from api_requests.others.iss import *

urllib3.disable_warnings()

my_position = (28.669155, 77.453758)


def is_close():
    return abs(math.dist(my_position, iss_position())) <= 5


def is_night():
    parameters = {
        "lat": my_position[0],
        "lng": my_position[1],
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", verify=False, params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    hour = datetime.datetime.now().hour
    return sunrise >= hour >= sunset


def look_up():
    from_usr = "learnPython11111@gmail.com"
    from_pwd = "hqgbrgytwpgbxkju"
    to_user = "anuj.nits@gmail.com"
    gmail_conn = "smtp.gmail.com"
    message = "Subject:Look Up\n\nThe ISS is above you in the sky!"
    conn = smtplib.SMTP(gmail_conn)
    conn.starttls()
    conn.login(user=from_usr, password=from_pwd)
    conn.sendmail(from_addr=from_usr, to_addrs=to_user, msg=message)
    conn.close()


if __name__ == '__main__':
    if is_close() and is_night():
        look_up()
