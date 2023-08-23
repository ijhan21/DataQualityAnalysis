import streamlit as st
from utils import *

    
if 'page' not in st.session_state:
    st.session_state['page']='SUMMARY'
    # st.session_state['page']='metrics'
with st.sidebar:
        
    if st.button("개요", type='primary' if st.session_state['page']=='SUMMARY' else 'secondary', use_container_width=True):
        st.session_state['page']='SUMMARY'
        st.experimental_rerun()
    
    st.markdown("## 데이터 품질평가 기준")
    if st.button("ISO 8000 설명", type='primary' if st.session_state['page']=='ISO8000' else 'secondary', use_container_width=True):
        st.session_state['page']='ISO8000'
        st.experimental_rerun()
    if st.button("ISO/IEC 25024 설명", type='primary' if st.session_state['page']=='ISOIEC25024' else 'secondary', use_container_width=True):
        st.session_state['page']='ISOIEC25024'
        st.experimental_rerun()
    st.markdown("## 데이터 품질평가")
    if st.button("데이터 로딩", type='primary' if st.session_state['page']=='Load' else 'secondary', use_container_width=True):
        st.session_state['page']='Load'
        st.experimental_rerun()
    if st.button("정확성 Accuracy", type='primary' if st.session_state['page']=='Accuracy' else 'secondary', use_container_width=True):
        st.session_state['page']='Accuracy'
        st.experimental_rerun()
    if st.button("완전성 Completeness", type='primary' if st.session_state['page']=='Completeness' else 'secondary', use_container_width=True):
        st.session_state['page']='Completeness'
        st.experimental_rerun()
    if st.button("일관성 Consistency", type='primary' if st.session_state['page']=='Consistency' else 'secondary', use_container_width=True):
        st.session_state['page']='Consistency'
        st.experimental_rerun()
    if st.button("신뢰성 Reliability", type='primary' if st.session_state['page']=='Reliability' else 'secondary', use_container_width=True):
        st.session_state['page']='Reliability'
        st.experimental_rerun()
    if st.button("유효성 Validity", type='primary' if st.session_state['page']=='Validity' else 'secondary', use_container_width=True):
        st.session_state['page']='Validity'
        st.experimental_rerun()
    if st.button("적시성 Timeliness", type='primary' if st.session_state['page']=='Timeliness' else 'secondary', use_container_width=True):
        st.session_state['page']='Timeliness'        
        st.experimental_rerun()

if st.session_state['page']=='SUMMARY':
    summary()
if st.session_state['page']=='ISO8000':
    ISO8000()
if st.session_state['page']=='ISOIEC25024':
    ISOIEC25024()
if st.session_state['page']=='Load':
    Load()
if st.session_state['page']=='Accuracy':
    Accuracy()
if st.session_state['page']=='Completeness':
    Completeness()
if st.session_state['page']=='Consistency':
    Consistency()
if st.session_state['page']=='Reliability':
    Reliability()
if st.session_state['page']=='Validity':
    Validity()
if st.session_state['page']=='Timeliness':
    Timeliness()