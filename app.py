import streamlit as st
import pandas as pd
from fortune_tell import fortune_teller
from streamlit_extras.no_default_selectbox import selectbox
import matplotlib.pyplot as plt
import numpy as np


st.set_page_config(page_title='Nepoleon Tells Me')
st.title('Welcome Traveler!')
st.subheader('Welcome to Napoleon Fortune :comet:')

day_selection = {'អាទិត្យ':1,'ចន្ទ':2,'អង្គារ':3,'ពុធ':4,'ព្រហស្បតិ៍':5,'សុក្រ':6,'សៅរ៍':7}
month_selection = {'មិគសិរ':1,'បុស្ស':2,'មាឃ':3,'ផល្គុន':4,'ចេត្រ':5,'ពិសាខ':6,'ជេស្ឋ':7,'អាសាឍ':8,'ស្រាពណ៍':9,'ភទ្របទ':10,'អស្សុជ':11,'កត្តិក':12}
year_selection = {'ជូត':1,'ឆ្លូវ':2,'ខាល':3,'ថោះ':4,'រោង':5,'ម្សាញ់':6,'មមី':7,'មមែ':8,'វក':9,'រកា':10,'ច':11,'កុរ':12}

labels = ["វាសនា", "ទ្រព្យ", "ញាតិ", "មិត្ត", "បរិវារ", "សត្រូវ", "គូរព្រេង", "រោគ", "កិត្តិយស", "ការងារ", "លាភ", "អន្ដរាយ"]
labels_en = ['Destiny', 'Wealth', 'Relatives', 'Friends', 'Entourage', 'Enemies', 'Mate', 'Disease', 'Reputation', 'Career', 'Lucks', 'Disaster']

day = selectbox('DAY: ', day_selection, no_selection_label='--Select Your Day of Birth--')
month = selectbox('MONTH: ', month_selection, no_selection_label='--Select Your Month of Birth--')
year = selectbox('YEAR: ', year_selection, no_selection_label='--Select Your Year of Birth--')
if(day==None or month==None or year==None):
    st.subheader('Ready to tell your Fortune??')
else:
    st.markdown("""---""")
    data, life = fortune_teller(day, month, year)
    teenage = data[0]+data[1]+data[2]+data[3]
    adult = data[4]+data[5]+data[6]+data[7]
    old = data[8]+data[9]+data[10]+data[11]
    string = ''
    for i in data:
        string = string+str(data[i])+'  |  '
    
    st.write(string)
    
    st.markdown("""---""")
    st.write('Your Life Journey')
    col1, col2 = st.columns(2, gap='small')
    with col1:
        st.write('Teenage: ', teenage)
        st.write('Adult: ', adult)
        st.write('Old: ', old)
    with col2:
        line = [teenage, adult, old]
        st.line_chart(line)

    st.markdown("""---""")
    st.write('Your Wheel of Fortune')
    fig1, ax1 = plt.subplots()
    ax1.pie(life, labels=labels_en, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig1)

