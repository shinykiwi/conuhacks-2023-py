import breach_check


def check_email_leak(email):
    email_leaked = breach_check.check(email)
    if email_leaked:
        return f"{email} has been compromised in a data breach."
    else:
        return f"{email} has not been compromised in a data breach."


email = "example@gmail.com"
result = check_email_leak(email)
print(result)
