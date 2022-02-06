# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 17:12:30 2021

@author: aika takeda
"""

import streamlit as st
st.title("情報基礎実習のまとめ")
st.write("後期情報基礎実習の復習に役立ててください")
a=st.selectbox("どの分野の学習をしますか？",list(["双方向性とは","Slackチャットボット","Streamlit","ラズベリーパイ"]))
if a=="双方向性とは":
    st.write("第１回授業スライドです。")
    st.write('こちらをクリックしてください','https://drive.google.com/file/d/1hMeNvTIx7rCEjTLikPn7allHshBjH4G3/view')
elif a == 'Slackチャットボット' :
    st.write("第２回授業スライドです。")
    st.write('こちらをクリックしてください','https://drive.google.com/file/d/1lGecOmK7cXdv-iyRMM0izofS2QPjsQfO/view')
elif a == 'Streamlit' :
    b=st.selectbox("どの分野の学習をしますか？",list(["pandas スクレイピング","streamlitの基礎","GitHub関連","みんなの作品"]))
    if ｂ=="pandas スクレイピング":
         st.write("第3回授業スライドです。")
         st.write('こちらをクリックしてください','https://drive.google.com/file/d/151nZbpNDgld9uqMmxUlWOTb_q7vizdYr/view')
         st.write("第４回授業スライドです。")
         st.write('こちらをクリックしてください','https://drive.google.com/file/d/1LnJDU-nzvuls-Q9eBPXj92ixr-uppmgB/view')
    elif b == 'streamlitの基礎' :
        st.write("第5回授業スライドです。")
        st.write('こちらをクリックしてください','https://drive.google.com/file/d/10XowFK7TZO9b7WvA7kQJz55kJACXzfDC/view')
    elif b == 'GitHub関連' :
        st.write("第６回授業スライドです。")
        st.write('こちらをクリックしてください','https://drive.google.com/file/d/15oaTA3yyNeX_PHSxvyGleuROZZOdjOgE/view')
    elif b == 'みんなの作品' :
        st.write("２年生")
        st.write('こちらをクリックしてください','https://docs.google.com/presentation/d/14pOcIWo8acV98tH7ly-ks1u0PoNZQlEOwBziZWo0kZ8/edit#slide=id.p')
        st.write("３年生")
        st.write('こちらをクリックしてください','https://docs.google.com/presentation/d/1KxEI9bq5uylxmC4XOvQ4w_pFR0wVv2_TMMtekWUxXlQ/edit#slide=id.p') 
elif a == 'ラズベリーパイ' :
    c=st.selectbox("どの分野の学習をしますか？",list(["人工知能の仕組み","ラズベリーパイの基礎","みんなの作品"]))
    if c=="人工知能の仕組み":
         st.write("第9回授業スライドです。")
         st.write('こちらをクリックしてください','https://drive.google.com/file/d/13P0sSC9K06fIMduj1uT-YX8W7r11R0AQ/view')
    elif c == 'ラズベリーパイの基礎' :
        st.write("第10回授業スライドです。")
        st.write('こちらをクリックしてください','https://drive.google.com/file/u/0/d/1abTunFS_jnoF5_eM3CbbD1IKViZWcAfP/view?usp=drive_web')
        st.write("第11回授業スライドです。")
        st.write('こちらをクリックしてください','https://drive.google.com/file/d/1MGClHGWAeUrL-7aL9nJl41Iac0MAncPd/view')
        st.write("第12回授業スライドです。")
        st.write('こちらをクリックしてください','https://drive.google.com/file/d/1bPkYC9No1gtcC4BKRNJAEyn7XTaYb85P/view')
    elif c == 'みんなの作品' :
        st.write("２年生")
        st.write('こちらをクリックしてください','https://docs.google.com/presentation/d/13UZBAlfnP7k53iPD5AAncxY_nYJwp4ngxuvi-gSz80M/edit')
        
                                         

 


    