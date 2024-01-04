import streamlit as st

# Set page title and favicon
st.set_page_config(
    page_title="Sustainability Homepage",
    page_icon="🌱",
    layout="wide",
)

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

## Why Sustainability Matters

Sustainability is at the core of our values. It's not just about preserving the environment; it's about creating a better world for future generations

### Our Initiatives

- **Renewable Energy:** We harness the power of renewable sources to reduce our carbon footprint.

- **Waste Reduction:** We are dedicated to minimizing waste and promoting recycling.

- **Community Engagement:** Our team actively engages with local communities to create a positive social impact.

Feel free to contact us to learn more or get involved in our sustainability efforts!

[Contact Us](mailto:info@yourcompany.com)
""")





    #import streamlit as st

    #st.set_page_config(
    #    page_title="Sustainablity Awerness Website"
    #)

    #st.subheader("Hi Im yety")
    #st.title("A Website About Sustainability")

    #st.subheader("What Is Sustainability?")
    #st.write("The most often quoted definition comes from the UN World Commission on Environment Development: “sustainable development is development that meets the needs of the present without compromising the ability of future generations to meet their own needs.” In the charter for the UCLA Sustainability Committee, sustainability is defined as: “the integration of environmental health, social equity and economic vitality in order to create thriving, healthy, diverse and resilient communities for this generation and generations to come. The practice of sustainability recognizes how these issues are interconnected and requires a systems approach and an acknowledgement of complexity. Sustainable practices support ecological, human, and economic health and vitality. Sustainability presumes that resources are finite, and should be used conservatively and wisely with a view to long-term priorities and consequences of the ways in which resources are used. In simplest terms, sustainability is about our children and our grandchildren, and the world we will leave them.(“What Is Sustainability? | UCLA Sustainability”)")

    #st.sidebar.success("Choose a page.")