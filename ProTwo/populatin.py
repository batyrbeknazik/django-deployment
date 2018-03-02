from faker import Faker
import os
import random
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

django.setup()

from users.models import Names

faker = Faker()

def addNames(N=5):
    for a in range(N):
        fake_name=faker.name().split()
        fake_first = fake_name[0]
        fake_last = fake_name[1]
        fake_email = fake_first+fake_last+"@gmail.com"

        t=Names.objects.get_or_create(name=fake_first,lastname=fake_last,email=fake_email)[0]
        t.save()

if __name__=='__main__':
    print("populating for you")
    addNames(20)
    print("end population")