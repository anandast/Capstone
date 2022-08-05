import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(layout="wide")
st.title('Subsidi BBM Membengkak Imbas Kenaikan Harga Minyak Dunia')
st.markdown('---')
#Read Dataset
brent= pd.read_csv('brent.csv')
crude=pd.read_csv('crude.csv')
subsidi=pd.read_csv('subsidi-bbm.csv',delimiter=';')
harga = pd.read_csv('hargabbm.csv',delimiter=';')
bbm = pd.read_csv('bbm.csv',delimiter=';')
# Data preprocessing
brent['Date'] = pd.to_datetime(brent['Date'])
crude['Date'] = pd.to_datetime(crude['Date'])

cap1,chrt1=st.columns([2,2])
with cap1:
    st.write('Sejak tanggal 10 Juli 2022, PT Pertamina resmi menaikkan harga BBM non subsidi di Indonesia. Berdasarkan visualisasi terlihat bahwa harga Pertamax Turbo yang sebelumnya dijual Rp 14.500-Rp 15.100 per liter naik menjadi Rp 16.200-Rp 16.900 per liter. Kemudian, harga Dexlite dari sebelumnya dijual Rp 12.950-Rp 13.550 per liter naik menjadi Rp 15.000-Rp 15.700 per liter dan harga Pertamax yang sudah naik per 1 April 2022 dari Rp 9.000 menjadi Rp 12.500-Rp 13.000 per liter . Direktur Utama PT Pertamina, Nicke Widyawati mengatakan bahwa\nkenaikan harga BBM tidak lepas dari kenaikan harga minyak mentah dunia sejak Februari 2022 pasca serangan Rusia terhadap Ukraina.')
with chrt1:
    c=alt.Chart(bbm).mark_line().encode(
    x=alt.X('tanggal',axis=alt.Axis(title='Tanggal',labelAngle=0)),
    y=alt.Y('harga',axis=alt.Axis(title='Harga BBM per liter (Rp)')),
    color='jenis'
    ).properties(
        title='Tren Kenaikan Harga BBM Indonesia'
    ).interactive()

    st.altair_chart(
        c,use_container_width=True
    )
st.write('Berdasarkan visualisasi dapat terlihat bahwa harga minyak brent dan WTI menunjukkan tren peningkatan harga pasca serangan Rusia ke Ukraina, harga minyak brent mengalami kenaikan harga dengan puncak harga tertinggi pada tanggal 8 Maret 2022 mencapai 127,98 USD per barrel \ndan harga WTI mencapai 123,7 USD per barel.\nKedua jenis minyak tersebut mengalami kenaikan yang cukup signifikan dibandingkan tahun 2021 dengan rentang harga 60-80 USD per barel.')
chrt2,chrt3= st.columns([2,2])
with chrt2:
    c= alt.Chart(brent).mark_line(color='orange').encode(
        x='Date:T',
        y=alt.Y('Price',axis=alt.Axis(title='Price (USD)')),
        tooltip=['Date','Price','Change %']
    ).properties(
        title='Harga Minyak Brent (USD) '
    ).interactive()

    rule = alt.Chart(pd.DataFrame({
    'Date': ['2022-02-24'],
    'color': ['red']
    })).mark_rule().encode(
    x='Date:T',
    size=alt.value(2),
    color=alt.Color('color:N', scale=None)
    )
    st.altair_chart(
        c+rule,use_container_width=True
    )
    st.caption('Sumber: https://www.investing.com/commodities/brent-oil-historical-data')
with chrt3:
    c= alt.Chart(crude).mark_line(color='orange').encode(
        x='Date:T',
        y=alt.Y('Price',axis=alt.Axis(title='Price (USD)')),
        tooltip=['Date','Price','Change %']
    ).properties(
        title='Harga Minyak WTI'
    ).interactive()

    rule = alt.Chart(pd.DataFrame({
    'Date': ['2022-02-24'],
    'color': ['red']
    })).mark_rule().encode(
    x='Date:T',
    size=alt.value(2),
    color=alt.Color('color:N', scale=None)
    )
    st.altair_chart(
        c+rule,use_container_width=True
    )
    st.caption('Sumber: https://www.investing.com/commodities/crude-oil-historical-data')


