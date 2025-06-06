from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'video_file', 'category']


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(
        label="密码",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text="至少8个字符"
    )
    password2 = forms.CharField(
        label="重复输入密码",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text="再次输入密码"
    )

    username = forms.CharField(
        label="用户名",
        help_text="必填字段"
    )

    class Meta:
        model = User
        #fields = ('username', 'password1', 'password2', 'email')
        fields = ('username', 'password1', 'password2')

