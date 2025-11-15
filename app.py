import streamlit as st

# 웹 앱의 제목 설정
st.title('나의 첫 스트림릿 앱')

# 헤더 추가
st.header('간단한 예제입니다')

# 텍스트 입력 위젯 추가
user_input = st.text_input("여기에 메시지를 입력하세요:", "Hello, Streamlit!")

# 입력받은 텍스트 표시
st.write('사용자가 입력한 메시지:', user_input)
