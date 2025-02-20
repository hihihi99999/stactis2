import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# ページ設定
st.set_page_config(page_title="日本の統計データ", layout="wide")

# タイトルと説明
st.title("日本の統計の全体像をstreamlitで作りました")


st.write("")
st.write("")
st.write("")

# 大きなフォントサイズでサイドバーの説明を表示
st.markdown("<h1 style='text-align: left; font-size: 32px;'>サイドバーのリンクより様々な統計をご確認ください</h1>", unsafe_allow_html=True)

st.write("")
st.write("")

# サイドバーの作成
st.sidebar.header("データの選択")
selected_data = st.sidebar.selectbox(
    "表示するデータを選択してください",
    ["人口統計", "経済指標", "社会指標"]
)

# サンプルデータの作成（実際のアプリではAPIやCSVからデータを取得）
def generate_population_data():
    years = list(range(2010, 2025))
    population = [128057352, 127799000, 127515000, 127298000, 127083000,
                 126919000, 126706000, 126472000, 126246000, 125960000,
                 125710000, 125440000, 125180000, 124840000, 124500000]
    return pd.DataFrame({
        '年': years,
        '総人口': population
    })

def generate_economic_data():
    years = list(range(2010, 2025))
    gdp = [5759.0, 5706.0, 5937.0, 6155.0, 6203.0,
           6317.0, 6380.0, 6622.0, 6799.0, 6846.0,
           6759.0, 6931.0, 7078.0, 7225.0, 7380.0]
    return pd.DataFrame({
        '年': years,
        'GDP（兆円）': gdp
    })

def generate_social_data():
    years = list(range(2010, 2025))
    birth_rate = [1.39, 1.39, 1.41, 1.43, 1.42,
                  1.45, 1.44, 1.43, 1.42, 1.36,
                  1.34, 1.33, 1.31, 1.30, 1.29]
    return pd.DataFrame({
        '年': years,
        '合計特殊出生率': birth_rate
    })

# データの表示
if selected_data == "人口統計":
    st.header("人口統計")
    
    population_df = generate_population_data()
    
    # 折れ線グラフ
    fig = px.line(population_df, x='年', y='総人口',
                  title='日本の総人口推移',
                  labels={'総人口': '人口（人）'})
    st.plotly_chart(fig, use_container_width=True)
    
    # データテーブル
    st.markdown("### 詳細データ")
    st.dataframe(population_df)

elif selected_data == "経済指標":
    st.header("経済指標")
    
    economic_df = generate_economic_data()
    
    # 棒グラフ
    fig = px.bar(economic_df, x='年', y='GDP（兆円）',
                 title='日本のGDP推移',
                 labels={'GDP（兆円）': 'GDP（兆円）'})
    st.plotly_chart(fig, use_container_width=True)
    
    # データテーブル
    st.markdown("### 詳細データ")
    st.dataframe(economic_df)

else:
    st.header("社会指標")
    
    social_df = generate_social_data()
    
    # エリアチャート
    fig = px.area(social_df, x='年', y='合計特殊出生率',
                  title='合計特殊出生率の推移',
                  labels={'合計特殊出生率': '出生率'})
    st.plotly_chart(fig, use_container_width=True)
    
    # データテーブル
    st.markdown("### 詳細データ")
    st.dataframe(social_df)

# 補足情報
st.markdown("---")
st.markdown("""
### データについて
- このデータは参考値です。実際の統計データは政府統計ポータルサイトe-Statなどで確認できます。
- グラフはStreamlitとPlotlyを使用して作成しています。
""")

st.page_link("app.py", label="Home", icon="🏚")
st.page_link("pages/金価格の推移.py", label="Page1")
st.page_link("pages/国民負担率.py", label="Page2")
st.page_link("pages/貿易収支.py", label="Page3")
st.page_link("pages/輸出企業の売上推移.py", label="Page4")