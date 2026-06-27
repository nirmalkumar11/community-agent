import streamlit as st
from adk.orchestrator import run
import traceback

st.set_page_config(
    page_title="ClubMind AI",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 ClubMind AI")
st.caption(
    "Agentic Intelligence System for Member Discovery and Leadership Recommendation"
)

query = st.text_input(
    "Ask a question",
    placeholder="Who should lead the AI Workshop?"
)

# if st.button("Get Recommendation"):
#     with st.spinner("Analyzing members..."):
#         result = run(query)



if st.button("Submit"):
    try:
        print("User Query:", query)

        result = run(query)

        print("Workflow Finished")

        st.write(result)

    except Exception as e:
        print("ERROR OCCURRED")
        print(traceback.format_exc())

        st.error(str(e))
        st.code(traceback.format_exc())

    st.success("Recommendation Generated")
    st.markdown(result)
