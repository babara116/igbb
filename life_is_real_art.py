import streamlit as st

with st.sidebar:
    st.header("프로필")
    user_name = st.text_input("닉네임", key="user_name")
    weather = st.selectbox("오늘 날씨", ["맑음", "흐림", "비/눈", "매우 추움"], key="weather")
    st.markdown("---")
    st.info(f"반가워요, {user_name}님! 오늘 날씨는 '{weather}'이네요.")
