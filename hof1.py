def gmail_email(username,domain="gmail.com"):
    return f"{username}@{domain}"

def ymail_email(username,domain="ymail.com"):
    return f"{username}@{domain}"

def build_email(username,email_function):
    return email_function(username) #gmail_email("vishnudevi)

print(build_email("vishnudevi", gmail_email))