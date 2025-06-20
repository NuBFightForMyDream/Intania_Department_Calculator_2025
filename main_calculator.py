# import libraries (streamlit & pandas (for dataFrame) ) 
import streamlit as st 
import pandas as pd # for DataFrame 
import numpy as np # for calculting mathematics function 

# Step 1 : set page config (layout message) 
st.set_page_config(page_title="Intania Department Calculator 2025", layout="wide") 
st.title("Intania Department Calculator 🧮") 

# markdown for welcome message 
st.subheader("Welcome to my Intania Department Calculator , This program can help you to calculate possibility to reach your dream department.")
st.markdown("Note : If you want easier version to understand (Google Sheets) , Click here [Via this link , Don't use it for commercials](https://docs.google.com/spreadsheets/d/1vxl09wGhZNzD7PMFiAnqD_VPttb0QYFxf6-nfpaY2iY/edit?gid=1499624161#gid=1499624161) ")
st.markdown("Ps. More details about this program , You can read it at [README.md](https://github.com/NuBFightForCP51Again/Intania_Department_Calculator/blob/main/README.md) file in this repository.")

# insert multipler image 
st.markdown("Well , Here is a multiplier for each department [Click Here](https://github.com/NuBFightForCP51Again/Intania_Department_Calculator/blob/main/Multiplier%20Intania%20Department.jpg)") 

# Step 2 : input basic info 

# 2.1 create selectbox with list of departments (Lists) 
dream_department = st.selectbox( "อยากเป็น #2 อะไรกันน", 
                                [ "Computer Engineering (CP) 💻" , "Electrical Engineering (EE) ⚡" , "Industrial Engineering (IE) 🏭" , 
                                 "Mechanical Engineering (ME) ⚙️" , "Civil Engineering (CE) ⛑️" , "Metallurgical Engineering (MT) 🦾" , 
                                 "Chemical Engineering (CHE) 🧪" , "Petroleum Engineering (PE) ⚗️" , "Environmental Engineering (ENV) 🌲" ,
                                "Survey Engineering (SV) 🔎" , "Automotive Engineering (AE) 🚗" ] )

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
    submitted = st.form_submit_button("Calculate Possibility! 🎯") 
        
# 2.5 create list for storing all of users's grades 
your_grade_letter = [compprog , explore , material , drawing , cal1 , cal2 , phy1 , phy2 , genchem , labchem , labphy1 , labphy2 , eng1 , eng2] 
your_grade_value = [grades[compprog] , grades[explore] , grades[material], grades[drawing] , grades[cal1] , grades[cal2] , grades[phy1] , grades[phy2] , 
                            grades[genchem] , grades[labchem] , grades[labphy1] , grades[labphy2] , grades[eng1] , grades[eng2] ] 
                            
# Step 3 : create weights (dict) for each department [key = dep_name , value = weight] 
weights = { "Computer Engineering (CP) 💻"        : [9 , 3 , 3 , 3 , 3 , 3 , 3 , 3 , 3 , 1 , 1 , 1 , 3 , 3] , 
           "Electrical Engineering (EE) ⚡"       : [3 , 3 , 3 , 3 , 6 , 6 , 3 , 6 , 3 , 1 , 1 , 1 , 3 , 3] ,
             "Industrial Engineering (IE) 🏭"     : [5 , 1 , 4 , 4 , 5 , 5 , 2 , 2 , 2 , 1 , 1 , 1 , 3 , 3] , 
             "Mechanical Engineering (ME) ⚙️"     : [3 , 3 , 3 , 3 , 3 , 3 , 3 , 3 , 3 , 1 , 1 , 1 , 3 , 3] , 
             "Civil Engineering (CE) ⛑️"          : [3 , 3 , 3 , 3 , 3 , 3 , 3 , 3 , 3 , 1 , 1 , 1 , 3 , 3] , 
             "Metallurgical Engineering (MT) 🦾"  : [3 , 3 , 3 , 3 , 3 , 3 , 3 , 3 , 3 , 1 , 1 , 1 , 3 , 3] , 
             "Chemical Engineering (CHE) 🧪"      : [3 , 3 , 3 , 3 , 3 , 3 , 3 , 3 , 3 , 1 , 1 , 1 , 3 , 3] , 
             "Petroleum Engineering (PE) ⚗️"      : [4 , 3 , 3 , 3 , 3 , 3 , 3 , 3 , 3 , 1 , 1 , 1 , 4 , 4] , 
             "Environmental Engineering (ENV) 🌲" : [3 , 3 , 3 , 3 , 3 , 3 , 3 , 3 , 3 , 2 , 2 , 2 , 3 , 3] , 
             "Survey Engineering (SV) 🔎"         : [6 , 3 , 3 , 3 , 6 , 6 , 3 , 3 , 3 , 1 , 1 , 1 , 3 , 3] , 
             "Automotive Engineering (AE) 🚗"     : [3 , 3 , 3 , 3 , 3 , 3 , 3 , 3 , 3 , 1 , 1 , 1 , 3 , 3] } 

