# import libraries (streamlit & pandas (for dataFrame) )
import streamlit as st
import pandas as pd # for DataFrame
import numpy as np # for calculting mathematics function

# Step 1 : set page config (layout message)
st.set_page_config(page_title="Intania Department Calculator 2025", layout="wide")
st.title("Intania Department Calculator 🧮")
st.markdown("Welcome to my Intania Department Calculator , This program can help you to calculate possibility to reach your dream department. Hop you enjoy")

st.image("/workspaces/Intania_Department_Calculator/Multiplier Intania Department.jpg" , caption = "Gei")

# 💡 put selection box outside (Study Group & Dream Department)

# Step 2 : input basic info
# 2.1 create selectbox with list of departments (Lists)
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

# 2.2 create dict for storing key;value of grade
grades = {'A' : 4.00 , 'B+' : 3.50 , 'B' : 3.00 , 'C+' : 2.50 , 'C' : 2.00 , 'D+' : 1.50 , 'D' : 1.00 , 'F' : 0.00 , 'W' : 0.00}

# 2.3 create form for input grades -> don't forget st.form_submit_button (must)
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

    # 2.4 create submit button for calculating points
    submitted = st.form_submit_button("Submit")


# 2.5 create list for storing all of users's grades
your_grade_letter = [compprog , explore , material , drawing , cal1 , cal2 , phy1 , phy2 , genchem , labchem , labphy1 , labphy2 , eng1 , eng2]

your_grade_value = [grades[compprog] , grades[explore] , grades[material], grades[drawing] , grades[cal1] , grades[cal2] ,
                    grades[phy1] , grades[phy2] , grades[genchem] , grades[labchem] , grades[labphy1] , grades[labphy2] , grades[eng1] , grades[eng2] ]


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

# Step 4 : calculate score for each department
score_each_dept = {} # dict ( for key (dept_name) :value (score) )

# outer loop : extract key (each_dept) and value (weight_list) from weights dict
for (each_dept , weight_list) in weights.items() : 
    # create sum_score var. (reset for each dept)
    sum_score = 0
    # inner loop : calculate score for each department
    for pos in range(len(weight_list)):

        # Note : we can use (pos , weight_each_subj) in enumerate(weight_list) to get index and weight (similar to zip() but not all)

        # calculate score for each subject
        sum_score += your_grade_value[pos] * weight_list[pos]
            # enumerate form : sum_score += your_grade_value[pos] * weight_each_subj

    # store the score in score_each_dep dict
    score_each_dept[each_dept] = sum_score

# Step 5 : Calculate possibilities for each department
    # Logic : based on 6-year data backward , we'll calculate 2 ways
        # 1st way : calculate by average of min_score
        # 2nd way : calculate by weighted min_score (more accurate)

    # 5.1 : create dict for storing minscore of each department
    minscore_dept = {
        "Computer Engineering (CP) 💻"           : [125 , 136 , 140 , 141.5 , 153 , 115] , 
            "Electrical Engineering (EE) ⚡"     : [107 , 118.5 , 121 , 110 , 124 , 87.5] , 
            "Industrial Engineering (IE) 🏭"     : [98 , 107 , 115.5 ,112 , 116.5 , 98.5] , 
            "Mechanical Engineering (ME) ⚙️"     : [100 , 99 , 102.5 , 88 , 93.5 , 79.5] ,
            "Civil Engineering (CE) ⛑️"          : [78.5 , 87.5 , 90 , 74.5 , 76 , 7.5] ,
            "Metallurgical Engineering (MT) 🦾"  : [35 , 58.5 , 35 , 64 , 49.5 , 39] , 
            "Chemical Engineering (CHE) 🧪"      : [77.5 , 63 , 41.5 , 34 , 66.5 , 57.5] ,
            "Petroleum Engineering (PE) ⚗️"      : [94.5 , 90 , 87.5 , 74 , 97.5, 74.5] , 
            "Environmental Engineering (ENV) 🌲" : [82 , 76.5 , 90 , 80.5 , 81.5 , 77.5] , 
            "Survey Engineering (SV) 🔎"         : [69 , 66.5 , 84.5 , 101 , 35.5 , 55.5] , 
            "Automotive Engineering (AE) 🚗"     : [76.5 , 88 , 87.5 , 71.5 , 76 , 70.5]
    }

