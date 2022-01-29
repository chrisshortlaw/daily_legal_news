from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    '''
    Form for submission of comments to articles
    Fields:
        - article: Type[Article]
        - body: TextField
        - parent: Type[Comment], default=None
        - approved: Boolean Field, default=False
    '''
    class Meta:
        model = Comment
        fields = ('article', 'body', 'user',
                  'parent', 'approved',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
                'body': 'What do you want to say?'
                }
        for field in self.fields:
            if field in placeholders:
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].label = False
            else:
                pass

