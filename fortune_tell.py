day_selection = {'អាទិត្យ':1,'ចន្ទ':2,'អង្គារ':3,'ពុធ':4,'ព្រហស្បតិ៍':5,'សុក្រ':6,'សៅរ៍':7}
month_selection = {'មិគសិរ':1,'បុស្ស':2,'មាឃ':3,'ផល្គុន':4,'ចេត្រ':5,'ពិសាខ':6,'ជេស្ឋ':7,'អាសាឍ':8,'ស្រាពណ៍':9,'ភទ្របទ':10,'អស្សុជ':11,'កត្តិក':12}
year_selection = {'ជូត':1,'ឆ្លូវ':2,'ខាល':3,'ថោះ':4,'រោង':5,'ម្សាញ់':6,'មមី':7,'មមែ':8,'វក':9,'រកា':10,'ច':11,'កុរ':12}

life = ["វាសនា", "ទ្រព្យ", "ញាតិ", "មិត្ត", "បរិវារ", "សត្រូវ", "គូរព្រេង", "រោគ", "កិត្តិយស", "ការងារ", "លាភ", "អន្ដរាយ"]

def fortune_teller(selected_day, selected_month, selected_year):

    cal_day = []
    cal_month = []
    cal_year = []

    result = []

    ## Days
    day_temp = day_selection[selected_day]
    for i in day_selection:
        if day_temp <= 7:
            day = day_temp
            cal_day.append(day)
            day_temp+=1
        elif day_temp > 7:
            day = day_temp
            cal_day.append(day-7)
            day_temp+=1
    cal_day.extend([0,0,0,0,0])

     ## Months
    month_temp = month_selection[selected_month]
    for i in month_selection:
        if month_temp <= 12:
            month = month_temp
            cal_month.append(month)
            month_temp+=1
        elif month_temp > 12:
            month = month_temp
            cal_month.append(month-12)
            month_temp+=1

    ## Years
    year_temp = year_selection[selected_year]
    for i in year_selection:
        if year_temp <= 12:
            year = year_temp
            cal_year.append(year)
            year_temp+=1
        elif year_temp > 12:
            year = year_temp
            cal_year.append(year-12)
            year_temp+=1

    for day, month, year in zip(cal_day, cal_month, cal_year):
        summed_value = day+month+year
        if(summed_value<36 and summed_value>=24):
            summed_value-=24
        elif(summed_value<24 and summed_value>=12):
            summed_value-=12
        result.append(summed_value)

    fortune = []
    for item in result:
        fortune.append(round((item/11)*100,2))

    return(result)