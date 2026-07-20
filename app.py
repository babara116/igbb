import streamlit as st

st.markdown("# AI 챗봇 만들기")
st.markdown("---")
st.markdown("## 질문을 하시면 AI가 응답 할 수 도있고 아닐 수 도있고.")
st.header("1. 기본 정보 입력")
user_id = st.text_input("아이디(ID) 입력해라", placeholder="example_user")
age = st.number_input("나이를 입력해라", min_value=1, max_value=100, value=17)
question = st.text_area("AI에게 보낼 질문을 입력하든가 말든가", placeholder="여기에 질문을 작성해 주세요.")

st.header("2. 챗봇 설정")
ai_model = st.radio("사용할 AI 모델을 선택해", ["GPT-4", "Claude 3", "Gemini Pro"], horizontal=True)
tone = st.selectbox("답변의 말투를 골라봐", ["친절하게", "냉철하게", "유머러스하게"])
features = st.multiselect("추가 기능을 선택하세요", ["뭘봐", "자신있냐?", "싸울래?", "뒤질라꼬"])
creativity = st.slider("AI의 창의성 수준을 설정하세요", 0, 10000000000, 50)
ai_speed = st.select_slider("응답 처리 속도를 선택하세요",options=["ㅈㄴ 느림", "뭐 평범하게 느림", "애매모호함 ㅇㅇ", "나쁘지 않은 정도임", "ㅈㄴ 빠름 ㅅㅂ"],value="애매모호함 ㅇㅇ")
agree = st.checkbox("개인정보 수집 및 AI 학습 이용에 동의합니다.")
st.markdown("---")

if st.button("질문 전송하기"):
    if agree:
        st.success(f"성공적으로 전송되었습니다! ({user_id}님)")
        st.markdown(f"""
        * **질문 내용:** {question}
        * **선택 모델:** `{ai_model}` | **말투:** `{tone}`
        * **활성화 기능:** {', '.join(features) if features else '없음'}
        * **창의성:** `{creativity}%` | **처리 속도:** `{ai_speed}`
        """)
        
        if age < 14:
            st.info("참고: 14세 미만 사용자이므로 보호자 모드가 활성화됩니다.")
    else:
        st.error("⚠️ 동의 항목에 체크해야 전송이 가능합니다.")
