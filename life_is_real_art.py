import streamlit as st
from openai import OpenAI

ai_client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
st.set_page_config(page_title="기분 맞춤 추천기", page_icon="🍕", layout="centered")

st.title("🎧 오늘 뭐 먹고 뭐 듣지?")
st.caption("현재 당신의 상황과 기분에 딱 맞는 음식과 노래를 추천해 드려요!")

with st.sidebar:
    st.header("프로필")
    user_name = st.text_input("닉네임", key="user_name")
    weather = st.selectbox("오늘 날씨", ["☀️ 화창하고 밝음", "🌧️ 비가 내림", "☁️ 흐리고 꿀꿀함", "❄️ 춥거나 눈이 옴", "🌙 센치한 밤"], key="weather")
    feel = st.selectbox("당신의 기분은 어떤가요?",["최악 😭", "우울/지침 😮‍💨", "평범 😐", "기분 좋음 😊", "텐션 최고! 🥳"])
    with_whom = st.selectbox("👥 누구와 함께 있나요?", ["👤 나 혼자만의 시간", "👥 친구들과 함께", "💕 연인과 데이트", "🏠 가족들과 함께"])
    genre = st.selectbox("🎶 어떤 장르의 노래를 듣고싶나요?", ["힙합", "발라드", "트로트", "팝송","동요"])
    extra_info = st.text_input("💡 추가로 들려주고 싶은 이야기가 있나요? (선택)", placeholder="예: 오늘 시험이 끝났어요, 외국 힙합이 듣고싶어요 등")
    st.markdown("---")
    st.info(f"반가워요, {user_name}님! 오늘 날씨는 '{weather}'이네요. 당신의 기분은 '{feel}'이신가요? 그렇다면 이 기분과 '{with_whom}'일때에 맞는 노래와 음식을 추천해 드릴게요!")

if st.button("✨ 맞춤 추천 받기", use_container_width=True):
    prompt = f"""기분이랑 날씨와 누구랑 있는지에 따라서 어떤 노래를 추천해 주셨으면 좋겠어요! 아래 사용자와 적합한 노래 3곡을 추천해주세요! 
        [사용자 상황]
    - 날씨: {weather}
    - 함께 있는 사람: {with_whom}
    - 현재 기분: {feel}
    - 추가 정보: {extra_info if extra_info else '없음'}

    [출력 형식]
    1. 🍽️ **오늘의 추천 음식**: (음식 이름)
       - 추천 이유: (다정한 어조로 2~3줄 설명)
    2. 🎵 **기분 맞춤 플레이리스트**:
       - 곡 1: 가수 - *노래 제목*
         (추천 이유 한 줄)          <---여기는 노래제목이랑 추천이유는 꼭 칸을 나눠주세요
       - 곡 2: 가수 - *노래 제목*
         (추천 이유 한 줄)
       - 곡 3: 가수 - *노래 제목*
         (추천 이유 한 줄)
    3. 음악의 배경 지식과 이러한 음악 선정의 이유를 간단하게 설명해서 유튜브의 영상을 넣어서 바로 틀수있게 마무리 해줘
    
    """

with st.spinner("당신의 기분에 딱 맞는 조합을 찾고 있어요... 🔮"):
        try:
            response = ai_client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )
            
            # 결과 출력
            result = response.choices[0].message.content
            
            st.success("🎉 추천이 도착했습니다!")
            st.markdown(result)
            
        except Exception as e:
            st.error(f"오류가 발생했습니다: {e}")
