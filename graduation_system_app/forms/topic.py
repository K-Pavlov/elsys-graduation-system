from django.forms import ModelForm

from ..models.topic import Topic

class TopicForm(ModelForm):
    class Meta:
        model = Topic
        exclude = ('id')