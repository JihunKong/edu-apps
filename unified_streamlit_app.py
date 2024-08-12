
import streamlit as st

# 사이드바에 탭을 구성
st.sidebar.title("앱 선택")
app_selection = st.sidebar.radio("앱을 선택하세요:", 
                                 ('Life Coach', 'Ethical Dilemma System', 'School Food', 
                                  'Literature', 'Grasps', 'Test Feedback', 
                                  'Student Record Enhancement System', 'Curriculum', 'Evaluation'))

# 각 앱의 메인 코드를 조건문으로 구분하여 포함
if app_selection == 'Life Coach':
    st.title("Life Coach")
    with open('/mnt/data/extracted_apps/lifecoach-main/app.py') as f:
        exec(f.read())
        
elif app_selection == 'Ethical Dilemma System':
    st.title("Ethical Dilemma System")
    with open('/mnt/data/extracted_apps/ethical-dilemma-system-main/app.py') as f:
        exec(f.read())
        
elif app_selection == 'School Food':
    st.title("School Food")
    with open('/mnt/data/extracted_apps/schoolfood-main/app.py') as f:
        exec(f.read())
        
elif app_selection == 'Literature':
    st.title("Literature")
    with open('/mnt/data/extracted_apps/literature-main/app.py') as f:
        exec(f.read())
        
elif app_selection == 'Grasps':
    st.title("Grasps")
    with open('/mnt/data/extracted_apps/grasps-main/app.py') as f:
        exec(f.read())
        
elif app_selection == 'Test Feedback':
    st.title("Test Feedback")
    with open('/mnt/data/extracted_apps/test_feedback-main/app.py') as f:
        exec(f.read())
        
elif app_selection == 'Student Record Enhancement System':
    st.title("Student Record Enhancement System")
    with open('/mnt/data/extracted_apps/student-record-enhancement-system-main/app.py') as f:
        exec(f.read())
        
elif app_selection == 'Curriculum':
    st.title("Curriculum")
    with open('/mnt/data/extracted_apps/curriculum-main/app.py') as f:
        exec(f.read())
        
elif app_selection == 'Evaluation':
    st.title("Evaluation")
    with open('/mnt/data/extracted_apps/evaluation-main/app.py') as f:
        exec(f.read())
