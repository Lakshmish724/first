from django import forms

class EmailSendForm(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()
	to = forms.CharField()
	comments = forms.CharField(required=False, widget=forms.Textarea)

from app1.models import Comment


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name', 'email', 'body')