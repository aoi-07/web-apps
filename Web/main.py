import streamlit as st

#認証前はサイドバーを非表示
if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.set_page_config(initial_sidebar_state="collapsed")
else:
    #認証後　サイドバーを開く
    st.set_page_config(initial_sidebar_state="expanded")

#pass
AUTH_password = "pass"

st.title("Python Apps Portal")
st.text("2026/03/23 更新")

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