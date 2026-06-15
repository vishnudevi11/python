from functools import partial

# def calculate(base_price,tax_rate):
#     return base_price*(1+tax_rate)
#
# price_with_gst=partial(calculate,tax_rate=0.18)
# print(price_with_gst(1000))


def create_email(username,domain):
    return f"{username}@{domain}"

gmail=partial(create_email,domain="gmail.com")
ymail=partial(create_email,domain="ymail.com")

print(gmail("gowtham"))