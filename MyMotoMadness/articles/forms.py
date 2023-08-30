from django import forms

from MyMotoMadness.articles.models import ArticlesModel


class BasicArticleForm(forms.ModelForm):
    class Meta:
        model = ArticlesModel
        exclude = ('published',)
        widgets = {
            'article_type': forms.Select(
                attrs={
                    'style': "height: 55px; width: 225px;",
                },
            ),
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


class SearchArticleForm(forms.Form):
    title__icontains = forms.CharField(
        required=False,
        label='Title:',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search by title.',
            }
        )
    )
    sub_title__icontains = forms.CharField(
        required=False,
        label='Sub Title:',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search by sub title.'
            }
        )
    )
