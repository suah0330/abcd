import streamlit as st

st.title('나의 첫 번째 스트림릿 앱 ✨')

# 사용자에게 텍스트 입력 받기
user_name = st.text_input("이름을 입력해주세요:")

# 버튼 생성
if st.button('인사하기'):
    if user_name:
        st.write(f"안녕하세요, {user_name}님! 만나서 반가워요.")
    else:
        st.write("이름을 입력해주세요.")
