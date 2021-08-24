from django.shortcuts import render
from django import forms

class MyFirstForm(forms.Form):
    title = forms.CharField(max_length=100)
    context = forms.CharField(max_length=255)
    作付面積 = forms.IntegerField()
    気温平均最高 = forms.IntegerField()
    降水量合計 = forms.IntegerField()
    降水量最大10分間 = forms.IntegerField()
    最高気温 = forms.IntegerField()