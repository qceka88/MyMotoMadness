from django import forms

from MyMotoMadness.articles.models import ArticlesModel


class BasicArticleForm(forms.ModelForm):
    class Meta:
        model = ArticlesModel
        exclude = ['published']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Title'
                }
            ),
            'sub_title': forms.TextInput(
                attrs={
                    'placeholder': 'Sub Title'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description'
                }
            ),
        }


class CreateArticleForm(BasicArticleForm):
    ...


class EditArticleForm(BasicArticleForm):
    ...


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
