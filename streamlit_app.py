import streamlit as st
import random
from datetime import datetime

if 'total' not in st.session_state:
    st.session_state.total = 0
if 'wins' not in st.session_state:
    st.session_state.wins = 0
if 'losses' not in st.session_state:
    st.session_state.losses = 0
if 'profit' not in st.session_state:
    st.session_state.profit = 150000 
if 'history' not in st.session_state:
    st.session_state.history = []

st.set_page_config(page_title="超级抽奖机 Pro", page_icon="🎰")
st.title("🎰❗不要赌博❗小心等下4.7k❗❗❗")

with st.sidebar:
    st.header("游戏选项")
    if st.button("懦夫津贴 (+500)"):
        st.session_state.profit += 500
        st.rerun()
    st.divider()
    if st.button('清空数据重新开始'):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.rerun()

COST_PER_DRAW = 10000
col1, col2, col3, col4 = st.columns(4)
col1.metric("总抽奖次数", st.session_state.total)
col2.metric("中奖次数", st.session_state.wins)
col3.metric("空奖次数", st.session_state.losses)
col4.metric("当前资产", f"${st.session_state.profit}", delta=f"{st.session_state.profit - 150000}")

st.write(f"one time = $10000 **${COST_PER_DRAW}**")
    

if luckly == 91:
        current_money = 91919
        st.success(f"wow*congratulations*wow\nyou get ${current_money}")
elif luckly == 908:
        current_money = 1
        st.("神的诞生日")
        st.("😋😋奖励你一块钱😋😋")
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
        st.text("☝️🤓👇康神开播啦？真的假的？🤨🤨我靠真开播了😮😮我没胖！我真比以前瘦了昂😠😠你们再这样说我我真的受不了了🥵🥵")
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

record = f"{datetime.now(0).strftime('%H:%M:%S')} - 号码 {luckly}: 中奖 ${current_prize} ({result_msg})"
         st.session_state.history.insert(0, record)
else:
    st.session_state.losses += 1
if current_money > 0:
        st.session_state.wins += 1
        st.session_state.profit += current_money


if st.sidebar.button('重置所有数据'):
   for key in st.session_state.keys():
        del st.session_state[key]
    st.rerun()
        st.divider()
st.subheader(" 中奖记录")
if st.session_state.history:
for item in st.session_state.history[:20]
        st.write(item)
else:
    st.info("notting here")
