from django import forms

from CoockingWebsite.posts.models import Post


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
