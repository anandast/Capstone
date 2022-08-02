import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(layout="wide")
st.title('Dampak Kenaikan Harga Minyak Dunia Terhadap Subsidi BBM di Indonesia')
st.markdown('---')
#Read Dataset
brent= pd.read_csv('brent.csv')
crude=pd.read_csv('crude.csv')
subsidi=pd.read_csv('subsidi-bbm.csv',delimiter=';')
# Data preprocessing
brent['Date'] = pd.to_datetime(brent['Date'])
crude['Date'] = pd.to_datetime(crude['Date'])

st.write('Sejak tanggal 10 Juli 2022, PT Pertamina resmi menaikkan harga BBM di Indonesia. Direktur Utama PT Pertamina, Nicke Widyawati mengatakan bahwa\nkenaikan harga BBM tidak lepas dari kenaikan harga minyak mentah dunia sejak Februari 2022 pasca serangan Rusia terhadap Ukraina.')

chrt1,chrt2= st.columns([2,2])
with chrt1:
    c= alt.Chart(brent).mark_line(color='orange').encode(
        x='Date:T',
        y=alt.Y('Price'),
        tooltip=['Date','Price','Change %']
    ).properties(
        title='Harga Minyak Brent (USD) '
    ).interactive()
   
    st.altair_chart(
        c,use_container_width=True
    )
    st.caption('Sumber: https://www.investing.com/commodities/brent-oil-historical-data')
with chrt2:
    c= alt.Chart(crude).mark_line(color='orange').encode(
        x='Date:T',
        y=alt.Y('Price'),
        tooltip=['Date','Price','Change %']
    ).properties(
        title='Harga Minyak WTI (USD) '
    ).interactive()

    st.altair_chart(
        c,use_container_width=True
    )
    st.caption('Sumber: https://www.investing.com/commodities/crude-oil-historical-data')

st.write('Berdasarkan visualisasi diatas terlihat bahwa harga minyak brent dan WTI menunjukkan tren peningkatan harga pasca serangan Rusia ke Ukraina, harga minyak brent mengalami kenaikan harga dengan puncak harga tertinggi pada tanggal 8 Maret 2022 mencapai 127,08 USD per barrel \ndan harga WTI mencapai 123,7 USD per barel.\nKedua jenis minyak tersebut mengalami kenaikan yang cukup signifikan dibandingkan tahun 2021 dengan rentang harga 60-80 USD per barel.')

cap1,chrt3= st.columns([2,2])
with cap1:
    st.write('Disamping itu, kenaikan harga BBM juga membuat alokasi APBN untuk subsidi BBM di Indonesia naik. Visualisasi disamping menunjukkan adanya tren peningkatan subsidi BBM dari tahun 2019.Sebelumnya dalam UU APBN 2022, subsidi BBM sebesar 77,5 triliun dengan acuan harga ICP Indonesia sebesar 63 USD. Namun setelah adanya kenaikan harga, pemerintah menetapkan harga ICP sebesar 100 USD per barel, maka pemerintah mengusulkan tambahkan subsidi BBM sebesar Rp 71,8 triliun sehingga alokasi subsidi BBM menjadi **Rp 149,4 triliun**.')

with chrt3:
    c= alt.Chart(subsidi).mark_bar().encode(
        x='Tahun:O',
        y='Subsidi BBM:Q',
        tooltip=['Subsidi BBM']
    ).properties(
        title='Alokasi Subsidi BBM Indonesia (dalam triliun rupiah)'
    ).interactive()

    st.altair_chart(
        c,use_container_width=True
    )
    st.caption('Sumber:  http://www.data-apbn.kemenkeu.go.id/')
