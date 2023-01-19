import streamlit as st
import pandas as pd
from fortune_tell import fortune_teller

st.title('Welcome Traveler')

day_selection = {'អាទិត្យ':1,'ចន្ទ':2,'អង្គារ':3,'ពុធ':4,'ព្រហស្បតិ៍':5,'សុក្រ':6,'សៅរ៍':7}
month_selection = {'មិគសិរ':1,'បុស្ស':2,'មាឃ':3,'ផល្គុន':4,'ចេត្រ':5,'ពិសាខ':6,'ជេស្ឋ':7,'អាសាឍ':8,'ស្រាពណ៍':9,'ភទ្របទ':10,'អស្សុជ':11,'កត្តិក':12}
year_selection = {'ជូត':1,'ឆ្លូវ':2,'ខាល':3,'ថោះ':4,'រោង':5,'ម្សាញ់':6,'មមី':7,'មមែ':8,'វក':9,'រកា':10,'ច':11,'កុរ':12}


day = st.selectbox('Select your day of birth: ', day_selection)
month = st.selectbox('Select your month of birth: ', month_selection)
year = st.selectbox('Select your year of birth: ', year_selection)

data = fortune_teller(day, month, year)
teenage = data[0]+data[1]+data[2]+data[3]
adult = data[4]+data[5]+data[6]+data[7]
old = data[8]+data[9]+data[10]+data[11]

for i in data:
    st.write(i)

# line = [teenage, adult, old]
# line2 = []
# st.line_chart(line)
# st.write('Teenage: ', teenage)
# st.write('Adult: ', adult)
# st.write('Old: ', old)

