import streamlit as st
import pandas as pd
def summary():
    st.title("ISOS 데이터 품질 평가 Solution")
    with st.expander("데이터 품질 평가 관련 솔루션"):
        st.markdown("""\n
    ISO 8000 데이터 품질에 대한 국제 표준\n
    ISO/IEC 25024 소프트웨어 엔지니어링 및 시스템에 대한 국제 표준\n
    의 기준을 따름""")
    st.subheader("목적")
    st.info("기업 및 기관이 데이터 기반의 의사결정을 내리기 위해 사용하는 데이터의 품질을 평가하고 향상시키는 것을 목적으로 함")
    st.subheader("적용범위")
    st.info("모든 데이터 중심 기업/기관 : 제조, 금융, 유통, 헬스케어 등 모든 분야에서 데이터 기반의 의사결정을 하는 기업 및 기관")
    st.subheader("제약조건")
    st.info("표준 규정에 따른 평가 : ISO8000 및 ISO/IEC 25024에 명시된 규정 및 기준에 따라 데이터 평가 적용")
    st.subheader("프로세스")
    st.image("images/dataquality_process.png")
    st.subheader("기대효과")
    st.image("images/data_effect.png")
    if st.button("데이터 품질 평가 기준 설명", use_container_width=True):
        st.session_state['page']='ISO8000'
        st.experimental_rerun()
        
@st.cache_data(show_spinner="Fetching data from source")
def get_data(path):
    return pd.read_csv(path, index_col=0)
    
def ISO8000():
    st.subheader("ISO 8000 데이터 품질에 관한 국제 표준")
    st.image("images/iso8000.jpg")
    st.markdown("""
             데이터의 정확성, 완전성, 신뢰성, 유효성, 일관성, 그리고 더 나아가 데이터가 적절한 시점과 형식으로 사용자에게 제공되는지 등에 대한 기준을 설정합니다. 이는 데이터의 생명주기 전반에 걸쳐 적용되며, 데이터 획득, 저장, 관리, 공유, 및 활용 등 여러 과정에서 데이터 품질을 보장하기 위한 방안을 제시합니다.

ISO 8000은 다음과 같은 주요 부분으로 구성될 수 있습니다:

데이터 아키텍처와 모델링: 데이터의 구조와 관계를 어떻게 설계할 것인지에 대한 지침을 제공합니다.

데이터 획득과 식별: 어떤 데이터를 획득할 것인지, 어떻게 식별할 것인지에 대한 기준을 마련합니다.

데이터 유효성 검사: 데이터가 특정 기준이나 규칙을 만족하는지를 확인합니다.

데이터 관리와 유지 보수: 어떻게 데이터를 안전하게 저장, 관리, 및 유지 보수할 것인지에 대한 지침을 제공합니다.

데이터 공유와 통합: 여러 시스템이나 조직 간에 데이터를 어떻게 공유하고 통합할 것인지에 대한 규칙과 지침을 마련합니다.

데이터 품질 측정: 데이터 품질을 어떻게 측정하고 평가할 것인지에 대한 메트릭과 툴을 제안합니다.

데이터 보안: 데이터의 민감성, 기밀성, 접근 제어 등에 관한 보안 기준을 설정합니다.

데이터 문서화: 데이터의 메타데이터, 문서화, 설명 등을 어떻게 관리할 것인지에 대한 지침을 제공합니다.

ISO 8000은 특히 큰 조직이나 복잡한 데이터 환경에서 중요한 역할을 할 수 있으며, 데이터 품질을 향상시키고 데이터 관련 문제를 최소화하는 데 큰 도움을 줄 수 있습니다.
             """)
    if st.button("ISO/IEC 25024 설명", use_container_width=True, key='body'):
        st.session_state['page']='ISOIEC25024'
        st.experimental_rerun()
def ISOIEC25024():
    st.subheader('ISO/IEC 25024 소프트웨어 및 시스템 제품 품질의 "데이터 품질 모델"에 대한 국제 표준')
    st.image("images/isoiec25024.jpg")
    st.markdown("""
                데이터 품질에 대한 일반적인 모델을 제공하며, 데이터 품질을 측정하고 평가하는 데 사용할 수 있는 특성과 메트릭을 정의합니다.

                ISO/IEC 25024는 데이터의 다음과 같은 품질 특성을 고려합니다:

                정확성(Accuracy): 데이터가 표현하는 현실 세계의 정확한 표현이어야 합니다.

                완전성(Completeness): 필요한 모든 데이터 항목이 포함되어야 합니다.

                일관성(Consistency): 동일한 데이터 항목은 시간과 공간에 걸쳐 일관된 값을 가져야 합니다.

                신뢰성(Reliability): 데이터는 원본과 일치하며, 오류가 없어야 합니다.

                유효성(Validity): 데이터는 정의된 규칙과 제약 조건을 충족해야 합니다.

                사용 가능성(Usability): 데이터는 명확하고 이해하기 쉬워야 하며, 사용자가 원하는 작업을 수행하는 데 유용해야 합니다.

                이러한 특성을 측정하고 평가하기 위한 다양한 메트릭을 정의할 수 있으며, 이 표준은 그러한 메트릭을 제공하거나 참고할 수 있도록 지침을 제공합니다.

                ISO/IEC 25024는 데이터 품질의 다양한 측면을 측정하고 평가하는 데 도움을 주는 중요한 표준 중 하나입니다. 이 표준을 따르면, 조직은 데이터 품질을 개선하고, 데이터 관련 문제를 미리 인식하고, 데이터의 가치를 극대화할 수 있습니다.
                """)
    if st.button("품질 평가 시작", use_container_width=True):
        st.session_state['page']='Accuracy'
        st.experimental_rerun()
def Load():
    global data
    uploaded_file = st.file_uploader("데이터 로딩", type=['csv','xls','xlsx'])
    if uploaded_file:
        data = get_data(uploaded_file)
        st.session_state['data']=data
        st.dataframe(data)
    elif 'data' in st.session_state:
        st.dataframe(st.session_state['data'])
    if st.button("데이터 초기화"):
        try:
            del st.session_state['data']
        except:
            st.warning("데이터 로딩 정보가 없습니다.")
class Accuracy:
    def __init__(self):
        st.header("Accuracy")
        
        st.subheader("데이터 검증 Data Validation")
        st.write("범위 검증")
        st.write("데이터 타입 검증")
        st.write("유일성 검증")
        st.session_state['data']
        
def Completeness():
    st.header("Completeness")
    
def Consistency():
    st.header("Consistency")
def Reliability():
    st.header("Reliability")
def Validity():
    st.header("Validity")
def Timeliness():
    st.header("Timeliness")