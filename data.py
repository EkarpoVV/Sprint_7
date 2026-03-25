


class MandatoryFilds:
    payload = [
    {
        "password": "password77",
        "firstName": "first_name77"
    },
    {
        "login": "password88",
        "firstName": "first_name88"
    }
    ] 

class RegistredCourier:
    payload = {"login": "oqrbfccinr","password": "pvpzicsnsf"}
    response_text = '{"id":716777}'
    COURIER_ID = 716644

class RegistredCourierWithName:
    payload = {
        "login": "oqrbfccinr",
        "password": "pvpzicsnsf",
        "firstName": "eabhmakafz"
        }
    response_text = '{"id":716777}' 

class Order:
    params = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": ["BLACK"]
        }

class RegistredLogin:
    params = {
        "login": "oqrbfccinr",
        "password": "pvpzicsnsf",
        "firstName": "eabhmakafz"
    }

class IncorrectLoginOrPassword:
        payload = [
        {
        "login": "INCORRECT",
        "password": "pvpzicsnsf"
        },
        {
        "login": "oqrbfccinr",
        "password": "INCORRECT"
        }
        ]

class OrderChooseColour:
    params = [
         {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": ["BLACK"]
        },
        {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": ["GREY"]
        }]