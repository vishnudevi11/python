# returning function as output
# inner can refer outer function argument
def email_builder(domain):
    def build_email(username):
        return f"{username}@{domain}"
    return build_email

gmail=email_builder("gmail.com")
ymail=email_builder("yahoo.com")

print(gmail("vishnudevi"))
print(ymail("Vish"))
