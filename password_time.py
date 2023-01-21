from passlib.pwd import PasswordPolicy, crack_time_seconds

def calculate_crack_time(password):
    policy = PasswordPolicy.from_names(
        length=8,  # Minimal length for the password
        uppercase=1,  # Minimal amount of uppercase characters
        digits=1,  # Minimal amount of digits
        nonletters=1,  # Minimal amount of non-letter characters
    )

    crack_time = crack_time_seconds(password, policy)
    return crack_time

password = "mypassword123"
crack_time = calculate_crack_time(password)
print(crack_time)