cap2,chrt4= st.columns([2,2])
with cap2:
    st.write('Disamping itu, kenaikan harga BBM juga membuat alokasi APBN untuk subsidi BBM di Indonesia naik. Berdasarkan visualisasi menunjukkan adanya tren peningkatan subsidi BBM dari tahun 2019.Sebelumnya dalam UU APBN 2022, subsidi BBM sebesar 77,5 triliun dan kompensasi BBM 18,5 triliun dengan acuan harga ICP Indonesia sebesar 63 USD. Namun setelah adanya kenaikan harga komoditas, pemerintah menetapkan harga ICP sebesar 100 USD per barel, maka pemerintah mengusulkan tambahkan subsidi BBM sebesar Rp 71,8 triliun dan kompensasi BBM Rp 234 triliun sehingga alokasi anggaran subsidi BBM menjadi **Rp 401,8 triliun**.')

with chrt4:
    c= alt.Chart(subsidi).mark_bar().encode(
        x=alt.X('Tahun:O', axis=alt.Axis(labelAngle=0)),
        y=alt.Y('Subsidi BBM:Q',axis=alt.Axis(title='Subsidi BBM (dalam triliun rupiah) ')),
        tooltip=['Subsidi BBM']
    ).properties(
        title='Alokasi Subsidi BBM Indonesia'
    ).interactive()

    st.altair_chart(
        c,use_container_width=True
    )
    st.caption('Sumber:  http://www.data-apbn.kemenkeu.go.id/')

cap3,chrt5= st.columns([2,2])
with cap3:
    st.write('Besarnya alokasi anggaran untuk subsidi BBM dikarenakan selama ini Pertamina menjual BBM dibawah harga keekonomian. Berdasarkan visualisasi dapat terlihat bahwa jenis BBM seperti Pertalite dan Solar dijual jauh dibawah harga keekonomian. Harga keekonomian Pertalite adalah Rp 17.200 per liter sedangkan harga jualnya Rp 7.650 per liter, akibatnya pemerintah harus membayar subsidi sebesar Rp 9.550. Sedangkan untuk Solar, pemerintah harus membayar subsidi sebesar Rp 13.000 per liter karena harga jual hanya Rp 5.150 per liter sedangkan harga keekonomiannya Rp 18.150 per liter. Selain itu, untuk BBM non subsidi seperti Pertamax dan Pertamax turbo, harga jual kedua jenis BBM tersebut masih dibawah harga keekonomian sebenarnya yaitu untuk pertamax Rp 17.950 per liter dan pertamax turbo Rp.20.000 per liter sehingga pemerintah perlu mensubsidi sebesar Rp 5.450 per liter dan Rp 3.800 per liter. Direktur Utama PT Pertamina, Nicke Widyawati mengatakan bahwa harga pertamax berada dikisaran Rp 12.500-Rp 13.000 per liter karena jika harga tersebut dinaikkan,maka akan terjadi shifting ke Pertalite. Tentu saja, kondisi tersebut akan membebani negara.')

with chrt5:
    bar= alt.Chart(harga).mark_bar().encode(
        x=alt.X('jenis', axis=alt.Axis(title='Jenis BBM')),
        y='harga',
        tooltip=['harga']
    ).properties(
        title='Harga BBM di Indonesia',
        width=alt.Step(100)
    ).interactive()

    tick = alt.Chart(harga).mark_tick(color='red',thickness=3,size=100*0.9).encode(
        x=alt.X('jenis',axis=alt.Axis(labelAngle=0,labelAlign='center')),
        y=alt.Y('harga_ekonomi',axis=alt.Axis(title='Harga BBM per liter (Rp)')),
        tooltip=['harga_ekonomi'],
    )
    st.altair_chart(
        bar+tick,use_container_width=True
    )
    st.caption('Sumber:  https://www.kompas.com/')
