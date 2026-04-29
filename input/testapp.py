import sys

# full_name=sys.argv[1]  #if index 1,it will take input's first value alone
full_name=" ".join(sys.argv[1:]) # 1 after :(colon),can give multiple values
print(full_name)

email=full_name.lower().replace(" ",".")+"@company.com"

print("Full name:",full_name)
print("Email:",email)

