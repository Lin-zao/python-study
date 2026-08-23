import streamlit as st

st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="👾",
    #布局
    layout="wide",
    #控制的是侧边栏的状态
    initial_sidebar_state="expanded",
    menu_items={}
)

#大标题
st.title("AI智能伴侣")

#logo
st.logo("resources/logo.png")