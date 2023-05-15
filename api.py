import json
import requests
import re
import os.path
import os
from datetime import datetime
from extract_clean import *
from decouple import config

API_URL = config('E_ACCOM_API_URL')
API_KEY = config('TOKEN')


def create_json(numberOfRoom, start, end, type_code, firstname, lastname, tel, email, booking_id, booking_date, ota_name, promotion, breakfast, adult_amount, kid_amount, paid_amount, ota_payment_status):

    data = {
        "outerServiceBooking": True,
        "numberOfRoom": numberOfRoom,
        "start": start,
        "end": end,
        "type_code": type_code,
        "ota_booking_id": booking_id,
        "customer": {
            "firstname": firstname,
            "lastname": lastname,
            "tel": tel,
            "email": email
        },
        "ota_attribute": {
            "booking_id": booking_id,
            "ota_name": ota_name,
            "promotion": promotion,
            "breakfast": breakfast,
            "adult_amount": adult_amount,
            "kid_amount": kid_amount
        },
        "remark": "",
        "payment": {
            "paid_amount": paid_amount,
            "ota_payment_status": ota_payment_status,
            "discount_amount": 0,
            "paid_type": "ONLINE_SYSTEM"
        },
        "capacity": {
            "adult": adult_amount,
            "child": kid_amount
        }
    }

    json_formatted_str = json.dumps(data, indent=4)

    print(json_formatted_str)
    print("\n"*3)
    return data


def post_data(data, msg_id):
    # Convert the JSON object to a string
    json_data = json.dumps(data)

    # Send the JSON data to a website using the HTTP POST method with the Authorization header
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}'
    }
    response = requests.post(API_URL, data=json_data, headers=headers)

    # Print the response from the website
    print(response.text)

    match = re.search("error", response.text)
    if match:
        if not os.path.exists("log_api.txt"):
            f = open("log_api.txt", "a")
            f.write("")
        with open('log_api.txt', "a") as f:
            f.write("msg_id " + msg_id + ' \ ' + str(datetime.now()) +
                    ' : ' + str(response.text) + '\n\n')
            f.close()


def delete_data(booking_id):

    # Define the Bearer token
    token = API_KEY

    url = f'{API_URL})ota/{booking_id}'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    response = requests.delete(url, headers=headers)
    print(url)
    # print content of request
    print(response.json())
