import streamlit as st
st.set_page_config(layout="wide")
choice = st.sidebar.selectbox("Select your choice",{"Summarize text", "Summarize document"})
if choice =="Summarize Text":
    st.subheader("Summarize Text using txtai")
    input_text = st.text_area("Enter your text here")
    input_text = st.text_area("Enter your text here")
    if st.button("Summarize text"):
        col1, col2= st.coloumn([1,1])
        with col1:
            st.markdown("your input text")
            st.info(input_text)
        
elif choice == "Summarize Document":
    st.subheader("Summarize Document using txtai")
    input_file = st.file_uploader("Upload your document", type = ["pdf"])
    if st.button("Summarize document"):
        pass
    
