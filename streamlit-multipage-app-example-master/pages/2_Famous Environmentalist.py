import streamlit as st

st.title("Famous Environmentalist ")

# The image that pops up onto the screen
st.image('streamlit-multipage-app-example-master/Greta_Thunberg_02_cropped.jpg', caption="Greta Thunberg")

# Text about the person
click_button = st.button("Reveal Info About Greta Thunberg")

# Check if the button is clicked
if click_button:
    # Display information when the button is clicked
    st.title("About")
    st.text("Born: January 3, 2003 (age 20 years), Stockholm, Sweden")
    st.text("Parents: Svante Thunberg, Malena Ernman")
    st.text("Height: 1.49 m")
    st.text("Movement: School Strike for Climate")
    st.write("Awards List [link](https://en.wikipedia.org/wiki/Greta_Thunberg#Honours_and_awards:~:text=COVID%2D19%20pandemic.-,Honours%20and%20awards,doctorate%20was%20scheduled%20to%20be%20granted%20in%20June%202023.%5B301%5D,-Species%20named%20in)")
    st.sidebar.success("Choose a page.")
else:
    # Optionally display some initial information
    st.info("Click the button to reveal information about Greta Thunberg.")
