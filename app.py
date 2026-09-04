import streamlit as st

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------
st.set_page_config(
    page_title="Satellite Intelligence",
    page_icon="🛰️",
    layout="wide"
)

# -----------------------------
# TITLE
# -----------------------------
st.title("🛰️ Satellite Intelligence")
st.write("Evidence-Verified Multimodal Satellite Analysis")

st.divider()

# -----------------------------
# IMAGE UPLOAD
# -----------------------------
st.subheader("📤 Upload Satellite Image")

uploaded_file = st.file_uploader(
    "Choose a satellite image",
    type=["jpg", "jpeg", "png"]
)

# -----------------------------
# IMAGE + QUESTION
# -----------------------------
if uploaded_file is not None:

    col1, col2 = st.columns(2)

    # LEFT SIDE — IMAGE
    with col1:
        st.subheader("🖼️ Satellite Image")

        st.image(
            uploaded_file,
            caption="Uploaded Satellite Image",
            use_container_width=True
        )

    # RIGHT SIDE — QUESTION
    with col2:
        st.subheader("💬 Ask a Question")

        question = st.text_area(
            "What would you like to know about this image?",
            placeholder="Example: What is visible in this satellite image?"
        )

        analyze_button = st.button(
            "🔍 Analyze Image",
            use_container_width=True
        )

    # -----------------------------
    # ANALYSIS RESULT
    # -----------------------------
    if analyze_button:

        if question.strip() == "":
            st.warning("⚠️ Please enter a question first.")

        else:
            st.divider()

            st.subheader("🤖 AI Analysis")

            st.info(
                "AI analysis will appear here. "
                "We will connect the real satellite AI model in the next step."
            )

            # -----------------------------
            # CONFIDENCE
            # -----------------------------
            st.subheader("📊 Confidence")

            st.progress(0.75)
            st.write("Confidence: 75%")

            # -----------------------------
            # EVIDENCE
            # -----------------------------
            st.subheader("🔎 Evidence")

            st.write(
                "Evidence collected from specialist satellite-analysis models "
                "will appear here."
            )

            # -----------------------------
            # EXECUTION TRACE
            # -----------------------------
            st.subheader("🧠 Execution Trace")

            st.write("1. Image received ✅")
            st.write("2. User question received ✅")
            st.write("3. Router selected → Waiting for AI model")
            st.write("4. Evidence verification → Waiting")
            st.write("5. Final answer → Waiting")
