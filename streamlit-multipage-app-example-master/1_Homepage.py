import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import requests

st.markdown(
    """
<style>
.css-nzvw1x {
    background-color: #314E92 !important;
    background-image: none !important;
    ,

    unsafe_allow_html=True
)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_sustainabilty = load_lottieurl("https://lottie.host/e716e02e-c7d5-4a8b-8750-6a3c0feb0845/JZqwhLJCLA.json")

# Set page title and favicon
st.set_page_config(
    page_title="Sustainability Homepage",
    page_icon="🌱",
    layout="wide",
)

st.sidebar.success("Choose a page.")

# Example Image URL (OpenAI's logo)
image_url = "https://www.investopedia.com/thmb/iN1zICPiRmVkfpng4dHOFhDSOZo=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/terms_s_sustainability_FINAL-78ce04eecd9b42e8ab1222b98c6aa79e.jpg"

# Display the image and text side by side
col1, col2 = st.columns(2)

# Column 1: Display the image
col2.image(image_url, use_column_width=True)

# Column 2: Display text
col1.write("""
# Welcome to My Sustainability Website 🌍

According to Wikipedia Sustainability means "meeting our own needs without compromising the ability of future generations to meet their own need"(Wikipedia Contributors)
""")
col2.write("""
## Why Sustainability Matters

Sustainability is at the core of our values. It's not just about preserving the environment; it's about creating a better world for future generations and so that our kids will have all the beautiful scenery as we have today.
more about why sustainability is important below with a video

### My Website Initiatives

- **What is Sustainability and Why it is important:** On the homepage there is info about this that you can read through plus it you can also watch a video.

- **Make Yourself Sustainable:** There is a whole page on this can you can go onto it to find out how you yourself can be sustainable.

- **Grow Awareness About Sustainability:** I made this website so that you can learn about sustainability in a interactive way.



""")

with col1:
    st_lottie(lottie_sustainabilty, height= 300, width= 500)




    #import streamlit as st

    #st.set_page_config(
    #    page_title="Sustainablity Awerness Website"
    #)

    #st.subheader("Hi Im yety")
    #st.title("A Website About Sustainability")

    #st.subheader("What Is Sustainability?")
    #st.write("The most often quoted definition comes from the UN World Commission on Environment Development: “sustainable development is development that meets the needs of the present without compromising the ability of future generations to meet their own needs.” In the charter for the UCLA Sustainability Committee, sustainability is defined as: “the integration of environmental health, social equity and economic vitality in order to create thriving, healthy, diverse and resilient communities for this generation and generations to come. The practice of sustainability recognizes how these issues are interconnected and requires a systems approach and an acknowledgement of complexity. Sustainable practices support ecological, human, and economic health and vitality. Sustainability presumes that resources are finite, and should be used conservatively and wisely with a view to long-term priorities and consequences of the ways in which resources are used. In simplest terms, sustainability is about our children and our grandchildren, and the world we will leave them.(“What Is Sustainability? | UCLA Sustainability”)")

    #st.sidebar.success("Choose a page.")

video_file = open('streamlit-multipage-app-example-master/Why is sustainability important_ A tip to explain it.mp4', 'rb')
st.video(video_file)
st.subheader('[(Sustainability Illustrated)](https://www.youtube.com/watch?v=EbZcQe9J-EE)')
