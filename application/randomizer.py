import numpy as np
import random

from datetime import datetime
from string import ascii_uppercase, ascii_lowercase, digits

def string(length: int, lowercase=None, numbers=False) -> str:
    if lowercase is True:
        letters_set = ascii_lowercase
    elif lowercase is False:
        letters_set = ascii_uppercase
    else:
        letters_set = ascii_lowercase + ascii_uppercase
    if numbers is True:
        letters_set = letters_set + digits
    return ''.join(random.choices(letters_set, k=length))

def numbers(length: int) -> str:
    return ''.join(random.choices(digits, k=length))

def random_call(func, args=None, kwargs=None, probability=1):
    if args is None:
        args = []
    if kwargs is None:
        kwargs = {}
    if probability >= 1:
        return func(*args, **kwargs)
    if random.choices([True, False], weights=[probability, 1-probability], k=1)[0]:
        return func(*args, **kwargs)

def choose(arr: list):
    return arr[random.randrange(len(arr))]

def sample(arr, size):
    return random.sample(arr, size)