# Step 4 : calculate score for each department 
yourscore_dict = {} # dict ( for key (dept_name) :value (score) ) 
# outer loop : extract key (each_dept) and value (weight_list) from weights dict 

for (each_dept , weight_list) in weights.items() : # create sum_score var. (reset for each dept) 
    sum_score = 0 
    # inner loop : calculate score for each department 
    for pos in range(len(weight_list)): # Note : we can use (pos , weight_each_subj) in enumerate(weight_list) to get index and weight (similar to zip() but not all)
        # calculate score for each subject 
        sum_score += your_grade_value[pos] * weight_list[pos] 
        # enumerate form : sum_score += your_grade_value[pos] * weight_each_subj 
        
    # store the score in score_each_dep dict 
    yourscore_dict[each_dept] = sum_score 
    
# Step 5 : Calculate possibilities for each department # Logic : based on 6-year data backward , we'll calculate 2 ways \
    # 1st way : calculate by average of min_score 
    # 2nd way : calculate by weighted min_score (more accurate) 
    
# 5.1 : create dict for storing minscore of each department 
minscore_dict = {    "Computer Engineering (CP) 💻"       : [125 , 136 , 140 , 141.5 , 153 , 115] , 
                     "Electrical Engineering (EE) ⚡"     : [107 , 118.5 , 121 , 110 , 124 , 87.5] , 
                     "Industrial Engineering (IE) 🏭"     : [98 , 107 , 115.5 ,112 , 116.5 , 98.5] , 
                     "Mechanical Engineering (ME) ⚙️"     : [100 , 99 , 102.5 , 88 , 93.5 , 79.5] , 
                     "Civil Engineering (CE) ⛑️"          : [78.5 , 87.5 , 90 , 74.5 , 76 , 7.5] , 
                     "Metallurgical Engineering (MT) 🦾"  : [35 , 58.5 , 35 , 64 , 49.5 , 39] , 
                     "Chemical Engineering (CHE) 🧪"      : [77.5 , 63 , 41.5 , 34 , 66.5 , 57.5] , 
                     "Petroleum Engineering (PE) ⚗️"      : [94.5 , 90 , 87.5 , 74 , 97.5, 74.5] , 
                     "Environmental Engineering (ENV) 🌲" : [82 , 76.5 , 90 , 80.5 , 81.5 , 77.5] , 
                     "Survey Engineering (SV) 🔎"         : [69 , 66.5 , 84.5 , 101 , 35.5 , 55.5] , 
                     "Automotive Engineering (AE) 🚗"     : [76.5 , 88 , 87.5 , 71.5 , 76 , 70.5] } 
                     
# 5.2 : calculate average minscore for each department 
avg_minscore_dict = { dept : np.mean(minscore_list) for dept , minscore_list in minscore_dict.items() } 

# 5.3 : create dict for storing weighted minscore of each department 
weighted_minscore_dict = { "Computer Engineering (CP) 💻"       : (0.08 * 125  + 0.125 * 136   + 0.15 * 140     + 0.15 * 141.5  + 0.37 * 153    + 0.125 * 115) , 
                           "Electrical Engineering (EE) ⚡"     : (0.14 * 107  + 0.14 * 118.5  + 0.14 * 121     + 0.14 * 110    + 0.22 * 124    + 0.22 * (87.5 + 0.2*(180-87.5)) ) , 
                           "Industrial Engineering (IE) 🏭"     : (0.08 * 98   + 0.12 * 107    + 0.216 * 115.5  + 0.216 * 112   + 0.216 * 116.5 + 0.15 * 98.5) , 
                           "Mechanical Engineering (ME) ⚙️"     : (0.15 * 100  + 0.15 * 99     + 0.2 * 102.5    + 0.15 * 88     + 0.15 * 93.5   + 0.2 * 79.5) , 
                           "Civil Engineering (CE) ⛑️"          : (0.19 * 78.5 + 0.19 * 87.5   + 0.19 * 90      + 0.19 * 74.5   + 0.19 * 76     + 0.05 * 7.5) , 
                           "Metallurgical Engineering (MT) 🦾"  : (0.3 * 35    + 0.033 * 58.5  + 0.3 * 35       + 0.033 * 64    + 0.033 * 49.5  + 0.3 * 39) , 
                           "Chemical Engineering (CHE) 🧪"      : (0.2 * 77.5  + 0.16 * 63     + 0.16 * 41.5    + 0.16 * 34     + 0.16 * 66.5   + 0.16 * 57.5) , 
                           "Petroleum Engineering (PE) ⚗️"      : (0.16 * 94.5 + 0.16 * 90     + 0.16 * 87.5    + 0.16 * 74     + 0.2 * 97.5    + 0.16 * 74.5) , 
                           "Environmental Engineering (ENV) 🌲" : (0.16 * 82   + 0.16 * 76.5   + 0.2 * 90       + 0.16 * 80.5   + 0.16 * 81.5   + 0.16 * 77.5) , 
                           "Survey Engineering (SV) 🔎"         : (0.16 * 69   + 0.16 * 66.5   + 0.16 * 84.5    + 0.2 * 101     + 0.16 * 35.5   + 0.16 * 55.5) , 
                           "Automotive Engineering (AE) 🚗"     : (0.15 * 76.5 + 0.2 * 88      + 0.2 * 87.5     + 0.15 * 71.5   + 0.15 * 76     + 0.15 * 70.5) } 
                           
