from django.forms import ModelForm
#We are using our defined Todo
from .models import Todo

#Create the class that we are making
class TodoForm(ModelForm):
    #Defining a 'Meta' class which
    class Meta:
        model = Todo
        fields = ['title','description','important']
