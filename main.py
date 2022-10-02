import  phonenumbers
from mob import number

# get the mobile number location
from phonenumbers import geocoder
ch_nmber = phonenumbers.parse(number, "CH")
print("Location : ", geocoder.description_for_number(ch_nmber, "en"))

# which sim card
from phonenumbers import carrier
service_num = phonenumbers.parse(number, "RO")
print("Sim : ", carrier.name_for_number(service_num, "en"))

# time zone
from phonenumbers import timezone
zone = phonenumbers.parse(number, "GB")
print("Time zone", timezone.time_zones_for_number(zone))

# Validating a phone number
valid = phonenumbers.is_valid_number(ch_nmber)
# Checking possibility of a number
possible = phonenumbers.is_possible_number(ch_nmber)
if valid:
    print("Yes, Valid this number")
else:
    print("Not Valid")
if possible:
    print("The Number is possible")
else:
    print("The number is not possible")