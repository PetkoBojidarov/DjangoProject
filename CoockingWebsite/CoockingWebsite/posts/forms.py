from django import forms

from CoockingWebsite.posts.models import Post, Comment


class BasePostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author', 'created_at', 'updated_at']


class PostAddForm(BasePostForm):
    pass


class PostEditForm(BasePostForm):
    pass


class PostDeleteForm(BasePostForm):
    pass


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text',]

        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Add comment...'}),
        }
