from django.contrib import admin
from .models import Todo

#This allows us to customize the /admin interface, eg. show readonly fields
class TodoAdmin(admin.ModelAdmin):
    #This 'created_date' name comes from inside the model.py
    readonly_fields = ['created_date']

# Register your models here.
#We can show this new class 'TodoAdmin' now
admin.site.register(Todo, TodoAdmin)
#or we can show the generic 'Todo' class which was defined in models.py
#However, you can only register ONE of them
#admin.site.register(Todo)