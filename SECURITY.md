# Security Policy

## Supported Versions

We currently support the latest version of the project available on the `main` branch.

| Version | Supported |
| :--- | :--- |
| `main` branch | ✅ |
| Older releases | ❌ |

## Reporting a Vulnerability

We take the security of our system seriously. If you believe you have found a security vulnerability in the Multi-Agent Research System, please report it to us as soon as possible.

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report it via the "Report a vulnerability" button on the GitHub repository's Security tab, or contact the repository maintainers directly.

Please include the following details in your report:
*   Type of issue (e.g., API key exposure, dependency vulnerability, etc.)
*   Full paths of source file(s) related to the manifestation of the issue.
*   The location of the affected source code (tag/branch/commit or direct URL).
*   Any special configuration required to reproduce the issue.
*   Step-by-step instructions to reproduce the issue.
*   Impact of the issue, including how an attacker might exploit the issue.

We will acknowledge your report and aim to provide a fix or workaround as soon as possible.

## Security Best Practices

### 🔑 API Key Management

This project requires a Google Cloud API Key (`GOOGLE_API_KEY`) to function.
*   **NEVER** commit your `.env` file or your API keys to version control.
*   Ensure `.env` is listed in your `.gitignore` file.
*   If you suspect your API key has been compromised, revoke it immediately in the Google Cloud Console and generate a new one.

### 🛡️ Data Privacy

This system uses Google's Gemini API for generating content.
*   Data submitted to the agents (topics, research notes) is sent to Google's servers for processing.
*   Please review [Google's Generative AI Terms of Service](https://policies.google.com/terms) and [Privacy Policy](https://policies.google.com/privacy) to understand how your data is handled.
*   **Do not** input sensitive, confidential, or personally identifiable information (PII) into the system.

### 📦 Dependencies

We recommend regularly updating the project dependencies to ensure you have the latest security patches.

```bash
pip install --upgrade -r requirements.txt
```
