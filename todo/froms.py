from django import forms
from todo.models import Task

class TodoForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"

class TodoRemove(forms.Form):
    name = forms.CharField(max_length=50)