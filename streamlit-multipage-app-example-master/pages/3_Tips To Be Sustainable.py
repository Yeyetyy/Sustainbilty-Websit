import streamlit as st

# Set page title and favicon
st.set_page_config(
    page_title="Sustainability Tips",
    page_icon="🌱",
    layout="centered",
)
st.sidebar.success("Choose a page.")

# New Lottie Gif URL for all tips
new_gif_url1 = "https://lottie.host/48a34669-981e-402a-addc-d99b545ca398/U1ZCuLozxm.json"
new_gif_url2 = "https://lottie.host/1eefdb7c-93c5-437e-82d9-ea29772c68ec/Y4JS4nXquw.json"
new_gif_url3 = "https://lottie.host/731b7c33-2ef1-451e-81f0-22c1614147b9/3POUfLYCrs.json"
new_gif_url4 = "https://lottie.host/e33315d8-2f42-4380-8f1a-1cf325fbc058/i7ryVSM0FK.json"
new_gif_url5 = "https://lottie.host/cf5da9df-a830-4343-8088-8e520edd9921/hB4MGsd24R.json"
new_gif_url6 = "https://lottie.host/bb35f332-b657-4a22-a9f6-a0354e265326/WNjCxa40XF.json"
new_gif_url7 = "https://lottie.host/60b29ca2-0eaa-49ee-8acf-ee2bbabf8054/gxt7HhWkhf.json"
new_gif_url8 = "https://lottie.host/9e5e131a-e1f8-469c-9886-c8fa14151d67/wfkK2pCnmM.json"
new_gif_url9 = "https://lottie.host/543d1da7-d053-4b94-8e44-d4a0722911b1/PexoWuB0Qm.json"



# List of sustainability tips with additional information
tips = [
    {
        "title": "Reduce, Reuse, Recycle!",
        "text": "One of the most effective ways to minimize your environmental impact is to follow the mantra: reduce, reuse, and recycle. Be mindful of your consumption, find creative ways to reuse items, and recycle materials whenever possible.",
        "gif_url": new_gif_url1,
    },
    {
        "title": "Think Twice Before Shopping",
        "text": "Before making a purchase, consider whether you really need the item. Avoid impulse buying and choose products with minimal packaging to reduce waste.",
        "gif_url": new_gif_url2,
    },
    {
        "title": "Conserve Water",
        "text": "Water is a precious resource, and conserving it is essential. Fix leaks promptly, use water-efficient appliances, and adopt water-saving habits such as turning off the tap while brushing your teeth.",
        "gif_url": new_gif_url3,
    },
    {
        "title": "Ditch Plastic and Switch to Reuse",
        "text": "Reduce your reliance on single-use plastics. Opt for reusable alternatives such as water bottles, bags, and containers. Every small change adds up!",
        "gif_url": new_gif_url4,
    },
    {
        "title": "Take Extinction Off Your Plate",
        "text": "Consider adopting a plant-based diet or reducing your meat consumption. Sustainable food choices can help protect biodiversity and reduce your carbon footprint.",
        "gif_url": new_gif_url5,
    },
    {
        "title": "Simplify the Holidays",
        "text": "Celebrate the holidays with a focus on meaningful experiences rather than excessive consumption. Choose sustainable gifts, decorations, and wrapping materials.",
        "gif_url": new_gif_url6,
    },
    {
        "title": "Choose Organic",
        "text": "Support organic agriculture, which avoids synthetic pesticides and fertilizers. Organic farming promotes healthier ecosystems, soil, and water quality.",
        "gif_url": new_gif_url7,
    },
    {
        "title": "Ditch Fast Fashion and Animal-Based Textiles",
        "text": "Fast fashion has a significant environmental impact. Choose quality, timeless clothing and explore sustainable, cruelty-free alternatives to animal-based textiles, (foxes are the most used animal for clothing).",
        "gif_url": new_gif_url8,
    },
    {
        "title": "Drive Less, Drive Green",
        "text": "Reduce your carbon footprint by using public transportation, carpooling, biking, or walking. Consider eco-friendly vehicles if possible.",
        "gif_url": new_gif_url9,
    },
    # Add more tips as needed
]

# Display introductory text
st.write("""
# Welcome to the Sustainability Tips Page! 🌍

Explore these practical tips to lead a more sustainable and eco-friendly lifestyle. Each tip is accompanied by information and a Lottie animation to make learning fun!

""")

# Iterate over the tips list with an index using enumerate
for i, tip in enumerate(tips):
    # Check if the index is even or odd to determine column placement
    col = st.columns(2) if i % 2 == 0 else st.columns(2)[::-1]

    # Display tip text in the first column of the current pair
    col[0].write(f"## {tip['title']}")
    col[0].write(tip["text"])

    with col[1]:
    # Display Lottie Gif
        st.lottie(tip["gif_url"], speed=1, width=300, height=200)

# Add more content or tips as needed

video_file = open('streamlit-multipage-app-example-master/Sustainability in everyday life _ Sustainability.mp4', 'rb')
st.video(video_file)
st.subheader('[(ACCIONA)](https://www.youtube.com/watch?v=kZIrIQDf1nQ)')


