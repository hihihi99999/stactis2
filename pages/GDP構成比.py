import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# データの作成
data = {
    '産業': ['農林水産業', '鉱業、電気・ガス・水道業', '製造業', '建設業', '商業、飲食・宿泊業', '運輸・倉庫業、通信業', 'その他サービス業'],
    'GDP構成比率（%）': [1.0, 3.1, 20.2, 5.6, 14.8, 9.6, 45.3]
}

# データフレームの作成
df = pd.DataFrame(data)

# Streamlitアプリケーションの設定
st.title('日本の産業別GDP構成比率')
st.write('以下の表とグラフは、日本の各産業におけるGDP構成比率を示しています。')

# データフレームの表示
st.dataframe(df)

# 円グラフの作成
fig, ax = plt.subplots()
ax.pie(df['GDP構成比率（%）'], labels=df['産業'], autopct='%1.1f%%', startangle=90, counterclock=False)
ax.axis('equal')  # 円を円形にするための設定
plt.title('日本の産業別GDP構成比率', fontsize=16)

# グラフの表示
st.pyplot(fig)