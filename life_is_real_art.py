import streamlit as st
from openai import OpenAI

#ai_client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
st.session_state.user_name
st.set_page_config(page_title="기분 맞춤 추천기", page_icon="🍕", layout="centered")

st.title("🎧 오늘 뭐 먹고 뭐 듣지?")
st.caption("현재 당신의 상황과 기분에 딱 맞는 음식과 노래를 추천해 드려요!")

with st.sidebar:
    st.header("프로필")
    user_name = st.text_input("닉네임", key="user_name")
    weather = st.selectbox("오늘 날씨", ["맑음", "흐림", "비/눈", "매우 추움", "매우 더움"], key="weather")
    feel = st.selectbox("당신의 기분은 어떤가요?",["최악 😭", "우울/지침 😮‍💨", "평범 😐", "기분 좋음 😊", "텐션 최고! 🥳"])
    st.markdown("---")
    st.info(f"반가워요, {user_name}님! 오늘 날씨는 '{weather}'이네요."/n "당신의 기분은 '{feel}'이신가요? 이에 맞는 노래와 음식을 추천해 드릴게요!")
