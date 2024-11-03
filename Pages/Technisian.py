import streamlit as st
from setuptools.command.editable_wheel import editable_wheel
from forms.aghlam import aghlam_form
from Pages.Operator import operator_screen
from forms.tech import tech_form


def operator_screen(read_only=False):
    if read_only:
        container_operator = st.container(height=None,border=True,key=None)
        container_operator.subheader('این قسمت توسط اپراتور انجام شده است')
        container_operator.text_input('شماره درخواست',key='form_code',disabled=True)
        container_operator.selectbox('نام واحد',options=['Chipper',
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
                                                        ],key='section_name',disabled=True)
        container_operator.text_input('مشخصات دستگاه',key='machine_name',disabled=True)
        container_operator.selectbox('شیفت',options=[
                                                'A',
                                                'B',
                                                'C'
                                                ],key='shift',disabled=True)
        container_operator.text_input('نام درخواست کننده',key='operator',disabled=True)
        container_operator.selectbox('نوع عیب',options=[
                                                        'مکانیکی',
                                                        'برقی',
                                                        'تولید',
                                                        'تاسیسات',
                                                        'فلزکاری',
                                                        ], disabled=True)
        container_operator.subheader('تعیین زمان بروز اشکال')
        container_operator.selectbox('وضعیت توقف',options=['ندارد','دارد'],disabled=True)
        container_operator.date_input('زمان شروع توقف',key='stop',format="YYYY/MM/DD",disabled=True)
        container_operator.date_input('زمان پایان توقف',key='start',disabled=True)
    else:
        st.title('Operator Page')
        
        
def technisian_screen():
    operator_screen(read_only=True)
    
    @st.dialog('اقلام')
    def show_aghlam_form():
        aghlam_form()
    
    @st.dialog('تکنیسین')
    def show_tech_form():
        tech_form()
        
    container_technisian = st.container(height=None,border=True,key=None)

    container_technisian.subheader('این قسمت توسط واحد انجام دهنده تعمیرات تکمیل می گردد')
    container_technisian.selectbox('نوع تعمیرات',options=['EM','CM','GM','PM'],key='problem_type',index = None)
    container_technisian.selectbox('نوع خدمات',options=['بازرسی و چک','تنظیم','آچارکشی','روانکاری','تعمیر','تعویض'],key='service_type',index = None)
    if container_technisian.selectbox('علت خرابی',options=['استهلاک طبیعی','عدم دقت اپراتور','نامناسب بودن تعمیرات قبلی','کیفیت پایین قطعه یدکی',
        'سرویس و نگهداری نامناسب','سایر مشکلات'],
        key='failure_type',
        index = None) == 'سایر مشکلات':
        container_technisian.text_area('توضیحات سایر مشکلات')
    else:
        container_technisian.success('Everything Fine')
            
    container_technisian.subheader('زمان های انجام کار')
    container_technisian.text_input('مدت تشخیص عیب',key='problem_time')
    container_technisian.text_input('مدت تهیه لوازم یدکی',key='aghlam_time')
    container_technisian.text_input('مدت انجام عملیات',key='operation_time')
    container_technisian.text_input('مدت راه اندازی خط',key='start_time')
    container_technisian.text_input('زمان تلف شده',key='wasted_time')
    container_technisian.text_input('جمع کل زمان عملیات',key='total_time')
    container_technisian.text_input('نفر ساعت صرف شده',key='person_time')
    container_technisian.text_area(':علت تاخیرات',key='discription')
    container_technisian.text_area(':شرح کامل اقدامات انجام شده جهت رفع عیب',key='problem')

    if container_technisian.button('ثبت',key='Submit'):
        st.success('Everything is fine')
        
    if container_technisian.button('اقلام',key=''):
        show_aghlam_form()
        
    if container_technisian.button('تکنیسین',key=''):
        show_tech_form()
        
        
        
technisian_screen()
