import random as rdm
import string


def create_random_password():
    password = ""
    random_number = rdm.randint(10, 15)
    for i in range(random_number):
        password += rdm.choice(string.ascii_letters + string.digits + string.punctuation)
    return password


print('Your new password is:', create_random_password())
