import streamlit as st
from openai import OpenAI

#ai_client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
st.set_page_config(page_title="기분 맞춤 추천기", page_icon="🍕", layout="centered")

st.title("🎧 오늘 뭐 먹고 뭐 듣지?")
st.caption("현재 당신의 상황과 기분에 딱 맞는 음식과 노래를 추천해 드려요!")

with st.sidebar:
    st.header("프로필")
    user_name = st.text_input("닉네임", key="user_name")
    weather = st.selectbox("오늘 날씨", ["☀️ 화창하고 밝음", "🌧️ 비가 내림", "☁️ 흐리고 꿀꿀함", "❄️ 춥거나 눈이 옴", "🌙 센치한 밤"], key="weather")
    feel = st.selectbox("당신의 기분은 어떤가요?",["최악 😭", "우울/지침 😮‍💨", "평범 😐", "기분 좋음 😊", "텐션 최고! 🥳"])
    with_whom = st.selectbox("👥 누구와 함께 있나요?", ["👤 나 혼자만의 시간", "👥 친구들과 함께", "💕 연인과 데이트", "🏠 가족들과 함께"])
    st.markdown("---")
    st.info(f"반가워요, {user_name}님! 오늘 날씨는 '{weather}'이네요. 당신의 기분은 '{feel}'이신가요? 그렇다면 이기분과 {with_whom}일때에 맞는 노래와 음식을 추천해 드릴게요!")
