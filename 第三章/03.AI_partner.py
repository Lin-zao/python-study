import streamlit as st
import os
from openai import OpenAI


st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🚤",
    #布局
    layout="wide",
    #控制的是侧边栏的状态
    initial_sidebar_state="expanded",
    menu_items={}
)

#大标题
st.title("AI智能伴侣")

#logo
st.logo("./resources/logo.png")

#系统提示词
system_prompt = "你是一名非常可爱的AI助理,你的名字叫小甜甜,请你使用温柔可爱的预期回答问题"

#初始化聊天信息
if "messages" not in st.session_state:
    st.session_state['messages'] = [{"role": "system", "content": system_prompt}]

#展示聊天信息
for message in st.session_state['messages']:
    st.chat_message(message["role"]).write(message["content"])

#创建与AI大模型交互的客户端对象
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

#消息输入框
prompt = st.chat_input("请输入您要问的问题")
if prompt:#字符串会自动转化为布尔值
    st.chat_message("user").write(prompt)
    st.session_state['messages'].append({"role": "user", "content": prompt})
    #调用AI大模型
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )
    st.session_state['messages'].append({"role": "assistant", "content": response.choices[0].message.content})

    st.chat_message("assistant").write(response.choices[0].message.content)




