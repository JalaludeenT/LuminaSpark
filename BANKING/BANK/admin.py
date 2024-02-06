from django.contrib import admin
from .models import District, Branch, Materials, Account_type, Gender, CreateAccount

# Register your models here.


admin.site.register(District)
admin.site.register(Branch)
admin.site.register(Materials)
admin.site.register(Account_type)
admin.site.register(Gender)
admin.site.register(CreateAccount)
