import streamlit as st
st.set_page_config(page_icon="😊",page_title="PortFolio",layout="wide")
st.title("Karthik",anchor=False)
st.subheader("Java Developer | Gamer",anchor=False)
with st.container(border=True):
    st.info("I am ..............")
col1,col2,col3=st.columns(3)
with col1:
    with st.expander(label="Certifications",expanded=False):
        st.info("NPTEL")
        st.image("data:image/png;base64,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",width=400)
with col2:
    with st.expander(label="Certifications",expanded=False):
        st.warning("Cisco")
with col3:
    with st.expander(label="Certifications",expanded=False):
        st.error("Great Learning")