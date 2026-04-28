import streamlit as st
import random

# --- 1. 初始化账本 (只在第一次打开时运行) ---
if 'total' not in st.session_state:
    st.session_state.total = 0
if 'wins' not in st.session_state:
    st.session_state.wins = 0
if 'losses' not in st.session_state:
    st.session_state.losses = 0

st.set_page_config(page_title="幸运抽奖", page_icon="🎰")
st.title("🎰 幸运大抽奖")

# --- 2. 显示统计数据 (用 metric 组件很漂亮) ---
col1, col2, col3 = st.columns(3)
col1.metric("总抽奖次数", st.session_state.total)
col2.metric("中奖次数", st.session_state.wins)
col3.metric("空奖次数", st.session_state.losses)

# 抽奖按钮
if st.button('🔥 点击开始抽奖 🔥'):
    # 只要点按钮，总数就加 1
    st.session_state.total += 1
    
    luckly = random.randint(0, 1000)
    st.subheader(f"current luckly: {luckly}")
    
    # 定义中奖逻辑 (把你的那些中奖数字都放进来)
    is_win = False
    if luckly in [91, 78, 13, 714, 999, 888] or luckly >= 700 or (1 <= luckly <= 10):
        is_win = True

    if is_win:
        st.session_state.wins += 1
        # --- 这里放你原本的所有奖励逻辑 ---
        if luckly == 91:
            st.success("wow*congratulations*wow\nyou get $91919")
        elif luckly == 78:
            st.success("wow*congratulations*wow\nyou get $78787")
        elif luckly == 888:
            st.balloons()
            st.success("😮wow;;;😮congratulations😮;;;wow😮\nyou get $888888")
        elif luckly >= 700:
            st.success(";;;congratulations;;;")
            money = random.randint(10000, 30000)
            st.markdown(f"#you get ${money}")
        # (篇幅原因，其他 elif 你可以根据之前的代码照样补齐)
        
    else:
        st.session_state.losses += 1
        # --- 这里放你原本的失败逻辑 (ewwww) ---
        st.error("🤣you get notting🤣")
        st.write("🤮ewwwwwwwwwww🤮")

# --- 3. 添加一个重置按钮 ---
if st.sidebar.button('重置统计数据'):
    st.session_state.total = 0
    st.session_state.wins = 0
    st.session_state.losses = 0
    st.rerun()
    
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
