import streamlit as st
import random
if 'total_count' not in st.session_state:
    st.session_state.total_count = 0
if 'win_count' not in st.session_state:
    st.session_state.win_count = 0
if 'loss_count' not in st.session_state:
    st.session_state.loss_count = 0
st.set_page_config(page_title="幸运抽奖", page_icon="🎰")
st.title("🎰 幸运大抽奖")

if st.button('6 点击开始抽奖 7'):
    luckly = random.randint(0, 1000)
    st.subheader(f"current luckly: {luckly}")

ol1, col2, col3 = st.columns(3)
col1.metric("总抽奖次数", st.session_state.total_count)
col2.metric("累计赢奖", st.session_state.win_count)
col3.metric("累计空奖", st.session_state.loss_count)
    
    if luckly == 91:
        st.success("wow*congratulations*wow")
        st.markdown("#you get $91919")
    elif luckly == 78:
        st.success("wow*congratulations*wow")
        st.markdown("#you get $78787")
    elif luckly == 13:
        st.success("wow*congratulations*wow")
        st.markdown("#you get $13131")
    elif luckly == 714:
        st.warning("懂你意思")
        st.markdown("#you get $71400")
        st.text("kskbl?🤨")
        st.text("zdjd🧐")
        st.text("wkzkbl😮")
        st.text("wzbyqs😤")
        st.text("nzzyswwzbsbll🥵")
    elif luckly == 999:
        st.balloons()
        st.success("wow;;;😮congratulations😮;;;wow")
        st.markdown("#you get $488888")
    elif luckly == 888:
        st.balloons()
        st.success("😮wow;;;😮congratulations😮;;;wow😮")
        st.markdown("#you get $888888")
        st.write("😮😮😮😮😮😮😮😮😮😮")
    elif luckly >= 990:
        st.snow()
        st.success(";;;congratulations;;;")
        money = random.randint(100000, 150000)
        st.markdown(f"#currnet money:you get ${money}")
    elif luckly >= 900:
        st.success(";;;congratulations;;;")
        money = random.randint(50000, 80000)
        st.markdown(f"#currnet money:you get ${money}")
    elif luckly >= 800:
        st.success(";;;congratulations;;;")
        money = random.randint(20000, 30000)
        st.markdown(f"#currnet money:you get ${money}")
    elif luckly >= 700:
        st.success(";;;congratulations;;;")
        money = random.randint(10000, 12500)
        st.markdown(f"#currnet money:you get ${money}")
    elif 1 <= luckly <= 10:
        st.success(";;;congratulations;;;")
        money = random.randint(10000, 12500)
        st.markdown(f"#currnet money:you get ${money}")
    else:
        st.error("🤣you get notting🤣")
        st.write("🤣lol🤣get the fuck away🤣lol🤣")
        st.write("🤣you fucking noob🤣")
        st.write("🤣lol🤣")
        st.write("🤮ewwwwwwwwwww🤮")
        st.write("🤮ewwwwwwwwwww🤮")
