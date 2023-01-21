import password_strength

def calculate_crack_time(password):
    strength = password_strength.password_strength(password)
    time_to_crack = strength.crack_time
    return time_to_crack

password = "mypassword123"
crack_time = calculate_crack_time(password)
print(crack_time)