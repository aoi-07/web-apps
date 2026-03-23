import streamlit as st
import random
import time

#画面設定をワイドに設定
st.set_page_config(layout="wide")

btnlist = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]

st.title("Web版 まるばつゲーム")
msg_place = st.empty()
resetbtn = st.button("リセット",key="reset")

# ボタンの見た目変更
st.markdown("""
    <style>
    /* 盤面のボタンを特定して、縦のサイズを大幅にアップ */
    div[data-testid="stHorizontalBlock"] button {
        width: 230% !important;
        height: 80px !important; /* 高さを思い切って250px以上にしてみる */
        font-size: 30px !important; /* 文字もそれに合わせて巨大化 */
        font-weight: bold !important;
    }
    </style>
    """, unsafe_allow_html=True)


#セッション状態の初期化
if "board" not in st.session_state:
    # 3x3の盤面を空文字で作成
    st.session_state.board = [["" for _ in range(3)]for _ in range(3)]
    st.session_state.turnYou = True
    st.session_state.result = False
    st.session_state.msg = ""

#リセット
if resetbtn:
    st.session_state.board = [["" for _ in range(3)]for _ in range(3)]
    st.session_state.turnYou = True
    st.session_state.result = False
    st.session_state.msg = ""
    st.rerun()

#st.write(f"現在の番：{st.session_state.turn}")

#勝敗の表示
if st.session_state.msg != "":
    msg_place.write(st.session_state.msg)
    st.session_state.result = True

#勝敗の判定
def result(row,col):
    #勝ち
    if st.session_state.board[row][0] == st.session_state.board[row][1] == st.session_state.board[row][2] == "○" or \
        st.session_state.board[0][col] == st.session_state.board[1][col] == st.session_state.board[2][col] == "○" or \
            st.session_state.board[0][0] == st.session_state.board[1][1] == st.session_state.board[2][2] == "○" or \
                st.session_state.board[2][0] == st.session_state.board[1][1] == st.session_state.board[0][2] == "○":
        return "YOU WIN !!"
    #負け
    elif st.session_state.board[row][0] == st.session_state.board[row][1] == st.session_state.board[row][2] == "×" or \
        st.session_state.board[0][col] == st.session_state.board[1][col] == st.session_state.board[2][col] == "×" or \
            st.session_state.board[0][0] == st.session_state.board[1][1] == st.session_state.board[2][2] == "×" or \
                st.session_state.board[2][0] == st.session_state.board[1][1] == st.session_state.board[0][2] == "×":
        return "YOU LOSE ..."
    
    else:
        nowbtn = []
        for i,j in btnlist:
            nowbtn.append(st.session_state.board[i][j])
        #勝敗つかないまま9マス埋まった場合
        if "" not in nowbtn:
            return "DRAW..."
        else:
            return ""

side_left,game_area,side_right = st.columns([1,2,1])

with game_area:
    #盤面の作成
    for i in range(3):
        cols = st.columns(3)
        for j in range(3):
            with cols[j]:
                #盤面の状態をボタンのラベルにする
                label = st.session_state.board[i][j]
                if label == "":
                    label = " "
            
                if st.button(label,key=f"{i}-{j}") and st.session_state.msg == "":
                    #まだ押されていないボタンかどうかチェック
                    if st.session_state.board[i][j] == "":
                        #自分の手番のマークに書き換える
                        st.session_state.board[i][j] = "○"
                        st.session_state.msg = result(i,j)

                        #CPU
                        if st.session_state.msg == "":
                            blankbtn = []
                            for i,j in btnlist:
                                if st.session_state.board[i][j] == "":
                                    blankbtn.append([i,j])
                            if len(blankbtn) > 0:
                                i,j = random.choice(blankbtn)
                                st.session_state.board[i][j] = "×"
                                st.session_state.turnYou = True
                                st.session_state.result = [True if result(i,j) != "" else False]
                                st.session_state.msg = result(i,j)
                                st.rerun()
                    
                        #画面を強制的に再描画
                        st.rerun()


