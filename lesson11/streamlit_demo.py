import streamlit as st

st.text("Fixed width text")
st.markdown("_Markdown_") # see *
st.latex(r""" e^{i\pi} + 1 = 0 """)
st.title("My title")
st.header("My header")
st.subheader("My sub")
st.code("for i in range(8): foo()")
st.html("<p>Hi!</p>")

url = 'https://www.twse.com.tw'
st.link_button("Go to TWSE", url)

checkbox1 = st.checkbox("I agree")
radio1 = st.radio("Pick one", ["cats", "dogs"])
selectbox1 = st.selectbox("Pick one", ["grape", "apple", "mongo"])
multiselect1 = st.multiselect("Buy", ["milk", "apples", "potatoes"])
slider1 = st.slider("Pick a number", 0, 100)

if st.button("Click me"):
    st.markdown("## 按到我了 !!")
    st.write(checkbox1)
    st.write(radio1)
    st.write(selectbox1)
    st.write(multiselect1)
    st.write(slider1)
