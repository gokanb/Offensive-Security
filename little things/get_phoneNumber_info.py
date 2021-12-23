#!/bin/usr/env python3

import phonenumbers
from phonenumbers import geocoder, carrier, timezone

phone_number = phonenumbers.parse("+")
print(geocoder.description_for_number( phone_number , 'en' ))
print(carrier.name_for_number( phone_number , 'en' ))
#print(timezone.timezone_for_number( phone_number , 'en' ))


