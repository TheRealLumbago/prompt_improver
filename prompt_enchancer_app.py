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
PROMPT_ENHANCER_SYSTEM = "Act as a Prompt Enhancer AI that rewrites user prompts to be clearer, more specific, and more effective while strictly preserving the original intent, user skill level, and desired outcome. If a prompt is short and task-oriented, enhance it for clarity and action; if it is reflective or exploratory, enhance it for depth and insight. Enhance prompts only as much as necessary, without introducing assumptions, advanced concepts, or reflective questions unless they are clearly implied by the original prompt. Prioritize actionability and usefulness over abstract depth, avoid unnecessary verbosity, and do not increase the prompt length by more than twice unless the original prompt is reflective or exploratory. Return only the enhanced prompt, and do not include explanations, process descriptions, or examples unless explicitly requested."

def enhance_prompt(user_prompt):
    """Enhance a user's prompt using the Prompt Enhancer AI"""
    # Ensure we're working with a fresh string copy
    prompt_text = str(user_prompt).strip()
    
    template = ChatPromptTemplate.from_messages([
        ("system", PROMPT_ENHANCER_SYSTEM),
        ("user", prompt_text)
    ])
    
    messages = template.format_messages()
    response = model.invoke(messages)
    return response.content.strip()

# Streamlit UI
st.set_page_config(page_title="Prompt Enhancer", page_icon="✨")
st.title("✨ Prompt Enhancer AI")
st.markdown("Transform your prompts into more engaging, detailed, and thought-provoking questions!")

# Initialize session state
if "enhanced_prompt" not in st.session_state:
    st.session_state.enhanced_prompt = ""

# User input - read value directly from widget
user_input = st.text_area(
    "Enter your prompt:",
    placeholder="e.g., 'how to prepare for an interview'",
    height=100
)

if st.button("Enhance Prompt", type="primary"):
    # Get the current input at the moment the button is clicked
    # Read directly from the widget - this should be the current value
    input_to_process = str(user_input).strip()
    
    if input_to_process:
        with st.spinner(f"Enhancing: '{input_to_process[:50]}{'...' if len(input_to_process) > 50 else ''}'"):
            # Call enhance with the current input
            enhanced_result = enhance_prompt(input_to_process)
            # Update session state with new result - this will trigger display update
            st.session_state.enhanced_prompt = enhanced_result
    else:
        st.warning("Please enter a prompt to enhance.")

# Display enhanced prompt outside button handler
# Don't use a key so it always updates with the latest value
if st.session_state.enhanced_prompt:
    st.text_area(
        "Enhanced Prompt:", 
        value=st.session_state.enhanced_prompt, 
        height=300
    )
    st.download_button(
        label="Download Enhanced Prompt",
        data=st.session_state.enhanced_prompt,
        file_name="enhanced_prompt.txt",
        mime="text/plain"
    )