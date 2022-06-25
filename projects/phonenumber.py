import phonenumbers
from phonenumbers import timezone, geocoder, carrier

phoneNumber = input("Enter your phone numder with contry code(+88): ")
  
phoneNumber = phonenumbers.parse(phoneNumber)
time = timezone.time_zones_for_number(phoneNumber)
net_carrier = carrier.name_for_number(phoneNumber, 'en')
location = geocoder.description_for_number(phoneNumber, 'en')
  
print(phoneNumber)
print(time)
print(net_carrier)
print(location)