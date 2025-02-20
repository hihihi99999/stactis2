import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# データの作成
data = {
    "年度": list(range(1995, 2024)),
    "輸出額（兆円）": [
        53.1, 59.3, 59.1, 57.6, 57.8, 63.4, 59.4, 61.4, 65.6, 70.1,
        72.9, 75.2, 78.4, 74.7, 49.2, 59.7, 62.3, 61.6, 70.0, 73.1,
        71.0, 63.3, 73.7, 75.6, 76.2, 63.4, 73.2, 82.8, 80.5
    ]
}

# データフレームの作成
df = pd.DataFrame(data)

# Streamlitアプリケーションの設定
st.title('日本の年間輸出額の推移 (1995-2023)')
st.write('以下のグラフは、1995年から2023年までの日本の年間輸出額の推移を示しています。')

# グラフの作成
fig, ax = plt.subplots(figsize=(12, 8))
bars = ax.bar(df["年度"], df["輸出額（兆円）"], color='skyblue')

# 各バーの上に値を表示
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height,
            f'{height:.1f}兆円',
            ha='center', va='bottom')

# グラフのタイトルとラベル
ax.set_xlabel('年度')
ax.set_ylabel('輸出額（兆円）')
ax.set_title('日本の年間輸出額の推移 (1995-2023)')

# グラフのレイアウト調整
plt.xticks(rotation=45)
plt.tight_layout()

# グラフの表示
st.pyplot(fig)