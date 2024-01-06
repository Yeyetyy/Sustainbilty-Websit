import streamlit as st

# Set page title and favicon
st.set_page_config(
    page_title="Green Initiatives",
    page_icon="🌿",
    layout="centered",
)

st.sidebar.success("Choose a page.")

# List of green initiatives/projects with additional information
projects = [
    {
        "name": "Solar Energy Expansion",
        "description": "With a focus on solar power projects in Europe, Australia, and America, RWE is leading the charge in the swift growth of renewable energies. RWE is investing up to 15 billion euros in green projects in Germany as part of its active participation in the energy transition. The company is particularly focused on opencast mining regions such as the Rhenish coalfield. RWE is leading the way in solar solutions here, in addition to wind farms. One such system is a photovoltaic system with battery storage that will be installed in the future shore area of the Hambach opencast mining lake. The organization demonstrates its commitment to innovation and sustainable energy practices by going above and beyond standard projects to conduct state-of-the-art research in technologies such as Agri PV and Floating PV. With more than 20 years of experience in the industry, RWE is transforming the energy environment and advancing solar technology through these initiatives.",
        "image_url": "https://www.rwe.com/-/media/RWE/images/11-forschung-und-entwicklung/solar-projekte/OG-solar-projekte.jpg",
        "details_url": "https://www.rwe.com/en/research-and-development/solar-energy-projects/",
    },
    {
        "name": "Tree Planting Campaign",
        "description": "In response to the urgent global need for environmental conservation, the Trees Campaign, in collaboration with influential figures such as MrBeast, has planted an astounding 20 million trees. This ambitious initiative seeks to address the pressing issues of deforestation and climate change by harnessing the collective power of individuals and communities worldwide. Aligned with MrBeast's vision, the campaign underscores the transformative impact that afforestation can have on the planet. The goal extends beyond the mere act of planting trees; it represents a united effort to restore ecosystems, enhance biodiversity, and combat the escalating challenges posed by climate change. By mobilizing a diverse and widespread community, the Trees Campaign aspires to leave an indelible mark on the environment, symbolizing the potential for positive change when people come together for a shared cause. Through this collective endeavor, the campaign strives to inspire a global movement committed to nurturing the Earth and securing a sustainable future for generations to come.",
        "image_url": "https://i.insider.com/5db9ceeadee0192a660a4355?width=1200&format=jpeg",
        "details_url": "https://teamtrees.org/",
    },
    {
        "name": "Waste Recycling Program",
        "description": "Undertaking a crucial task to tackle the growing issue of ocean pollution, the Ocean Cleanup Program—exemplified by programs such as Team Seas—is committed to removing an incredible 30 million pounds of waste from aquatic environments. With the world struggling to address the damaging effects of plastic and waste on marine ecosystems, this coordinated effort serves as an opportunity for revolutionary change and a ray of hope. Team Seas and the Ocean Cleanup Program use creativity and teamwork to address one of the most important environmental issues of our day by dedicating their all to cleaning up contaminated rivers and waterways. The effort aims to protect marine life, maintain biodiversity, and promote a sustainable balance between humans and the seas in addition to creating cleaner oceans. Team Seas is a prime example of the potential of group action in establishing a cleaner, healthier, and more resilient marine environment for the benefit of current and future generations. It does this by mobilizing support around the world and allocating funds to extensive cleanup operations.",
        "image_url": "https://assets.theoceancleanup.com/scaled/1200x675/app/uploads/2020/01/1911-The-Ocean-Cleanup-BoyaninAsia-DvdK-1111502-scaled.jpg",
        "details_url": "https://theoceancleanup.com/",
    },
    # Add more projects as needed
]

# Display introductory text
st.write("""
# Green Initiatives and Projects 🌿

Explore various initiatives and projects dedicated to promoting sustainability and environmental conservation.

""")

# Display information about each project
for project in projects:
    # Display project name as header
    st.write(f"## {project['name']}")

    # Display project description
    st.write(project["description"])

    # Display project image
    st.image(project["image_url"], caption=f"{project['name']} Project Image", use_column_width=True)

    # Provide a link to more details about the project
    st.write(f"Learn more about this project [here]({project['details_url']})")

    # Add a horizontal rule for visual separation
    st.markdown("---")

