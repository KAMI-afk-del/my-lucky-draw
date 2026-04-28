import streamlit as st
import random

st.set_page_config(page_title="幸运大抽奖", page_icon="🎰")

st.title("🎰 幸运大抽奖")
st.write("看看你今天的运气如何？点击按钮开始抽奖")

if st.button('🖕点击开始抽奖🖕'):
    luckly = random.randint(0, 1000)

    st.subheader(f"current luckly: {luckly}")

    if luckly == 91:
        st.success("wow*congratulations*wow")
        st.write("you get $91919")
        
    elif luckly == 78:
        st.success("wow*congratulations*wow")
        st.write("you get $78787")
        
    elif luckly == 13:
        st.success("wow*congratulations*wow")
        st.write("you get $13131")
        
    elif luckly == 714:
        st.warning("懂你意思")
        st.write("you get $71400")
        st.text("kskbl?🤨")
        st.text("zdjd🧐")
        st.text("wkzkbl😮")
        st.text("wzbyqs😤")
        st.text("nzzyswwzbsbll🥵")
        
    elif luckly == 999:
        st.balloons
        st.success("wow;;;😮congratulations😮;;;wow")
        st.write("you get $488888")
        
    elif luckly == 888:
        st.balloons()
        st.success("😮wow;;;😮congratulations😮;;;wow😮")
        st.write("you get $888888")
        st.write("😮😮😮😮😮😮😮😮😮😮")
        
    elif luckly >= 990:
        st.snow
        st.success(";;;congratulations;;;")
        money = random.randint(100000, 150000)
        st.write(f"currnet money:you get ${money}")
        
    elif luckly >= 900:
        st.success(";;;congratulations;;;")
        money = random.randint(50000, 80000)
        st.write(f"currnet money:you get ${money}")
        
    elif luckly >= 800:
        st.success(";;;congratulations;;;")
        money = random.randint(20000, 30000)
        st.write(f"currnet money:you get ${money}")
        
    elif luckly >= 700:
        st.success(";;;congratulations;;;")
        money = random.randint(10000, 12500)
        st.write(f"currnet money:you get ${money}")
        
    elif 1 <= luckly <= 10:
        st.success(";;;congratulations;;;")
        money = random.randint(10000, 12500)
        st.write(f"currnet money:you get ${money}")
        
    else:
        st.snow
        st.error("    🤣you get notting🤣")
        st.write("🤣lol🤣get the fuck away🤣lol🤣")
        st.write("      🤣you fucking noob🤣")
        st.write("          🤣lol🤣")
        st.write("     🤮ewwwwwwwwwww🤮")
        st.write("     🤮ewwwwwwwwwww🤮")
