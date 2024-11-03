import streamlit as st

def operator_screen():
    container_operator = st.container(height=None,border=True,key=None)
    # st.markdown("<h1 style='text-align: center; color: white;'>Login Page</h1>", unsafe_allow_html=True)
    container_operator.markdown("<h1 style='text-align: right; color: white;'>این قسمت توسط اپراتور انجام میشود</h1>", unsafe_allow_html=True)
    container_operator.text_input('Form Code',key='form_code')
    container_operator.selectbox('Section',options=['Chipper',
                                                    'Conveyor Line',
                                                    'Energy Plant',
                                                    'Dryer & Air Grader',
                                                    'Refiner',
                                                    'Before Press',
                                                    'Press',
                                                    'After Press',
                                                    'Sanding & RBS',
                                                    'Cooling System'
                                                    'Steam Boiler',
                                                    'General'
                                                    ],index = None,key='section_name')
    container_operator.text_input('مشخصات دستگاه',key='machine_name')
    container_operator.selectbox('شیفت',options=[
                                                'A',
                                                'B',
                                                'C'
                                                ],key='shift',index = None)
    container_operator.text_input('نام درخواست کننده',key='operator')
    container_operator.selectbox('نوع عیب',options=[
                                                    'مکانیکی',
                                                    'برقی',
                                                    'تولید',
                                                    'تاسیسات',
                                                    'فلزکاری'
                                                    ],index = None)
    container_operator.subheader('تعیین زمان بروز اشکال')
    if container_operator.selectbox('وضعیت توقف',options=['ندارد','دارد']) == 'ندارد':
        container_operator.date_input('زمان شروع توقف',key='stop',disabled=True)
        container_operator.date_input('زمان پایان توقف',key='start',disabled=True)
    else:
        container_operator.date_input('زمان شروع توقف',key='stop',disabled=False)
        container_operator.date_input('زمان پایان توقف',key='start',disabled=False)

    if container_operator.button('ثبت',key='operator_section'):
        st.success('Everything Works Fine')



operator_screen()

