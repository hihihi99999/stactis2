import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 日本語フォントの設定
rcParams['font.family'] = 'IPAexGothic'  # システムにインストールされている日本語フォント名を指定

# データの作成
data = {
    "年度": list(range(1995, 2024)),
    "輸出額": [53.1, 59.3, 59.1, 57.6, 57.8, 63.4, 59.4, 61.4, 65.6, 70.1,
             72.9, 75.2, 78.4, 74.7, 49.2, 59.7, 62.3, 61.6, 70.0, 73.1,
             71.0, 63.3, 73.7, 75.6, 76.2, 63.4, 73.2, 82.8, 80.5],
    "輸入額": [41.1, 44.4, 46.5, 45.9, 46.7, 47.4, 46.9, 47.9, 52.7, 58.0,
             61.0, 65.2, 66.1, 72.0, 49.0, 62.0, 73.2, 73.7, 80.0, 78.8,
             72.8, 63.5, 75.1, 78.7, 78.3, 61.5, 82.0, 91.0, 90.2],
}

# データフレームの作成
df = pd.DataFrame(data)

# 貿易収支の計算
df["貿易収支"] = df["輸出額"] - df["輸入額"]

# Streamlitアプリケーションの設定
st.title('日本の輸出入額および貿易収支 (1995-2023)')
st.write('以下のグラフは、1995年から2023年までの日本の輸出額、輸入額、そして貿易収支の推移を示しています。')
st.write("単位(兆)")
# グラフの作成
fig, ax = plt.subplots(figsize=(12, 8))

# 貿易収支の色設定（マイナスは赤、プラスは青）
colors = ['red' if val < 0 else 'blue' for val in df["貿易収支"]]

# 横棒グラフの描画
bars = ax.barh(df["年度"], df["貿易収支"], color=colors)

# 各バーの外側に値を表示
for bar in bars:
    width = bar.get_width()
    ax.text(width + (0.5 if width > 0 else -0.5),  # 正の値は右側に、負の値は左側にオフセット
            bar.get_y() + bar.get_height() / 2,
            f'{width:.1f}兆円',
            ha='left' if width > 0 else 'right',
            va='center',
            color='black')

# y軸の目盛りを1年ごとに設定
ax.set_yticks(df["年度"])
ax.set_yticklabels(df["年度"])

# グラフのタイトルとラベル
ax.set_xlabel('貿易収支 (兆円)')
ax.set_ylabel('年度')
ax.set_title('日本の貿易収支の推移 (1995-2023)')

# グラフのレイアウト調整
plt.tight_layout()

# グラフの表示
st.pyplot(fig)