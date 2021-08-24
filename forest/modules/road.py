import pandas as pd
import numpy as np
import pickle

def pred(a,b,c,d,e):
    col = [
    '作付面積(ha)',
    '気温平均日最高(℃)',
    '降水量合計',
    '降水量最大10分間',
    '最高気温(℃)'
    ]

    pre_test = pd.DataFrame(index=[], columns=col)
    test = [a, b, c, d, e]
    pre_test = pre_test.append(
        {'作付面積(ha)': test[0], '気温平均日最高(℃)': test[1], '降水量合計': test[2], '降水量最大10分間': test[3], '最高気温(℃)':test[4] },
        ignore_index=True)
    # 保存したモデルをロードする
    filename = "model.sav"
    model = pickle.load(open(filename, 'rb'))
    y_pred = model.predict(pre_test)
    return y_pred
