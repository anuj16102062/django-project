import random
import string
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'auth_project.settings')
django.setup()

from auth_app.models import User

def generate_random_string(length=10):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

def generate_random_phone_number():
    return ''.join(random.choice(string.digits) for _ in range(10))

def populate_data(num_records):
    for _ in range(num_records):
        name = generate_random_string()
        mob_number = generate_random_phone_number()
        email = f'{name.lower()}@yopmail.com'
        password = generate_random_string(8)

        user = User(name=name, mob_number=mob_number, email=email, password=password)
        user.save()

if __name__ == '__main__':
    record_need_to_create = 20
    populate_data(record_need_to_create)
    print(f'{record_need_to_create} records generated.')
