import streamlit as st
import random

st.title("가위바위보 게임 ✊✋✌️")

# 게임 옵션과 이모지 정의
options = {"바위": "✊", "가위": "✌️", "보": "✋"}
choices = list(options.keys())

# 게임 상태 초기화 (Session State 사용)
if 'user_score' not in st.session_state:
    st.session_state.user_score = 0
if 'computer_score' not in st.session_state:
    st.session_state.computer_score = 0
if 'result_message' not in st.session_state:
    st.session_state.result_message = "게임을 시작해 보세요!"


def play_game(user_choice):
    """게임 로직 처리 및 결과 업데이트"""
    computer_choice = random.choice(choices)
    user_emoji = options[user_choice]
    computer_emoji = options[computer_choice]
    
    result = ""

    if user_choice == computer_choice:
        result = "비겼습니다!"
    elif (user_choice == "바위" and computer_choice == "가위") or \
         (user_choice == "가위" and computer_choice == "보") or \
         (user_choice == "보" and computer_choice == "바위"):
        result = "🎉 **당신이 이겼습니다!**"
        st.session_state.user_score += 1
    else:
        result = "💻 컴퓨터가 이겼습니다."
        st.session_state.computer_score += 1
    
    st.session_state.result_message = f"**당신**: {user_emoji} vs **컴퓨터**: {computer_emoji} -> {result}"


# --- 앱 레이아웃 ---

# 점수판 표시
col1, col2 = st.columns(2)
with col1:
    st.metric("내 점수", st.session_state.user_score)
with col2:
    st.metric("컴퓨터 점수", st.session_state.computer_score)

st.markdown("---")

# 게임 결과 메시지 출력
st.subheader(st.session_state.result_message)

st.markdown("---")

# 사용자 선택 버튼
st.write("가위, 바위, 보 중 선택하세요:")
col_btns = st.columns(3)

with col_btns[0]:
    # 버튼 클릭 시 play_game 함수 실행 및 인자 전달
    st.button("바위 ✊", on_click=play_game, args=["바위"])
with col_btns[1]:
    st.button("가위 ✌️", on_click=play_game, args=["가위"])
with col_btns[2]:
    st.button("보 ✋", on_click=play_game, args=["보"])

# 리셋 버튼
if st.button("점수 초기화"):
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.session_state.result_message = "점수가 초기화되었습니다. 다시 시작하세요!"
    st.rerun() # 앱을 다시 로드하여 초기화된 상태 반영
