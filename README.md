# AI Infrastructure Auditor 🛡️

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

**A professional, passive security configuration auditor for your local and cloud AI infrastructure.**

The AI Infrastructure Auditor is a lightweight, Streamlit-based application designed to help developers and security engineers quickly identify common misconfigurations and security vulnerabilities in their AI environments. By simply pasting your configuration files, `.env` files, or deployment scripts, the auditor analyzes the text to flag critical risks before they reach production.

---

## 🎯 Key Features

- **Passive Analysis:** Scans configuration text statically without executing any code or connecting to your live infrastructure.
- **Exposed Interface Detection:** Identifies critical misconfigurations, such as binding local LLM servers (like Ollama) to all public interfaces (`0.0.0.0`) without proper authentication.
- **Credential Scanning:** Detects hardcoded plaintext secrets, such as OpenAI API keys, to prevent accidental credential leakage.
- **Clear Remediation Advice:** Provides immediate, actionable guidance on how to fix detected vulnerabilities.
- **Professional Interface:** Built with a clean, minimalist design tailored for enterprise usage.

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3.8 or higher installed on your machine.

### Local Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/shirdon-tech/ai-security-auditor.git
   cd ai-security-auditor
   ```

2. **Install dependencies:**
   It is recommended to use a virtual environment.
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   streamlit run app.py
   ```

4. **Access the Dashboard:**
   Open your browser and navigate to `http://localhost:8501`.

## 🛠️ Usage

1. Open the application.
2. Paste the contents of your configuration file, `docker-compose.yml`, environment variables, or setup scripts into the text area.
3. Click **"Analyze Configuration"**.
4. Review the audit results. High-risk issues will be highlighted in red with detailed remediation steps.

## 🔒 Security & Privacy

This application runs entirely in your local environment. It does **not** send your configuration text, API keys, or infrastructure details to any external third-party servers for analysis. All regular expression checks are performed locally within the Python runtime.

## 🤝 Contributing

Contributions are welcome! If you have ideas for new security checks, better regex patterns, or UI improvements, please feel free to open an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-security-check`).
3. Commit your changes (`git commit -m 'Add check for exposed vector databases'`).
4. Push to the branch (`git push origin feature/new-security-check`).
5. Open a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
