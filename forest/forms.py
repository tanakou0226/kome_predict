from django.shortcuts import render
from django import forms

class MyFirstForm(forms.Form):
    作付面積 = forms.IntegerField()
    気温平均最高 = forms.IntegerField()
    降水量合計 = forms.IntegerField()
    降水量最大10分間 = forms.IntegerField()
    最高気温 = forms.IntegerField()