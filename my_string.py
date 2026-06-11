driver_name="Vishnu"
mobile="123456789"

masked=mobile[:2]+"******"+mobile[-2:]
print(masked)

# title
song="shape of YOU"
artist="VishnuDevi"
formatted=f"{song.title()}-{artist.title()}"
print(formatted)

# replace
location="chennai central"
fixed_location=location.replace("chennai central","Thambaram")
print(fixed_location)

# split,strip
message="your uber booking id is: UB12345.Please keep it safe"
booking_id=message.split(":")[1].split(".")[0]
print(booking_id)

# print(driver_name.lower())
# print(driver_name.upper())

promo_msg="use zomato100 to get 100 off on your first order"
if "zomato100" in promo_msg:
    print("offer applied")

feedback="the driver was polite and the ride was smooth"
print(feedback.find("polite"))

name="vishnudevi sivashanmugam pazhaniappan"
initial="".join((word[0].upper() for word in name.split(" ")))
print(initial)

# to remove space
drity_input="   airport"
clean=drity_input.strip()
print(clean)