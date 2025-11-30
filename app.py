import streamlit as st
import pandas as pd
import json
import os
from llm_engine import LLMEngine

# --- CONFIGURATION & STATE ---
st.set_page_config(page_title="Email Productivity Agent", layout="wide")
llm = LLMEngine()

# Initialize Session State
if 'emails' not in st.session_state:
    with open('mock_data.json', 'r') as f:
        st.session_state.emails = json.load(f)

# Default Prompts [cite: 61]
if 'prompts' not in st.session_state:
    st.session_state.prompts = {
        "categorization": "Categorize emails into: Important, Newsletter, Spam, To-Do. To-Do emails must include a direct request requiring user action.",
        "action_item": "Extract tasks from the email. Respond in JSON: { 'task': '...', 'deadline': '...' }.",
        "auto_reply": "If an email is a meeting request, draft a polite reply asking for an agenda."
    }

if 'processed_data' not in st.session_state:
    st.session_state.processed_data = {} # Stores categories/actions by Email ID

if 'drafts' not in st.session_state:
    st.session_state.drafts = []

# --- SIDEBAR: NAVIGATION ---
st.sidebar.title("📧 Agent Controls")
page = st.sidebar.radio("Go to", ["Dashboard & Inbox", "Prompt Brain", "Email Agent Chat", "Drafts"])

# --- PAGE 1: DASHBOARD & INBOX [cite: 75] ---
if page == "Dashboard & Inbox":
    st.title("📥 Inbox Ingestion & Status")

    # Ingestion Controls
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Process Inbox (Run Agent)"):
            with st.spinner("Agent is reading emails, applying prompts..."):
                for email in st.session_state.emails:
                    e_id = email['id']
                    body = email['body']
                    
                    # 1. Run Categorization
                    cat = llm.process_with_llm(st.session_state.prompts['categorization'], body)
                    
                    # 2. Run Action Item Extraction
                    action = llm.process_with_llm(st.session_state.prompts['action_item'], body)
                    
                    st.session_state.processed_data[e_id] = {
                        "category": cat,
                        "action": action
                    }
            st.success("Inbox Processed Successfully!")

    # Inbox Viewer [cite: 81]
    st.subheader("Email List")
    
    # Convert to DataFrame for nicer display
    display_data = []
    for email in st.session_state.emails:
        meta = st.session_state.processed_data.get(email['id'], {"category": "Unprocessed", "action": "-"})
        display_data.append({
            "ID": email['id'],
            "Sender": email['sender'],
            "Subject": email['subject'],
            "Category": meta['category'], # [cite: 89]
            "Action Item": meta['action']
        })
    
    df = pd.DataFrame(display_data)
    st.dataframe(df, use_container_width=True)

# --- PAGE 2: PROMPT BRAIN [cite: 90] ---
elif page == "Prompt Brain":
    st.title("🧠 Agent Brain (Prompt Configuration)")
    st.write("Customize how the agent behaves by editing these system prompts.")

    with st.form("prompt_form"):
        st.subheader("1. Categorization Prompt")
        new_cat = st.text_area("Rules for sorting emails:", st.session_state.prompts['categorization'], height=100)
        
        st.subheader("2. Action Extraction Prompt")
        new_act = st.text_area("Rules for finding tasks:", st.session_state.prompts['action_item'], height=100)
        
        st.subheader("3. Auto-Reply Tone/Style")
        new_reply = st.text_area("Rules for drafting replies:", st.session_state.prompts['auto_reply'], height=100)
        
        if st.form_submit_button("Save Configuration"):
            st.session_state.prompts['categorization'] = new_cat
            st.session_state.prompts['action_item'] = new_act
            st.session_state.prompts['auto_reply'] = new_reply
            st.success("Agent behavior updated!")

# --- PAGE 3: EMAIL AGENT CHAT [cite: 107] ---
elif page == "Email Agent Chat":
    st.title("🤖 Email Agent")
    
    # Select an email to discuss
    email_options = {f"{e['id']} - {e['subject']}": e for e in st.session_state.emails}
    selected_option = st.selectbox("Select an email to discuss:", list(email_options.keys()))
    selected_email = email_options[selected_option]

    # Display Email Content
    with st.expander("View Email Content", expanded=True):
        st.write(f"**From:** {selected_email['sender']}")
        st.write(f"**Subject:** {selected_email['subject']}")
        st.info(selected_email['body'])

    # Chat Interface
    user_query = st.text_input("Ask the agent about this email:", placeholder="e.g., Summarize this, Draft a reply...")
    
    if st.button("Ask Agent"):
        if user_query:
            # Combine email content + user query + relevant prompt logic
            response = llm.process_with_llm(st.session_state.prompts['auto_reply'], selected_email['body'], user_query)
            st.chat_message("assistant").write(response)
            
            # If the user asked for a draft, give option to save it
            if "draft" in user_query.lower() or "reply" in user_query.lower():
                if st.button("Save as Draft"):
                    st.session_state.drafts.append({
                        "original_id": selected_email['id'],
                        "content": response
                    })
                    st.success("Draft saved to Drafts folder!")

# --- PAGE 4: DRAFTS [cite: 133] ---
elif page == "Drafts":
    st.title("📝 Generated Drafts")
    st.write("Review drafts before sending. The agent NEVER sends emails automatically. ")

    if not st.session_state.drafts:
        st.info("No drafts generated yet. Go to the Chat to generate one.")
    
    for i, draft in enumerate(st.session_state.drafts):
        with st.container():
            st.subheader(f"Draft #{i+1} (for Email ID {draft['original_id']})")
            edited_draft = st.text_area("Edit Draft:", draft['content'], key=f"draft_{i}", height=200)
            
            col1, col2 = st.columns([1, 4])
            with col1:
                if st.button("🗑️ Discard", key=f"del_{i}"):
                    st.session_state.drafts.pop(i)
                    st.rerun()
            with col2:
                if st.button("📨 Simulate Send", key=f"send_{i}"):
                    st.success(f"Email sent successfully! (Simulation)")
                    st.session_state.drafts.pop(i)
                    st.rerun()
            st.divider()
