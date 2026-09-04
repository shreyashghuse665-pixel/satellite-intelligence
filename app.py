import streamlit as st

st.set_page_config(
    page_title="Satellite Intelligence",
    page_icon="🛰️",
    layout="wide"
)

st.title("🛰️ Satellite Intelligence")
st.write("Evidence-Verified Multimodal Satellite Analysis")

uploaded_file = st.file_uploader(
    "Upload a satellite image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    st.image(
        uploaded_file,
        caption="Uploaded Satellite Image",
        use_container_width=True
    )

    st.success("Image uploaded successfully! 🎉")
