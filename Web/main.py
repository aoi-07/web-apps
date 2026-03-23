import streamlit as st

#pass
AUTH_password = "pass"

st.title("My Python Apps Portal")

#認証
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    pwd_input = st.text_input("パスワードを入力してください",type="password")
    if st.button("ログイン"):
        if pwd_input == AUTH_password:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("パスワードが違います")
    st.stop() #認証されるまでこれ以降の画面を表示しない

#認証後のメッセージ
st.write("認証に成功しました")
st.info("サイドメニューバーからアプリを選択してください。")