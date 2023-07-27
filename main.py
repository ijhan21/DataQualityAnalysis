import streamlit as st
from utils import *
st.title("ISOS 데이터 품질 평가 Solution")
st.divider()
with st.expander("데이터 품질 평가 관련 솔루션"):
    st.markdown("""\n
ISO 8000 데이터 품질에 대한 국제 표준\n
ISO/IEC 25024 소프트웨어 엔지니어링 및 시스템에 대한 국제 표준\n
의 기준을 따름""")
    
if 'page' not in st.session_state:
    st.session_state['page']='load'
    # st.session_state['page']='metrics'
with st.sidebar:    
    st.markdown("## 데이터 품질평가 항목")
    if st.button("정확성 Accuracy", type='primary' if st.session_state['page']=='load' else 'secondary', use_container_width=True):
        st.session_state['page']='load'
        st.experimental_rerun()
    if st.button("완전성 Completeness", type='primary' if st.session_state['page']=='report' else 'secondary', use_container_width=True):
        st.session_state['page']='report'
        st.experimental_rerun()
    if st.button("일관성 Consistency", type='primary' if st.session_state['page']=='preprocess' else 'secondary', use_container_width=True):
        st.session_state['page']='preprocess'
        st.experimental_rerun()
    if st.button("신뢰성 Reliability", type='primary' if st.session_state['page']=='datasets' else 'secondary', use_container_width=True):
        st.session_state['page']='datasets'
        st.experimental_rerun()
    if st.button("유효성 Validity", type='primary' if st.session_state['page']=='modeling' else 'secondary', use_container_width=True):
        st.session_state['page']='modeling'
        st.experimental_rerun()
    if st.button("적시성 Timeliness", type='primary' if st.session_state['page']=='metrics' else 'secondary', use_container_width=True):
        st.session_state['page']='metrics'        
        st.experimental_rerun()

if st.session_state['page']=='load':
    load()