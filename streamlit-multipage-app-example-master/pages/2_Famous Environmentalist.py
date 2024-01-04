
import streamlit as st


st.title("Famous Environmentalist ")



#the image that pops up onto the screen
st.image('streamlit-multipage-app-example-master/Greta_Thunberg_02_cropped.jpg', caption= "Greta Thunberg")

#text about the person
Click = st.button("Reveal Info About Greta Thunberg")

if Click is True:

    st.title("About")
    st.text("Born: January 3, 2003 (age 20 years), Stockholm, Sweden")
    st.text("Parents: Svante Thunberg, Malena Ernman")
    st.text("Height: 1.49 m")
    st.text("Movement: School Strike for Climate")
    st.write("Awards List [link](https://en.wikipedia.org/wiki/Greta_Thunberg#Honours_and_awards:~:text=COVID%2D19%20pandemic.-,Honours%20and%20awards,doctorate%20was%20scheduled%20to%20be%20granted%20in%20June%202023.%5B301%5D,-Species%20named%20in)")
    st.sidebar.success("Choose a page.")

    else 
    st.write("click the button")


# Set page title and favicon
st.set_page_config(
    page_title="Button Example",
    layout="centered",
)

# Button to toggle text visibility
if st.button("Toggle Text Visibility"):
    # Display text when the button is clicked
    st.write("Text is visible now!")

# You can add additional content outside the button, and it will always be visible
st.write("This text is always visible.")
