from turtle import title
from django import forms

class NewsForm(forms.Form):
    title = forms.CharField(
        error_messages= {
            "required" : "제목 입력"
        },
        max_length=200, label="제목"
    )
