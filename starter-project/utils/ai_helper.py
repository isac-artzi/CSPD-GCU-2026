import anthropic
import streamlit as st

def get_ai_response(system_prompt: str, user_message: str) -> str:
    """
    Send a message to Claude and get a response.

    Parameters:
        system_prompt (str): Instructions that tell Claude how to behave
        user_message (str): The actual message/question to send

    Returns:
        str: Claude's response text
    """

    # Create the Anthropic client
    # The API key is read automatically from the environment variable ANTHROPIC_API_KEY
    # or from Streamlit's secrets (for deployment)
    try:
        api_key = st.secrets.get("ANTHROPIC_API_KEY", None)
        if api_key:
            client = anthropic.Anthropic(api_key=api_key)
        else:
            client = anthropic.Anthropic()  # reads from environment variable
    except Exception:
        client = anthropic.Anthropic()

    # ──────────────────────────────────────────────
    # TODO 1: Call the Claude API
    #
    # Use client.messages.create() with these parameters:
    #   - model: "claude-sonnet-4-6"
    #   - max_tokens: 2048
    #   - system: system_prompt  (the instructions)
    #   - messages: a list with one dict: {"role": "user", "content": user_message}
    #
    # Example:
    #   response = client.messages.create(
    #       model="claude-sonnet-4-6",
    #       max_tokens=2048,
    #       system=system_prompt,
    #       messages=[{"role": "user", "content": user_message}]
    #   )
    #
    # Then return the text: response.content[0].text
    # ──────────────────────────────────────────────

    pass  # ← Replace this line with your code!


def get_chat_response(system_prompt: str, messages: list) -> str:
    """
    Send a conversation (multiple messages) to Claude and get a response.
    Used for the Socratic Tutor's back-and-forth conversation.

    Parameters:
        system_prompt (str): Instructions that tell Claude how to behave
        messages (list): List of message dicts like [{"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}]

    Returns:
        str: Claude's response text
    """

    try:
        api_key = st.secrets.get("ANTHROPIC_API_KEY", None)
        if api_key:
            client = anthropic.Anthropic(api_key=api_key)
        else:
            client = anthropic.Anthropic()
    except Exception:
        client = anthropic.Anthropic()

    # ──────────────────────────────────────────────
    # TODO 2: Call the Claude API with a conversation
    #
    # This is very similar to TODO 1, but instead of a single message,
    # you pass the entire 'messages' list (which contains the full conversation history).
    #
    # Use client.messages.create() with:
    #   - model: "claude-sonnet-4-6"
    #   - max_tokens: 2048
    #   - system: system_prompt
    #   - messages: messages  (the full conversation list)
    #
    # Then return: response.content[0].text
    # ──────────────────────────────────────────────

    pass  # ← Replace this line with your code!
