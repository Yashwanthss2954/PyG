# from pygwalker.api.streamlit import StreamlitRenderer
# import pandas as pd
# import streamlit as st

# # Adjust the width of the Streamlit page
# st.set_page_config(
#     page_title="Use Pygwalker In Streamlit",
#     layout="wide"
# )

# # Add Title
# st.title("Use Pygwalker In Streamlit")


# st.subheader("Upload a CSV File")
# uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

# # You should cache your pygwalker renderer, if you don't want your memory to explode
# @st.cache_resource
# def get_pyg_renderer() -> "StreamlitRenderer":
#     df = pd.read_csv(uploaded_file)
#     # If you want to use feature of saving chart config, set spec_io_mode="rw"
    
#     return StreamlitRenderer(df, spec="./gw_config.json", spec_io_mode="rw")


# renderer = get_pyg_renderer()

# renderer.explorer()


from pygwalker.api.streamlit import StreamlitRenderer
import pandas as pd
import streamlit as st
import os

# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="Use Pygwalker In Streamlit",
    layout="wide"
)

# Add Title
st.title("Use Pygwalker In Streamlit")

st.subheader("Upload a CSV File")
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

@st.cache_resource
def get_pyg_renderer(csv_path: str) -> "StreamlitRenderer":
    df = pd.read_csv(csv_path)
    return StreamlitRenderer(df, spec="./gw_config.json", spec_io_mode="rw")

# Handle file saving and rendering
if uploaded_file is not None:
    # Save the uploaded file to the parent directory
    save_path = os.path.join(os.path.dirname(__file__), uploaded_file.name)
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Create and show the Pygwalker renderer
    renderer = get_pyg_renderer(save_path)
    renderer.explorer()
