import streamlit as st
from streamlit.report_thread import get_report_ctx
from streamlit.server.server import Server

class SessionState:
    def __init__(self, session, **kwargs):
        self.session = session
        self._state = {}
        self._state.update(**kwargs)

def get_session():
    ctx = get_report_ctx()
    session_id = ctx.session_id
    session = None
    current_server = Server.get_current()
    if current_server:
        session = current_server._get_session_info(session_id)
    return session

def get_state():
    session = get_session()
    if session:
        if not hasattr(session, "_custom_session_state"):
            session._custom_session_state = SessionState(session)
        return session._custom_session_state

# Set page title and favicon
st.set_page_config(
    page_title="Button Toggle Example",
    layout="centered",
)

state = get_state()

st.title("Famous Environmentalist ")

# The image that pops up onto the screen
st.image('streamlit-multipage-app-example-master/Greta_Thunberg_02_cropped.jpg', caption="Greta Thunberg")

# Text about the person
click_button = st.button("Reveal Info About Greta Thunberg")

# Check if the button is clicked
if click_button:
    state.show_text = not getattr(state, "show_text", False)

# Display information based on button state
if getattr(state, "show_text", False):
    st.title("About")
    st.text("Born: January 3, 2003 (age 20 years), Stockholm, Sweden")
    st.text("Parents: Svante Thunberg, Malena Ernman")
    st.text("Height: 1.49 m")
    st.text("Movement: School Strike for Climate")
    st.write("Awards List [link](https://en.wikipedia.org/wiki/Greta_Thunberg#Honours_and_awards:~:text=COVID%2D19%20pandemic.-,Honours%20and%20awards,doctorate%20was%20scheduled%20to%20be%20granted%20in%20June%202023.%5B301%5D,-Species%20named%20in)")
    st.sidebar.success("Choose a page.")
else:
    st.info("Click the button to reveal information about Greta Thunberg.")
