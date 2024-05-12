import streamlit as st
from streamlit.components.v1 import html

from streamlit_gtag import st_gtag

st.set_page_config(
    page_title="Google Gtag",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Activate session state

# Initialize session state
if 'cookie' not in st.session_state:
    st.session_state['cookie'] = 'false'


def cookie_banner():
    if st.session_state['cookie'] == 'false':
        placeholder = st.empty()

        # Define the cookie banner layout
        col0, col1, col2, col3, col4 = placeholder.columns([5, 2.5, 0.5, 0.5, 5])

        # Display cookie message in the first column
        col1.write("We use cookies to improve your experience on our website.")

        # If "Accept" button is clicked, set session state to 'true'
        if col2.button("Accept", type='primary'):
            st.session_state['cookie'] = 'true'
            st_gtag(
                key="gtag_send_event_b",
                id="G-8H46WZXW14",
                event_name="send_event_button",
                params={
                    "event_category": "test_category_b",
                    "event_label": "test_label_b",
                    "value": 97,
                }
            )

        # If "Reject" button is clicked, set session state to 'true'
        if col3.button("Reject"):
            st.session_state['cookie'] = 'true'

        # If either "Accept" or "Reject" button is clicked, remove the cookie banner
        if st.session_state['cookie'] == 'true':
            placeholder.empty()


cookie_banner()
st.title("Google Analytics:chart:")
