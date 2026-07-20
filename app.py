import streamlit as st

st.markdown("# AI 챗봇 만들기")
st.markdown("---")
st.markdown("## 질문을 하시면 AI 친구가 응답합니다.")
st.header("1. 기본 정보 입력")
user_id = st.text_input("이름", placeholder="이름")
grade = st.radio("학년", ["1", "2", "3"], horizontal=True)
age = st.number_input("반", min_value=1, max_value=11, value=1)
ai_speed = st.select_slider("난이도",options=["쉬움", "약간 애매", "보통", "조금 어려움", "어려움"],value="보통")
creativity = st.slider("점수", 0, 100, 50)
question = st.text_area("소감", placeholder="소감.")

if st.button("확인"):
    st.success(f"{user_id} / {grade}학년 / {age}반 / {ai_speed}")
    st.markdown(f"점수: `{creativity}`")
    st.info(f"소감: {question}")
