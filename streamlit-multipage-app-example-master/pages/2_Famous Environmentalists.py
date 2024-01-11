import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import requests

st.title("Biggest Youth Climate Activist")

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

col1, col2 = st.columns(2)

lottie_sustainability = load_lottieurl("https://lottie.host/cef9acda-9ca2-4ba8-b632-a011c99ba5a1/kaI1BWTads.json")



with col2:
    st_lottie(lottie_sustainability, height= 500, width= 500)

st.sidebar.success("Choose a page.")


with st.container():
    url_image = ("streamlit-multipage-app-example-master/Greta_Thunberg_02_cropped.jpg")
    #the image that pops up onto the screen
    col1.image(url_image, use_column_width=True)

    #text about the person
    on = col1.toggle('Reveal Info About Greta Thunberg')

    if bool(on):
        with col1:
            st.title("About")
            st.text("Born: January 3, 2003 (age 20 years), Stockholm, Sweden")
            st.text("Parents: Svante Thunberg, Malena Ernman")
            st.text("Height: 1.49 m")
            st.text("Movement: School Strike for Climate")
            st.write("Awards List [link](https://en.wikipedia.org/wiki/Greta_Thunberg#Honours_and_awards:~:text=COVID%2D19%20pandemic.-,Honours%20and%20awards,doctorate%20was%20scheduled%20to%20be%20granted%20in%20June%202023.%5B301%5D,-Species%20named%20in)")

st.markdown("---")

col1, col2 = st.columns(2)

col2.title("Environmental Activist")

with st.container():
    url_image2 = "streamlit-multipage-app-example-master/Haven_Coleman_(cropped).jpg"
    #the image that pops up onto the screen
    col2.image(url_image2, use_column_width=True)

    on = col2.toggle('Reveal Info About Haven Coleman')

    if bool(on):
        with col2:
            st.title("About")
            st.text("Born: March 29, 2006 (age 17), Denver, Colorado")
            st.text("Known For: Environmental activism")
            st.write("More About Her Here [link](https://en.wikipedia.org/wiki/Haven_Coleman)")

    lottie_gif = load_lottieurl("https://lottie.host/7c38eddf-c84e-4e74-8118-b969df786f36/Z6YjX2n4ME.json")



    with col1:
        st_lottie(lottie_gif, height= 500, width= 700)


st.markdown("---")

col1, col2 = st.columns(2)

col1.title("Celebrity Climate Activist")

with st.container():
    url_image3 = ("https://www.un.org/sites/un2.un.org/files/styles/large-article-image-style-16-9/public/field/image/1581003090.3685.jpg")
    col1.image(url_image3, use_column_width=True)

    on = col1.toggle('Reveal Info About Leonardo DiCaprio')

    if bool(on):
        with col1:
            st.title("About")
            st.write("**Born**: November 11, 1974 (age 49) Los Angeles, California, U.S.")
            st.write("**What He Has Done For Climate Change and Sustainability**: He has donated 100 million dollars to fight climate change and the news is [Here](https://www.khaleejtimes.com/citytimes/hollywood/hollywood-stars-foundation-donates-dh367m-to-fight-climate-change) and In 2017, DiCaprio was named a United Nations Messenger of Peace with a special focus on climate change")

    lottie_gif = load_lottieurl("https://lottie.host/7c38eddf-c84e-4e74-8118-b969df786f36/Z6YjX2n4ME.json")






