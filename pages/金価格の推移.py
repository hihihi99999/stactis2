import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 金価格データの作成
data = {
    '年': list(range(1995, 2025)),
    '金価格（円/グラム）': [
        1243, 1471, 1337, 1287, 1069, 1014, 1105, 1296, 1472, 1619,
        2287, 2659, 2937, 2951, 3477, 4060, 4321, 4453, 4340, 4564,
        4396, 4576, 4543, 4918, 6122, 6402, 7649, 8834, 11718, 12882
    ]
}

# データフレームの作成
df = pd.DataFrame(data)

# Streamlitアプリケーションの設定
st.title('過去30年間の金価格推移')
st.write('1995年から2024年までの日本における金価格（円/グラム）の推移を示します。')

# データフレームの表示
st.dataframe(df)

# グラフの作成
plt.figure(figsize=(10, 5))
plt.plot(df['年'], df['金価格（円/グラム）'], marker='o')
plt.title('1995年から2024年の金価格推移')
plt.xlabel('年')
plt.ylabel('金価格（円/グラム）')
plt.grid(True)

st.write('（30年前から金価格は１０倍）')
st.write('（金そのものは価値が一定のため、金が高くなっているというよりかは、円が安くなっている）')
st.write('（金で資産を形成した人はかなりの利益が出ているはずである）')

# グラフの表示
st.pyplot(plt)