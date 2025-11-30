import json
import os
# from openai import OpenAI # Uncomment if you have a real key

class LLMEngine:
    def __init__(self):
        # Initialize your API client here if using real AI
        # self.client = OpenAI(api_key="YOUR_KEY_HERE")
        pass

    def process_with_llm(self, prompt_template, email_content, user_query=""):
        """
        Simulates the LLM processing.
        In a real scenario, this sends the request to OpenAI/Groq.
        """
        full_prompt = f"{prompt_template}\n\nEmail Content:\n{email_content}\n\nUser Instruction:\n{user_query}"
        
        # --- MOCK LOGIC FOR DEMO PURPOSES (To save API costs) ---
        # This ensures the assignment works "out of the box"
        
        # Categorization Logic
        if "Categorize emails" in prompt_template:
            content_lower = email_content.lower()
            if "lottery" in content_lower or "scam" in content_lower:
                return "Spam"
            elif "newsletter" in content_lower or "invitation" in content_lower:
                return "Newsletter"
            elif "urgent" in content_lower or "due" in content_lower:
                return "Important"
            elif "review" in content_lower or "meeting" in content_lower:
                return "To-Do"
            else:
                return "General"

        # Action Item Extraction Logic
        elif "Extract tasks" in prompt_template:
            return json.dumps({
                "task": "Review content and take necessary action",
                "priority": "Medium"
            })

        # Auto-Reply Logic
        elif "draft a polite reply" in prompt_template:
            return f"Subject: Re: {email_content[:20]}...\n\nHi,\n\nThanks for the email. I have received your request regarding '{email_content[:30]}...' and will get back to you shortly.\n\nBest regards,\n[User Name]"
        
        # General Chat Logic
        else:
            return f"I analyzed the email. Here is the info regarding: {user_query}. Context: {email_content[:50]}..."

    def generate_draft(self, system_prompt, email_body, instructions):
        # Mock Draft generation
        return f"""Subject: Re: [Original Subject]

Dear Sender,

{instructions}

(Drafted based on context: {email_body[:30]}...)

Sincerely,
Automated Agent"""
