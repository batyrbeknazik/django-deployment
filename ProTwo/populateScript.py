from faker import Faker
import os
import random
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

django.setup()

from threeApp.models import AccessRecord,Webpage,Topic

fakegen = Faker()

topics=[ 'Search','Social','Marketplace','News','Games' ]

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t
def populate(N=5):
    for i in range(N):
        top = add_topic()

        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        webp = Webpage.objects.get_or_create(topic = top,url=fake_url,name=fake_name)[0]

        acc_rec = AccessRecord.objects.get_or_create(name = webp,date=fake_date)[0]

if __name__=='__main__':
    print('populating your database')
    populate(20)
    print('populating complete')