# Step 6 : calculate possibility for each department (2 ways) 
# Formula : possibility = 100 + ( (got - avg) / avg * 400 ) when ( (got - avg)/avg is difference) 
average_min_possibility = { dept : (100 +  ( (yourscore_dict[dept] - avg_minscore_dict[dept]) / avg_minscore_dict[dept] * 400 )  ) for dept in yourscore_dict } 
weighted_min_possibility = { dept : ( 100 +  ( (yourscore_dict[dept] - weighted_minscore_dict[dept]) / weighted_minscore_dict[dept] * 400 )  ) for dept in yourscore_dict } 
# Note : yourscore_eachdept[dept] = total score of each department , avg_minscore[dept] = average minscore of each department 

# Step 7 : Quote score condition for each department 
status_eachdept_dict = {} 

for each_dept in weighted_min_possibility : 

    # case 1 : Chance >= 120% 
    if weighted_min_possibility[each_dept] >= 120 : # add key (dept name) and value (quote) to condition_quote dict 
        status_eachdept_dict[each_dept] = "คะเเนนเลยที่คาดการณ์พอสมควร มีโอกาสติดสูงมาก ✅✅" 
        
    # case 2 : Chance between 85% and 120% 
    elif 85 <= weighted_min_possibility[each_dept] <= 120 : # add key (dept name) and value (quote) to condition_quote dict 
        status_eachdept_dict[each_dept] = "คะเเนนค่อนข้างเซฟ มีโอกาสติดสูง 🫡" 
        
    # case 3 : Chance between 60% and 85% 
    elif 60 <= weighted_min_possibility[each_dept] <= 85 : # add key (dept name) and value (quote) to condition_quote dict 
        status_eachdept_dict[each_dept] = "คะเเนนไม่ค่อยเซฟ มีลุ้นได้ เเต่ต้องดู Ranking ประกอบ 😌" 
        
    # case 4 : Chance between 30% and 60% 
    elif 30 <= weighted_min_possibility[each_dept] <= 60 : # add key (dept name) and value (quote) to condition_quote dict 
        status_eachdept_dict[each_dept] = "คะเเนนไม่เซฟเลย มีความเสี่ยงหลุดสูง 😭😭" 
        
    # case 5 : Chance less than 30 
    elif weighted_min_possibility[each_dept] <= 30 : # add key (dept name) and value (quote) to condition_quote dict 
        status_eachdept_dict[each_dept] = "หาภาคอื่นสำรองเถอะ สุ่มเสี่ยงเกินไป 💀💀" 
        
# Step 7 : display after submit button 
if (submitted == True) : 
    # 7.1 : Create a DataFrame to display results 
    result_df = pd.DataFrame({ 
        # DataFram consists of : #   - Department lists , Score for each department , Minscore (Avg , Weighted) , 
                                 #   - % Chance of getting department (Avg , Weighted) , Recommended Status 
                                 # filled in this form : 'Column Name' : list of values 
                'Department': list(yourscore_dict.keys()), 
                'Your Score': list(yourscore_dict.values()), 

                'Min Score (Average)': [round(avg_minscore_dict[dept], 1) for dept in yourscore_dict], 
                '% Chance (Average)': [round(average_min_possibility[dept], 1) for dept in yourscore_dict], 

                'Min Score (Weighted)' : [round(weighted_minscore_dict[dept], 1) for dept in yourscore_dict], 
                '% Chance (Weighted)': [round(weighted_min_possibility[dept], 1) for dept in yourscore_dict], 
                
                'Evaluation Result (WEighted)' : [status_eachdept_dict[dept] for dept in yourscore_dict] }) 
                
    # 7.2 : Display data of dream department first 
    st.divider() # divide code 
    st.subheader(f"🎯 Your Dream Department Evaluation : {dream_department} ") 
    st.subheader(f"% Chance of Getting this department (Weighted) : {weighted_min_possibility[dream_department]:.1f} %") 
    st.subheader(f"Status : {status_eachdept_dict[dream_department]}") 
    
    # 7.3 : Display the results using Streamlit 
    st.divider() # divide code 
    st.subheader("🔍 Result for Intania Department Calculation") 
    st.dataframe(result_df , use_container_width = True) # use_contanier_width is for expanding DataFrame to full width 
    
# markdown for ending message 
st.markdown("Copyright © 2025 NuBFightForCP51Again , All rights reserved.") 
st.markdown("Big thanks to the old version of this program [You can try it here](https://intania-department-calculator.vercel.app/?fbclid=IwAR1Qr4YZ_Liix9ZyB20HmsS9Q6dwh1GIqFVKwdD1BCzpfconQ1Kbe92b2O0) ")
