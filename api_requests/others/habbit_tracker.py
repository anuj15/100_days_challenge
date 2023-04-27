from datetime import datetime as dt

import requests
import urllib3

from api_requests.others.data import *

urllib3.disable_warnings()

END_POINT = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"
GRAPH_DATE = dt(year=2023, month=4, day=22).strftime("%Y%m%d")
header = {
    "X-USER-TOKEN": PIXELA_TOKEN
}


def create_user():
    create_user_params = {
        "token": PIXELA_TOKEN,
        "username": PIXELA_USER_NAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }
    requests.post(url=END_POINT, json=create_user_params, verify=False)


def create_graph():
    create_graph_params = {
        "id": GRAPH_ID,
        "name": "Cycling Graph",
        "unit": "km",
        "type": "float",
        "color": "ajisai",
    }
    requests.post(url=f"{END_POINT}/{PIXELA_USER_NAME}/graphs", json=create_graph_params, headers=header,
                  verify=False)


def create_pixel():
    create_pixel_params = {
        "date": GRAPH_DATE,
        "quantity": "15",
    }
    requests.post(url=f"{END_POINT}/{PIXELA_USER_NAME}/graphs/{GRAPH_ID}", headers=header, json=create_pixel_params,
                  verify=False)


def update_pixel():
    update_pixel_params = {
        "quantity": "5",
    }
    requests.put(url=f"{END_POINT}/{PIXELA_USER_NAME}/graphs/{GRAPH_ID}/{GRAPH_DATE}", headers=header,
                 json=update_pixel_params, verify=False)


def delete_pixel():
    requests.delete(url=f"{END_POINT}/{PIXELA_USER_NAME}/graphs/{GRAPH_ID}/{GRAPH_DATE}", headers=header, verify=False)


if __name__ == '__main__':
    print("")
    delete_pixel()
