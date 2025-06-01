import streamlit as st
import requests

# Streamlit app UI
st.set_page_config(page_title="SpecGPT Agent 🧠", layout="centered")
st.title("💬 SpecGPT via OpenRouter")

# User input
user_input = st.text_input("Ask something:")

# Secret sauce — your OpenRouter API Key
#OPENROUTER_API_KEY = "org-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # Replace this!
OPENROUTER_API_KEY = "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"

# Chat history (to keep conversation context)
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Make the API call if user submits a question
if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    with st.spinner("Thinking..."):
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "HTTP-Referer": "http://localhost",  # Required header
                "X-Title": "SpecGPT-Streamlit"
            },
            json={
                "model": "openai/gpt-3.5-turbo",  # You can change this to gpt-4o or Claude, etc.
                "messages": st.session_state.chat_history
            }
        )

        result = response.json()
        #reply = result["choices"][0]["message"]["content"]
        if "choices" in result:
            reply = result["choices"][0]["message"]["content"]
        else:
            st.error("❌ OpenRouter API Error:\n" + result.get("error", {}).get("message", "Unknown error."))
            reply = "Sorry, something went wrong with the response."

            
        st.session_state.chat_history.append({"role": "assistant", "content": reply})

# Display chat history
for msg in st.session_state.chat_history:
    if msg["role"] == "user":
        st.markdown(f"🧑‍💻 **You:** {msg['content']}")
    else:
        st.markdown(f"🤖 **Agent:** {msg['content']}")
