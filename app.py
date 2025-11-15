import streamlit as st
import random
import time

# --- 게임 설정 ---
GRID_WIDTH = 10
GRID_HEIGHT = 20
EMPTY = 0
FILLED = 1

st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

# 게임 상태 초기화
if 'board' not in st.session_state:
    st.session_state.board = [[EMPTY for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

def create_new_block():
    """간단한 1x1 블록을 맨 위에 생성합니다 (복잡한 테트리스 블록 대신 단순화)"""
    # 랜덤한 위치에 블록을 놓습니다
    x = random.randint(0, GRID_WIDTH - 1)
    y = 0
    if st.session_state.board[y][x] == FILLED:
        st.session_state.game_over = True
    else:
        st.session_state.board[y][x] = FILLED

def draw_board():
    """현재 게임 보드를 Streamlit에 표시합니다"""
    html_code = "<div style='display: grid; grid-template-columns: repeat(" + str(GRID_WIDTH) + ", 20px);'>"
    for row in st.session_state.board:
        for cell in row:
            color = 'gray' if cell == EMPTY else 'blue'
            html_code += f"<div style='width: 20px; height: 20px; background-color: {color}; border: 1px solid #ddd;'></div>"
    html_code += "</div>"
    st.markdown(html_code, unsafe_allow_html=True)

def move_down():
    """모든 블록을 한 칸 아래로 이동시킵니다"""
    if st.session_state.game_over:
        return

    new_board = [[EMPTY for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    moved = False
    for r in range(GRID_HEIGHT - 2, -1, -1):
        for c in range(GRID_WIDTH):
            if st.session_state.board[r][c] == FILLED:
                if st.session_state.board[r+1][c] == EMPTY:
                    new_board[r+1][c] = FILLED
                    moved = True
                else:
                    new_board[r][c] = FILLED # 아래 칸이 차있으면 그대로 둠
    
    st.session_state.board = new_board
    if not moved:
        # 더 이상 움직일 블록이 없으면 새 블록 생성
        check_lines()
        create_new_block()

def check_lines():
    """완성된 줄을 제거하고 점수를 추가합니다"""
    new_board = []
    lines_cleared = 0
    for row in st.session_state.board:
        if EMPTY in row:
            new_board.append(row)
        else:
            lines_cleared += 1
            st.session_state.score += 10
    
    # 제거된 줄 수만큼 빈 줄을 맨 위에 추가
    for _ in range(lines_cleared):
        new_board.insert(0, [EMPTY for _ in range(GRID_WIDTH)])
    
    st.session_state.board = new_board


# --- UI 구성 ---

st.sidebar.title("조작")
st.sidebar.button('블록 아래로 이동', on_click=move_down)
st.sidebar.button('새 블록 생성', on_click=create_new_block)

st.write(f"현재 점수: **{st.session_state.score}**")

if st.session_state.game_over:
    st.error("게임 오버! 😭")
    if st.button("다시 시작"):
        st.session_state.board = [[EMPTY for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        st.session_state.score = 0
        st.session_state.game_over = False
        st.rerun()

draw_board()
