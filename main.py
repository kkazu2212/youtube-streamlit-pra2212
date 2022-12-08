import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!'

latest_interation = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_interation.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.05)

'Done!!!!!'

option = st.selectbox(
    '好きな数字は？',
    list(range(1, 11))
)
'好きな数字は、',option, 'です。'

st.write('Interactive Widgets')

text = st.sidebar.text_input('あなたの趣味をおしえてください。')
condition = st.sidebar.slider('調子は？', 0, 100, 50)

'あなたの趣味：',text
'調子：', condition

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')