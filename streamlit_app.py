import streamlit as st
import random

# --- 1. 初始化账本 (让网页记住数据) ---
if 'total' not in st.session_state:
    st.session_state.total = 0
if 'wins' not in st.session_state:
    st.session_state.wins = 0
if 'losses' not in st.session_state:
    st.session_state.losses = 0
if 'profit' not in st.session_state:
    st.session_state.profit = 0

st.set_page_config(page_title="超级抽奖机", page_icon="💰")
st.title("🎰 幸运大抽奖")

# --- 2. 显示仪表盘 (新增累计盈利) ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("总抽奖次数", st.session_state.total)
col2.metric("中奖次数", st.session_state.wins)
col3.metric("空奖次数", st.session_state.losses)
# delta 是变化量，这里用来显示盈利总额，非常专业
col4.metric("累计盈利", f"${st.session_state.profit}", delta=f"{st.session_state.profit} USD")

# 抽奖按钮
if st.button('🔥 点击开始抽奖 🔥'):
    st.session_state.total += 1
    luckly = random.randint(0, 1000)
    st.subheader(f"current luckly: {luckly}")
    
    current_money = 0  # 用来记录本次抽奖赚了多少
    
    # --- 3. 核心逻辑：判断奖金并累加盈利 ---
    if luckly == 91:
        current_money = 91919
        st.success(f"wow*congratulations*wow\nyou get ${current_money}")
    elif luckly == 78:
        current_money = 78787
        st.success(f"wow*congratulations*wow\nyou get ${current_money}")
    elif luckly == 13:
        current_money = 13131
        st.success(f"wow*congratulations*wow\nyou get ${current_money}")
    elif luckly == 714:
        st.warning("懂你意思")
        st.markdown("#you get $71400")
        st.text("kskbl?🤨")
        st.text("zdjd🧐")
        st.text("wkzkbl😮")
        st.text("wzbyqs😤")
        st.text("nzzyswwzbsbll🥵")
    elif luckly == 999:
        current_money = 488888
        st.balloons()
        st.success(f"wow;;;😮congratulations😮;;;wow\nyou get ${current_money}")
    elif luckly == 888:
        current_money = 888888
        st.balloons()
        st.success(f"😮wow;;;😮congratulations😮;;;wow😮\nyou get ${current_money}")
    elif luckly >= 990:
        current_money = random.randint(100000, 150000)
        st.snow()
        st.success(f";;;congratulations;;;\nyou get ${current_money}")
    elif luckly >= 900:
        current_money = random.randint(50000, 80000)
        st.success(f";;;congratulations;;;\nyou get ${current_money}")
    elif luckly >= 800:
        current_money = random.randint(20000, 30000)
        st.success(f";;;congratulations;;;\nyou get ${current_money}")
    elif luckly >= 700:
        current_money = random.randint(10000, 12500)
        st.success(f";;;congratulations;;;\nyou get ${current_money}")
    elif 1 <= luckly <= 10:
        current_money = random.randint(10000, 12500)
        st.success(f";;;congratulations;;;\nyou get ${current_money}")
    else:
        current_money = 0
        st.error("🤣you get notting🤣")
        st.write("🤣lol🤣get the fuck away🤣lol🤣")
        st.write("🤣you fucking noob🤣")
        st.write("🤣lol🤣")
        st.write("🤮ewwwwwwwwwww🤮")
        st.write("🤮ewwwwwwwwwww🤮")
# --- 4. 更新账本数据 ---
    if current_money > 0:
        st.session_state.wins += 1
        st.session_state.profit += current_money
    else:
        st.session_state.losses += 1

# --- 5. 侧边栏重置 ---
if st.sidebar.button('重置所有数据'):
    for key in st.session_state.keys():
        del st.session_state[key]
    st.rerun()
