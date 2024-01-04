import streamlit as st


st.title("Famous Environmentalist ")

st.session_state['answer'] = ''

st.write(st.session_state)

realans = ['', 'abc', 'edf']

if  st.session_state['answer'] in realans:
    answerStat = "correct"
elif st.session_state['answer'] not in realans:
    answerStat = "incorrect"

st.write(st.session_state)
st.write(answerStat)

url_image = "https://upload.wikimedia.org/wikipedia/commons/6/6f/Greta_Thunberg_02_cropped.jpg"

image(image_url, use_column_width=True)


#text about the person
Click = st.button("Reveal Info About Greta Thunberg")

if Click:

    st.title("About")
    st.text("Born: January 3, 2003 (age 20 years), Stockholm, Sweden")
    st.text("Parents: Svante Thunberg, Malena Ernman")
    st.text("Height: 1.49 m")
    st.text("Movement: School Strike for Climate")
    st.write("Awards List [link](https://en.wikipedia.org/wiki/Greta_Thunberg#Honours_and_awards:~:text=COVID%2D19%20pandemic.-,Honours%20and%20awards,doctorate%20was%20scheduled%20to%20be%20granted%20in%20June%202023.%5B301%5D,-Species%20named%20in)")
    st.sidebar.success("Choose a page.")
