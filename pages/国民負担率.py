
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 国民負担率データの作成
data = {
    '年度': [1994 + i for i in range(31)],
    '国民負担率': [
        38.3, 35.2, 36.3, 36.2, 35.4, 35.6, 36.5, 35.0, 34.1, 34.5,
        36.2, 37.0, 37.9, 39.2, 37.2, 37.2, 38.8, 39.8, 40.1, 42.4,
        42.3, 42.7, 43.3, 44.2, 44.2, 47.7, 48.1, 48.4, 46.1, 45.1, 45.0
    ]
}

# データフレームの作成
df = pd.DataFrame(data)

# Streamlitアプリケーションの設定
st.title('日本の国民負担率の推移（1994年度～2024年度）')

# 横棒グラフの作成
plt.figure(figsize=(10, 12))
plt.barh(df['年度'], df['国民負担率'], color='b')
plt.xlabel('国民負担率（%）')
plt.ylabel('年度')
plt.title('日本の国民負担率の推移')
plt.grid(axis='x', linestyle='--', alpha=0.7)

# 各バーの横に値を表示
for index, (year, value) in enumerate(zip(df['年度'], df['国民負担率'])):
    plt.text(value + 0.5, year, f'{value:.1f}', va='center')

plt.tight_layout()

# グラフをStreamlitに表示
st.pyplot(plt)


st.write('（現状は年の半分は、税金を支払うために働いている）')
st.write('（消費税の増税分は社会保障費に充てると謳っているが、実際は輸出企業の減税に使われている）')
st.write('（日本の経済は成長していないが、輸出企業の売上は右肩上がりです。）')
st.write('（日本の国会議員の報酬も右肩上がりです）')
st.write('（99:1）のように1%を肥やすために99%が搾取されている')


st.page_link("app.py", label="Home", icon="🏚")
st.page_link("pages/page1.py", label="金価格の推移")
st.page_link("pages/page2.py", label="page2")