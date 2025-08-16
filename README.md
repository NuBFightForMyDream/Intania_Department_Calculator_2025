# Web App : Intania Department Calculator (2025 Version) (เราเลือกภาค หรือให้ภาคเลือกเรา)

## Contributors
- 6730084521 Chatrphol Ovanonchai (Main Contributors)
  
## 🧮 Introduction
The idea from this project is from myself that can't wait for Engineering Registeration Department that works so slow and I want to renovate the old web which doesn't cover latest data.
So , It was developed to a brand new web application for 1st year General Engineering Student @ Chulalongkorn University to decide and calculate which department is the their best choice.
> ⭐⭐⭐ Well if you don't understand about how we'll choose our department. You can read it via this link [How to เลือกสาขาวิชาในฝัน By Nine #2 รวม Ft.วิน #2 รวม](https://www.canva.com/design/DAGrAdyzMJE/nLnY6-VaIXCXFQC1ts7e1A/edit?utm_content=DAGrAdyzMJE&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton) (In progress)

## 💡Easier ways to use this app via Google Sheets
- This is example of Google Sheets calculator screen
![Example of Google Sheets calculator](https://github.com/NuBFightForCP51Again/Intania_Department_Calculator/blob/main/Intania%20Department%20Calculator%20Example%20Sheets.jpg)
[You can try this program via this link , Do not use it for commercials](https://docs.google.com/spreadsheets/d/1vxl09wGhZNzD7PMFiAnqD_VPttb0QYFxf6-nfpaY2iY/edit?gid=922121716#gid=922121716)

## ✖️2️⃣ Multiplier charts & 10-year back history of department choosing
![Multiplier Chart](https://github.com/NuBFightForCP51Again/Intania_Department_Calculator/blob/main/Multiplier%20Intania%20Department.jpg) Big thanks for ESC Chula for this picture

[💻 Drive of history of 10-year back (2006-2024) Via this link](https://drive.google.com/drive/folders/1txEBUvLlHcWB706bdATHjrJsf_BAV-vm?usp=sharing)

## ‼️ Cautions for using this calculator (Written in Excel)
- Use this carefully , **Don't be obsessed** with this program too much. It can leads to your mental heakth unintentionally.
- This program didn't consist of external factors (popularity , Seats for each department , Psychology game behind department choosing)
- **Georesources & Nuclear** Engineering are **NOT** in this program (because of unpopular department , info not covered 6-year (some year didn't aren't applicable via choosing department) )
- This program didn't contain **Safe Score** for each department (with this score , nisits can ensure that they have higher possibilities to get their dream department) [but in shhets have it]
- Opening google sheets in iPad can cause bug (shown as "Loading ...") . so , reopen it and it will shown your score
- Formula of % Chance is **`100 + [(Your_score - Min_score) / Min_score * 400] (Change Difference to Percent then x4 and compare to 100 percent)`**

## 🔎 2 Methods of calculating **Minimum Score**
Well , I created 2 methods how to calculate score for each department.
  - The first nethod is **Average Minimum Score** which caculate 6-year back minimum score then find average of them
  - The second method is **Weighted Minimum Score** . Because of Civil Engineering in 2023 having a bug score (7.5 points , which was retired from university) . So , I weigted score differently on each year (0.16 for other year , and 0.20 for latest year) [for Civil it'll be 0.19 amnd 0.15 respectively]
  > Update 21/6/2025 : Weighted score will be depend on factors on each department (popularity , min score , external factors) , So percentage of chance will be changed too.

## 💡Easier ways to use this app via Google Sheets
[Via this link , Do not use it for commercials](https://docs.google.com/spreadsheets/d/1vxl09wGhZNzD7PMFiAnqD_VPttb0QYFxf6-nfpaY2iY/edit?gid=922121716#gid=922121716)

## 💻 Code Explained : How can I created this project
1. First , you need to install some library in your command prompt

   ```
   py -m pip install streamlit
   py -m pip install pandas # for DataFrame
   py -m pip install numpy # for Mathematical Calculation
   ```

  Note : I edited all code in Github codespaces (to practice using Git commands). Git command using in this program will be
  
  ```
    # First you need to press ☑️ Commit in GitHub Extension first . Then these are commands for commit & push to GitHub respectively
    git commit -m "Update your commit message here"
    git push origin main # push to main branch
  ```
    
2. Changing formula from Google Sheets to Python code (you can read my code & my explained description in `main_calculator.py`)
   
3. After done all code , run `main_calculator.py` using this cmd in terminal
      ```
      streamlit run main_calculator.py
      ```
   It will shown as local web , you need to publish your code to GitHub and Streamlit cloud too.

Note : Here's some commands and some methods/functions you can learn it via [Streamlit Documentation](https://docs.streamlit.io/)

And that's all my process. Hope yall get your dream department. Fighting !! 🫡🦾
