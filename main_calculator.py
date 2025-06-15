# import libraries (streamlit & pandas (for dataFrame) )
import streamlit as st
import pandas as pd # for DataFrame

# Step 1 : set page config (layout message)
st.set_page_config(page_title="Intania Department Calculator 2025", layout="wide")
st.title("Intania Department Calculator 🧮")
st.markdown("Welcome to my Intania Department Calculator , This program can help you to calculate possibility to reach your dream department. Hop you enjoy")

# 💡 put selection box outside (Study Group & Dream Department)

# Step 2 : input info
# create selectbox with list of departments (Lists)
dream_department = st.selectbox(
    
    "อยากเป็น #2 อะไรกันน",
        [
            "Computer Engineering (CP) 💻" , "Electrical Engineering (EE) ⚡" , "Industrial Engineering (IE) 🏭" , 
            "Mechanical Engineering (ME) ⚙️" , "Civil Engineering (CE) ⛑️" , "Metallurgical Engineering (MT) 🦾" , 
            "Chemical Engineering (CHE) 🧪" , "Petroleum Engineering (PE) ⚗️" , "Environmental Engineering (ENV) 🌲" , 
            "Survey Engineering (SV) 🔎" , "Automotive Engineering (AE) 🚗"
        ]
)

start_course = st.selectbox("Study Group", ["ENG DRAWING First", "COMP PROG First"])

# create dict for storing key;value of grade
grades = {'A' : 4.00 , 'B+' : 3.50 , 'B' : 3.00 , 'C+' : 2.50 , 'C' : 2.00 , 'D+' : 1.50 , 'D' : 1.00 , 'F' : 0.00 , 'W' : 0.00}

# create form for input grades
with st.form("Intania Department Calculator"):
    
    if start_course == "ENG DRAWING First":
        st.subheader("Semester 1 (ENG DRAWING , GEN CHEM , LAB CHEM)")
        cal1 = st.selectbox("🔢2301107 Calculus I Grade" , list(grades.keys()))
        phy1 = st.selectbox("⚛️2304103 General Physics I Grade" , list(grades.keys()) )
        drawing = st.selectbox("⚙️2103106 Engineering Drawing Grade" , list(grades.keys()) )
        genchem = st.selectbox("🧪2302127 General Chemistry Grade" , list(grades.keys()) )
        labchem = st.selectbox("🧪2302163 General Chemistry Laboratory Grade" , list(grades.keys()) )
        labphy1 = st.selectbox("⚛️2304183 General Physics Laboratory I Grade" , list(grades.keys()) )
        eng1 = st.selectbox("🧑‍🔬5500111 Experimental Engineering I Grade" , list(grades.keys()) )

        st.subheader("Semester 2 (COMP PROG , ENG MATERIALS , EXPLORE ENG WORLD)")
        cal2 = st.selectbox("🔢2301108 Calculus II Grade" , list(grades.keys()))
        phy2 = st.selectbox("⚛️2304104 General Physics II Grade" , list(grades.keys()))
        compprog = st.selectbox("💻2110101 Computer Programming Grade" , list(grades.keys()))
        material = st.selectbox("🧱2109101 Engineering Materials Grade" , list(grades.keys()))
        explore = st.selectbox("🌍2100111 Exploring the Engineering World Grade" , list(grades.keys()))
        labphy2 = st.selectbox("⚛️2304184 General Physics Laboratory II Grade" , list(grades.keys()))
        eng2 = st.selectbox("🧑‍🔬5500112 Experimental Engineering II Grade" , list(grades.keys()))

    else:  # COMP PROG First
        st.subheader("Semester 1 (COMP PROG , ENG MATERIALS , EXPLORE ENG WORLD)")
        cal1 = st.selectbox("🔢2301107 Calculus I Grade" , list(grades.keys()) )
        phy1 = st.selectbox("⚛️2304103 General Physics I Grade" , list(grades.keys()) )
        compprog = st.selectbox("💻2110101 Computer Programming Grade" , list(grades.keys()))
        material = st.selectbox("🧱2109101 Engineering Materials Grade" , list(grades.keys()))
        explore = st.selectbox("🌍2100111 Exploring Engineering World Grade" , list(grades.keys()))
        labphy1 = st.selectbox("⚛️2304183 General Physics Laboratory I Grade" , list(grades.keys()) )
        eng1 = st.selectbox("🧑‍🔬5500111 Experimental Engineering I Grade" , list(grades.keys()) )

        st.subheader("Semester 2 (ENG DRAWING , GEN CHEM , LAB CHEM) ")
        cal2 = st.selectbox("🔢2301108 Calculus II Grade" , list(grades.keys()))
        phy2 = st.selectbox("⚛️2304104 General Physics II Grade" , list(grades.keys()))
        drawing = st.selectbox("⚙️2103106 Engineering Drawing Grade" , list(grades.keys()) )
        genchem = st.selectbox("🧪2302127 General Chemistry Grade" , list(grades.keys()) )
        labchem = st.selectbox("🧪2302163 General Chemistry Laboratory Grade" , list(grades.keys()) )
        labphy2 = st.selectbox("⚛️2304184 General Physics Laboratory II Grade" , list(grades.keys()))
        eng2 = st.selectbox("🧑‍🔬5500112 Experimental Engineering II Grade" , list(grades.keys()))

