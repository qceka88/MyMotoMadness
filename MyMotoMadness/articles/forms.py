from django import forms

from MyMotoMadness.articles.models import ArticlesModel


class BasicArticleForm(forms.ModelForm):
    class Meta:
        model = ArticlesModel
        exclude = ('published',)
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Title',
                    'style': "height: 55px",
                }
            ),
            'sub_title': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Sub Title',
                    'style': "height: 55px",
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Enter Article Content'
                }
            ),
            'author': forms.HiddenInput(

            ),
            'article_type': forms.Select(
                attrs={
                    'style': "height: 55px",
                }
            )
        }


class CreateArticleForm(BasicArticleForm):
    ...


class EditArticleForm(BasicArticleForm):
    BasicArticleForm.Meta.exclude = ('published', 'author')


class DeleteArticleForm(BasicArticleForm):
    class Meta:
        model = ArticlesModel
        fields = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance
