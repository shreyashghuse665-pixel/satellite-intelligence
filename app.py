import streamlit as st
from huggingface_hub import InferenceClient

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
# HUGGING FACE CLIENT
# -----------------------------
client = InferenceClient(
    api_key=st.secrets["HF_TOKEN"],
    provider="featherless-ai"
)

MODEL = "Qwen/Qwen2.5-VL-3B-Instruct"

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

    with col1:
        st.subheader("🖼️ Satellite Image")

        st.image(
            uploaded_file,
            caption="Uploaded Image",
            use_container_width=True
        )

    with col2:
        st.subheader("💬 Ask a Question")

        question = st.text_area(
            "What would you like to know about this image?",
            placeholder="Example: What is visible in this image?"
        )

        analyze_button = st.button(
            "🔍 Analyze Image",
            use_container_width=True
        )

    # -----------------------------
    # REAL AI ANALYSIS
    # -----------------------------
    if analyze_button:

        if question.strip() == "":
            st.warning("⚠️ Please enter a question first.")

        else:

            with st.spinner("🧠 AI is analyzing the image..."):

                try:

                    image_bytes = uploaded_file.getvalue()

                    import base64

image_base64 = base64.b64encode(image_bytes).decode("utf-8")

messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{image_base64}"
                }
            },
            {
                "type": "text",
                "text": question
            }
        ]
    }
]

                    response = client.chat.completions.create(
                        model=MODEL,
                        messages=messages,
                        max_tokens=300
                    )

                    answer = response.choices[0].message.content

                    # -----------------------------
                    # ANSWER
                    # -----------------------------
                    st.divider()

                    st.subheader("🤖 AI Analysis")

                    st.write(answer)

                    # -----------------------------
                    # CURRENT STATUS
                    # -----------------------------
                    st.subheader("📊 Confidence")

                    st.info(
                        "Confidence verification will be added "
                        "after we integrate the specialist models."
                    )

                    st.subheader("🔎 Evidence")

                    st.info(
                        "Independent evidence models will be added next."
                    )

                    # -----------------------------
                    # EXECUTION TRACE
                    # -----------------------------
                    st.subheader("🧠 Execution Trace")

                    st.write("1. Image received ✅")
                    st.write("2. User question received ✅")
                    st.write("3. VLM analysis completed ✅")
                    st.write("4. Evidence verification → Coming next")
                    st.write("5. Final verified answer → Coming next")

                except Exception as e:

                    st.error(
                        "❌ Something went wrong while calling the AI model."
                    )

                    st.code(str(e))