# create list for storing all of users's grades
your_grade = [compprog , explore , material , drawing , cal1 , cal2 , phy1 , phy2 , genchem , labchem , labphy1 , labphy2 , eng1 , eng2]

# Step 3 : create weights (dict) for each department [key = dep_name , value = weight]
weights = {
            "Computer Engineering (CP) 💻"       : [9 , 3 , 3 , 3 , 3 , 3 , 3 , 3 , 3 , 1 , 1 , 1 , 3 , 3] , 
            "Electrical Engineering (EE) ⚡"     : [3 , 3 , 3 , 3 , 6 , 6 , 3 , 6 , 3 , 1 , 1 , 1 , 3 , 3] , 
            "Industrial Engineering (IE) 🏭"     : [5 , 1 , 4 , 4 , 5 , 5 , 2 , 2 , 2 , 1 , 1 , 1 , 3 , 3] , 
            "Mechanical Engineering (ME) ⚙️"     : [3 , 3 , 3 , 3 , 3 , 3 , 3 , 3 , 3 , 1 , 1 , 1 , 3 , 3] ,
            "Civil Engineering (CE) ⛑️"          : [3 , 3 , 3 , 3 , 3 , 3 , 3 , 3 , 3 , 1 , 1 , 1 , 3 , 3] ,
            "Metallurgical Engineering (MT) 🦾"  : [3 , 3 , 3 , 3 , 3 , 3 , 3 , 3 , 3 , 1 , 1 , 1 , 3 , 3] , 
            "Chemical Engineering (CHE) 🧪"      : [3 , 3 , 3 , 3 , 3 , 3 , 3 , 3 , 3 , 1 , 1 , 1 , 3 , 3] ,
            "Petroleum Engineering (PE) ⚗️"      : [4 , 3 , 3 , 3 , 3 , 3 , 3 , 3 , 3 , 1 , 1 , 1 , 4 , 4] , 
            "Environmental Engineering (ENV) 🌲" : [3 , 3 , 3 , 3 , 3 , 3 , 3 , 3 , 3 , 2 , 2 , 2 , 3 , 3] , 
            "Survey Engineering (SV) 🔎"         : [6 , 3 , 3 , 3 , 6 , 6 , 3 , 3 , 3 , 1 , 1 , 1 , 3 , 3] , 
            "Automotive Engineering (AE) 🚗"     : [3 , 3 , 3 , 3 , 3 , 3 , 3 , 3 , 3 , 1 , 1 , 1 , 3 , 3]
}

# define var.
cp_total = 0 ; ee_total = 0 ; me_total = 0 ; ie_total = 0 ; che_total = 0 ; pe_total = 0 ; 
ae_total = 0 ; sv_total = 0 ; mt_total = 0 ; ce_total = 0 ; env_total = 0

score_each_dep = []

for each_dep in weights : 
    cp_total += weights[]
    







# ประมวลผลหลัง submit
# if submitted:
    #df = pd.DataFrame([{"ประเทศ": country, "ปี": year, "GDP": gdp}])
    #st.write("ข้อมูลที่กรอก:")
    #st.dataframe(df)
    #st.success(f"GDP ของ {country} ในปี {year} คือ {gdp:,}")
