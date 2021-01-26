import string
import random

# create random captcha


def random_string():
    # hash length
    N = 4
    S = string.ascii_uppercase + string.ascii_lowercase + string.digits
    # random string length 4
    random_string = ''.join(random.choices(s, k=N))
    return random_string
