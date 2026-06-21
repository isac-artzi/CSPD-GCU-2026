import os

import anthropic
import streamlit as st

# Load variables from a local .env file (if present) into the environment.
# This is only used when running locally — on Streamlit Cloud you use Secrets.
# If python-dotenv isn't installed, we silently skip it.
try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

# The model used by all three tools. Kept in one place so it's easy to change.
# Note: the workshop guide references "claude-sonnet-4-20250514", which was
# retired on 2026-06-15. "claude-sonnet-4-6" is its drop-in replacement.
MODEL = "claude-sonnet-4-6"


def _get_client():
    """
    Create the Anthropic client.

    The API key is read from Streamlit's secrets (when deployed on Streamlit
    Cloud) or from the ANTHROPIC_API_KEY environment variable (when running
    locally). This lets the same code work in both places.
    """
    try:
        api_key = st.secrets.get("ANTHROPIC_API_KEY", None)
        if api_key:
            return anthropic.Anthropic(api_key=api_key)
    except Exception:
        # st.secrets may not exist when running outside Streamlit; fall through.
        pass
    return anthropic.Anthropic()  # reads from the environment variable


def get_ai_response(system_prompt: str, user_message: str) -> str:
    """
    Send a single message to Claude and get a response.

    Parameters:
        system_prompt (str): Instructions that tell Claude how to behave
        user_message (str): The actual message/question to send

    Returns:
        str: Claude's response text, or None if the call failed
    """
    client = _get_client()

    try:
        # ── TODO 1 (completed): Call the Claude API ──
        response = client.messages.create(
            model=MODEL,
            max_tokens=2048,
            system=system_prompt,
            messages=[{"role": "user", "content": user_message}],
        )
        # Return just the text from Claude's response
        return response.content[0].text
    except Exception as e:
        # Show a friendly error in the app instead of crashing.
        st.error(f"AI request failed: {e}")
        return None


def get_chat_response(system_prompt: str, messages: list) -> str:
    """
    Send a conversation (multiple messages) to Claude and get a response.
    Used for the Socratic Tutor's back-and-forth conversation.

    Parameters:
        system_prompt (str): Instructions that tell Claude how to behave
        messages (list): List of message dicts like
            [{"role": "user", "content": "..."},
             {"role": "assistant", "content": "..."}]

    Returns:
        str: Claude's response text, or None if the call failed
    """
    client = _get_client()

    try:
        # ── TODO 2 (completed): Call the Claude API with the full conversation ──
        response = client.messages.create(
            model=MODEL,
            max_tokens=2048,
            system=system_prompt,
            messages=messages,
        )
        # Return just the text from Claude's response
        return response.content[0].text
    except Exception as e:
        st.error(f"AI request failed: {e}")
        return None
