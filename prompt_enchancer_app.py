import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# Load API key
with open('.openai') as f:
    os.environ['OPENAI_API_KEY'] = f.read().strip()

# Initialize model
model = ChatOpenAI(model="gpt-4o-mini")

# Prompt Enhancer System Message
PROMPT_ENHANCER_SYSTEM = """Act as a Prompt Enhancer AI that takes user-input prompts and transforms them into more engaging, detailed, and thought-provoking questions. 

IMPORTANT: Only return the enhanced prompt itself. Do not include any explanations, process descriptions, or examples. Just output the enhanced version of the user's prompt."""

def enhance_prompt(user_prompt):
    """Enhance a user's prompt using the Prompt Enhancer AI"""
    template = ChatPromptTemplate.from_messages([
        ("system", PROMPT_ENHANCER_SYSTEM),
        ("user", user_prompt)
    ])
    
    messages = template.format_messages()
    response = model.invoke(messages)
    return response.content.strip()

# Streamlit UI
st.set_page_config(page_title="Prompt Enhancer", page_icon="✨")
st.title("✨ Prompt Enhancer AI")
st.markdown("Transform your prompts into more engaging, detailed, and thought-provoking questions!")

# User input
user_input = st.text_area(
    "Enter your prompt:",
    placeholder="e.g., 'Tell me about climate change'",
    height=100
)

if st.button("Enhance Prompt", type="primary"):
    if user_input.strip():
        with st.spinner("Enhancing your prompt..."):
            enhanced = enhance_prompt(user_input)
            st.text_area("Enhanced Prompt:", value=enhanced, height=300, key="enhanced_output")
            st.download_button(
                label="Download Enhanced Prompt",
                data=enhanced,
                file_name="enhanced_prompt.txt",
                mime="text/plain"
            )
    else:
        st.warning("Please enter a prompt to enhance.")