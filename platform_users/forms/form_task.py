
from django import forms
from platform_users.models import Task


class TaskForm(forms.ModelForm):

    title = forms.CharField(
        label='TITULO',
        error_messages= {
            'required': 'The title is required',
            'max_length': 'The text is too longer',
        },
        max_length=50,
    )
    desc = forms.CharField(
        label='DESCRICAO',
        widget=forms.Textarea()
    )

    is_published = forms.BooleanField(
        label='TAREFA PUBLICA',
    )

    is_finished = forms.BooleanField(
        label='TAREFA FINALIZADA',
    )

    class Meta:
        model = Task
        fields = ['title', 'desc', 'is_published', 'is_finished']