# 5.3 : create dict for storing weighted minscore of each department
weighted_minscore = {
        "Computer Engineering (CP) 💻"       : (0.16 * 125  + 0.16 * 136   + 0.16 * 140   + 0.16 * 141.5 + 0.16 * 153   + 0.2 * 115) , 
        "Electrical Engineering (EE) ⚡"     : (0.16 * 107  + 0.16 * 118.5 + 0.16 * 121   + 0.16 * 110   + 0.16 * 124   + 0.2 * 87.5) , 
        "Industrial Engineering (IE) 🏭"     : (0.16 * 98   + 0.16 * 107   + 0.16 * 115.5 + 0.16 * 112   + 0.16 * 116.5 + 0.2 * 98.5) , 
        "Mechanical Engineering (ME) ⚙️"     : (0.16 * 100  + 0.16 * 99    + 0.16 * 102.5 + 0.16 * 88    + 0.16 * 93.5  + 0.2 * 79.5) ,
        "Civil Engineering (CE) ⛑️"          : (0.19 * 78.5 + 0.19 * 87.5  + 0.19 * 90    + 0.19 * 74.5  + 0.19 * 76    + 0.05 * 7.5) ,
        "Metallurgical Engineering (MT) 🦾"  : (0.16 * 35   + 0.16 * 58.5  + 0.16 * 35    + 0.16 * 64    + 0.16 * 49.5  + 0.2 * 39) , 
        "Chemical Engineering (CHE) 🧪"      : (0.16 * 77.5 + 0.16 * 63    + 0.16 * 41.5  + 0.16 * 34    + 0.16 * 66.5  + 0.2 * 57.5) ,
        "Petroleum Engineering (PE) ⚗️"      : (0.16 * 94.5 + 0.16 * 90    + 0.16 * 87.5  + 0.16 * 74    + 0.16 * 97.5  + 0.2 * 74.5) , 
        "Environmental Engineering (ENV) 🌲" : (0.16 * 82   + 0.16 * 76.5  + 0.16 * 90    + 0.16 * 80.5  + 0.16 * 81.5  + 0.2 * 77.5) , 
        "Survey Engineering (SV) 🔎"         : (0.16 * 69   + 0.16 * 66.5  + 0.16 * 84.5  + 0.16 * 101   + 0.16 * 35.5  + 0.2 * 55.5) , 
        "Automotive Engineering (AE) 🚗"     : (0.16 * 76.5 + 0.16 * 88    + 0.16 * 87.5  + 0.16 * 71.5  + 0.16 * 76    + 0.2 * 70.5)
    }

# Step 6 : calculate possibility for each department (2 ways) 
average_min_possibility = {
        "Computer Engineering (CP) 💻"       : (0.16 * 125  + 0.16 * 136   + 0.16 * 140   + 0.16 * 141.5 + 0.16 * 153   + 0.2 * 115) , 
        "Electrical Engineering (EE) ⚡"     : (0.16 * 107  + 0.16 * 118.5 + 0.16 * 121   + 0.16 * 110   + 0.16 * 124   + 0.2 * 87.5) , 
        "Industrial Engineering (IE) 🏭"     : (0.16 * 98   + 0.16 * 107   + 0.16 * 115.5 + 0.16 * 112   + 0.16 * 116.5 + 0.2 * 98.5) , 
        "Mechanical Engineering (ME) ⚙️"     : (0.16 * 100  + 0.16 * 99    + 0.16 * 102.5 + 0.16 * 88    + 0.16 * 93.5  + 0.2 * 79.5) ,
        "Civil Engineering (CE) ⛑️"          : (0.19 * 78.5 + 0.19 * 87.5  + 0.19 * 90    + 0.19 * 74.5  + 0.19 * 76    + 0.05 * 7.5) ,
        "Metallurgical Engineering (MT) 🦾"  : (0.16 * 35   + 0.16 * 58.5  + 0.16 * 35    + 0.16 * 64    + 0.16 * 49.5  + 0.2 * 39) , 
        "Chemical Engineering (CHE) 🧪"      : (0.16 * 77.5 + 0.16 * 63    + 0.16 * 41.5  + 0.16 * 34    + 0.16 * 66.5  + 0.2 * 57.5) ,
        "Petroleum Engineering (PE) ⚗️"      : (0.16 * 94.5 + 0.16 * 90    + 0.16 * 87.5  + 0.16 * 74    + 0.16 * 97.5  + 0.2 * 74.5) , 
        "Environmental Engineering (ENV) 🌲" : (0.16 * 82   + 0.16 * 76.5  + 0.16 * 90    + 0.16 * 80.5  + 0.16 * 81.5  + 0.2 * 77.5) , 
        "Survey Engineering (SV) 🔎"         : (0.16 * 69   + 0.16 * 66.5  + 0.16 * 84.5  + 0.16 * 101   + 0.16 * 35.5  + 0.2 * 55.5) , 
        "Automotive Engineering (AE) 🚗" 
}


# ประมวลผลหลัง submit
if submitted:












    st.subheader("📊 คะแนนรวมของแต่ละภาค:")
    for dep, score in score_each_dep.items():
        st.write(f"**{dep}** : {score:.2f} คะแนน")
    
    # เพิ่มการเน้นภาคที่ฝันไว้
    if dream_department in score_each_dep:
        dream_score = score_each_dep[dream_department]
        st.markdown(f"🎯 คะแนนของภาคในฝัน ({dream_department}) ของคุณคือ: **{dream_score:.2f}**")

        if dream_score >= 50:
            st.success("โอกาสสูงมาก! ✅")
        elif dream_score >= 40:
            st.warning("โอกาสกลาง ๆ พอลุ้นได้ 🟡")
        else:
            st.error("ต้องพยายามเพิ่มอีกหน่อย ❌")

