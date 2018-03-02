from django.contrib import admin
from threeApp.models import AccessRecord,Topic,Webpage
from users.models import Names
# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(Names)