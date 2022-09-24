
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
        widget=forms.Textarea(),
        required=False,
    )

    is_published = forms.BooleanField(
        label='TAREFA PUBLICA',
        required=False,
    )

    is_finished = forms.BooleanField(
        label='TAREFA FINALIZADA',
        required=False,
    )

    class Meta:
        model = Task
        fields = ['title', 'desc', 'is_published', 'is_finished']
