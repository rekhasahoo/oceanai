[cite\_start]Here is the **README.md** file, tailored specifically to meet the submission requirements outlined in the assignment[cite: 15].

You should save this content in a file named `README.md` inside your `email_agent` folder.

-----

````markdown
# Prompt-Driven Email Productivity Agent

## Overview
This application is an intelligent, prompt-driven Email Productivity Agent designed to process an inbox, categorize emails, extract action items, and draft replies using LLM logic. [cite_start]The system behavior is entirely guided by user-defined prompts ("The Agent Brain")[cite: 5, 9].

## Features
* [cite_start]**Inbox Ingestion:** Loads a mock inbox of sample emails[cite: 34].
* [cite_start]**Automated Processing:** Categorizes emails and extracts action items (JSON format) based on prompts[cite: 6, 35].
* [cite_start]**Prompt Brain:** A dedicated interface to create, edit, and save system prompts that control the agent's behavior[cite: 38, 91].
* [cite_start]**Email Agent Chat:** An interactive chat interface to summarize emails or ask specific questions about the inbox[cite: 111, 115].
* [cite_start]**Draft Generation:** Auto-drafts replies based on tone and context, stored safely for review before "sending"[cite: 36, 145].

## Prerequisites
* Python 3.8 or higher
* pip (Python package installer)

## [cite_start]Installation & Setup [cite: 16]

1.  **Clone or Download the Repository**
    Ensure all files (`app.py`, `llm_engine.py`, `mock_data.json`, `requirements.txt`) are in the same folder.

2.  **Install Dependencies**
    Open your terminal/command prompt, navigate to the project folder, and run:
    ```bash
    pip install -r requirements.txt
    ```

## [cite_start]How to Run the Application [cite: 17]

To launch the Web UI (Streamlit), run the following command in your terminal:

```bash
streamlit run app.py
````

The application will open automatically in your default web browser (usually at `http://localhost:8501`).

## Usage Guide

### [cite\_start]1. Loading the Mock Inbox [cite: 18, 54]

  * Upon launching the application, the system automatically loads the 10 sample emails provided in `mock_data.json`.
  * Navigate to the **"Dashboard & Inbox"** tab to view the raw email list.

### 2\. Processing Emails

  * In the **"Dashboard & Inbox"** tab, click the **"🔄 Process Inbox (Run Agent)"** button.
  * [cite\_start]The agent will read the active prompts and populate the "Category" and "Action Item" columns for each email[cite: 103, 104].

### [cite\_start]3. Configuring Prompts ("Prompt Brain") [cite: 19, 38]

  * Navigate to the **"Prompt Brain"** tab.
  * Here you can modify the three core prompts:
    1.  **Categorization Prompt:** Define rules for tags like "Spam", "Important", or "To-Do".
    2.  **Action Item Prompt:** Define how tasks are extracted (e.g., JSON format).
    3.  **Auto-Reply Prompt:** Define the tone and style for draft generation.
  * Click **"Save Configuration"** to update the agent's logic immediately.

### [cite\_start]4. Using the Chat Agent [cite: 31, 109]

  * Navigate to the **"Email Agent Chat"** tab.
  * Select a specific email from the dropdown menu.
  * Ask questions like:
      * *"Summarize this email."*
      * *"What is the deadline mentioned?"*
      * *"Draft a polite refusal reply."*

### [cite\_start]5. Managing Drafts [cite: 133, 146]

  * If you ask the Chat Agent to write a reply, click **"Save as Draft"**.
  * Navigate to the **"Drafts"** tab to review, edit, or delete drafts.
  * Click **"📨 Simulate Send"** to "send" the email (this removes it from the drafts list).

## [cite\_start]Project Structure [cite: 13]

```text
email_agent/
├── app.py              # Main UI application (Streamlit)
├── llm_engine.py       # Backend logic handling LLM processing (Simulated or API)
[cite_start]├── mock_data.json      # Sample inbox data [cite: 22]
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

## Configuration Notes

  * **LLM Backend:** By default, `llm_engine.py` runs in **Simulation Mode** to function without an API key for demonstration purposes. To use a real LLM (OpenAI/Groq), uncomment the API client code in `llm_engine.py` and add your `.env` file.

<!-- end list -->

```
```
