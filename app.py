import streamlit as st
import re

st.title("AI Infrastructure Auditor")
st.subheader("Analyze configuration files for security misconfigurations.")

st.markdown("""
Paste your environment variables or configuration text below to check for potential security risks.
""")

config_text = st.text_area("Configuration Text", height=300)

if st.button("Analyze Configuration"):
    if config_text:
        st.write("### Audit Results")
        
        flags = []
        
        # Check 1: Exposed Ollama Interface
        if re.search(r"OLLAMA_HOST\s*=\s*[\"']?0\.0\.0\.0[\"']?", config_text):
            flags.append({
                "severity": "High Risk",
                "issue": "Exposed to Public Interfaces",
                "details": "OLLAMA_HOST is set to 0.0.0.0. This binds the Ollama API to all network interfaces, potentially exposing it to the public internet.",
                "remediation": "Change OLLAMA_HOST to 127.0.0.1 to bind only to localhost, or ensure a reverse proxy with robust authentication is in place."
            })
            
        # Check 2: Plaintext OpenAI API Key
        # Matches typical sk-... keys
        if re.search(r"OPENAI_API_KEY\s*=\s*[\"']?sk-[a-zA-Z0-9]+[\"']?", config_text):
             flags.append({
                "severity": "High Risk",
                "issue": "Plaintext API Key",
                "details": "A plaintext OPENAI_API_KEY was found in the configuration.",
                "remediation": "Do not store sensitive API keys in plain text. Use a secure secret manager or inject them securely at runtime."
            })

        if not flags:
            st.success("No known misconfigurations detected in the provided text.")
        else:
            for flag in flags:
                st.error(f"**{flag['severity']}: {flag['issue']}**\n\n{flag['details']}\n\n**Remediation:** {flag['remediation']}")
    else:
        st.warning("Please provide configuration text to analyze.")
