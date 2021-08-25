from django.shortcuts import render
from django.http import HttpResponse
from .forms import MyFirstForm

import pandas as pd
import numpy as np
import pickle
from home.settings import BASE_DIR

# Create your views here.
def index(request):
    # 関数作成
    def pred(a,b,c,d,e):
        col = ['作付面積(ha)','気温平均日最高(℃)','降水量合計','降水量最大10分間','最高気温(℃)']

        pre_test = pd.DataFrame(index=[], columns=col)
        test = [a, b, c, d, e]
        pre_test = pre_test.append(
            {'作付面積(ha)': test[0], '気温平均日最高(℃)': test[1], '降水量合計': test[2], '降水量最大10分間': test[3], '最高気温(℃)':test[4] },
            ignore_index=True)
        # 保存したモデルをロードする
        model = pickle.load(open(str(BASE_DIR) + '/data/model.sav', 'rb'))
        y_pred = model.predict(pre_test)
        return y_pred

    form = MyFirstForm()
    title = None
    ans = "数値を入力してください"
    try:
        a = request.GET["作付面積"]
        b = request.GET["気温平均最高"]
        c = request.GET["降水量合計"]
        d = request.GET["降水量最大10分間"]
        e = request.GET["最高気温"]
        ans = pred(a,b,c,d,e)
    except:
        pass
    params = {
        'title' : "お米の収穫量を予測！",
        'msg'   : '',
        "form"  : form,
        "pred"  : ans,
    }
    form = MyFirstForm()
    context = {"form":form}
    return render(request, 'hello/index.html', params)