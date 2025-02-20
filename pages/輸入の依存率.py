import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# データの作成
data = {
    '品目': ['原油', '石炭', '液化天然ガス（LNG）', '小麦', '大豆', '衣類', '鉄鉱石'],
    '輸入依存度': [88, 99.6, 100, 90, 95, 55.8, 100],  # 数値データに変更
    '主な輸入先国': ['中東諸国（約8割）', 'オーストラリア（約6割）', 'オーストラリア、マレーシア、カタール', 
                 'アメリカ、カナダ、オーストラリア', 'アメリカ、ブラジル', '中国', 'オーストラリア']
}

# データフレームの作成
df = pd.DataFrame(data)

# Streamlitアプリケーションの設定
st.title('日本の主な品目の輸入依存度')
st.write('以下の表は、日本の主な品目における輸入依存度と主な輸入先国を示しています。')

# データフレームの表示
st.dataframe(df)

# グラフの作成
plt.figure(figsize=(10, 6))
sns.set(style="whitegrid")
barplot = sns.barplot(x='輸入依存度', y='品目', data=df, palette='viridis')

# グラフのタイトルとラベル
plt.title('日本の主な品目の輸入依存度', fontsize=16)
plt.xlabel('輸入依存度（%）', fontsize=14)
plt.ylabel('品目', fontsize=14)

st.write("")
st.write("原油が止まると、全ての経済活動が止まります。発電ができないからです。全ての工業製品は原油に依存しています。")
st.write("第二次世界対戦は原油のための戦いでした。原油を止められたため、戦争をせざるを得ない状況になりました")
st.write("その状況は今も変わりはないです。他国に依存しています。資源の安全保障のリスクは高い")
st.write("原油の価格上昇するは全ての価格を上げます。円安に輸入コストの増加により現在も価格上昇（インフレ）が起きています")
st.write("")

# 各バーの横に値を表示
for index, value in enumerate(df['輸入依存度']):
    barplot.text(value + 1, index, f'{value}%', color='black', va="center")

# グラフの表示
st.pyplot(plt)