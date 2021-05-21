import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier


def checkPN(number):
    ch_number = phonenumbers.parse(number, "CH")
    print(geocoder.description_for_number(ch_number, "en"))

    service_number = phonenumbers.parse(number, "RO")
    print(carrier.name_for_number(service_number, 'en'))


while True:
    number = input("Enter Your Phone Number\n")
    checkPN(number)
    print()
