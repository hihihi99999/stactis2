import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# データの作成
data = {
    '年度': [2018, 2019, 2020, 2021, 2022, 2023],
    'カロリーベース自給率（%）': [37, 38, 38, 37, 38, 38],
    '生産額ベース自給率（%）': [66, 67, 70, 67, 58, 61]
}

# データフレームの作成
df = pd.DataFrame(data)

# Streamlitアプリケーションの設定
st.title('日本の食料自給率の推移')
st.write('以下の表とグラフは、2018年から2023年までの日本のカロリーベースおよび生産額ベースの食料自給率の推移を示しています。')

# データフレームの表示
st.dataframe(df)

# グラフの作成
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(df['年度'], df['カロリーベース自給率（%）'], marker='o', label='カロリーベース自給率（%）')
ax.plot(df['年度'], df['生産額ベース自給率（%）'], marker='s', label='生産額ベース自給率（%）')

# グラフのタイトルとラベル
ax.set_title('日本の食料自給率の推移（2018年～2023年）', fontsize=16)
ax.set_xlabel('年度', fontsize=14)
ax.set_ylabel('自給率（%）', fontsize=14)
ax.set_xticks(df['年度'])
ax.set_ylim(0, 100)
ax.legend()
ax.grid(True)

# グラフの表示
st.pyplot(fig)