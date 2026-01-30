# DevOps Express

**DevOps Express** is a "secure" dashboard for DevOps teams... or is it?

This application is a **VULNERABLE-BY-DESIGN** educational tool. It demonstrates
how to use the [Gemini CLI Security Extension][1] to scan for common security
issues in PRs. 

## ⚠️ WARNING
**DO NOT DEPLOY THIS APPLICATION TO A PRODUCTION ENVIRONMENT.**

## Features & Vulnerabilities

PRs proposing the following features with vulnerabilities are sent for review.
[Gemini Code Assist GitHub App][2] and a special GitHub Actions workflow
calling the Gemini CLI Security Extension catch and fix the vulnerabilities. 

1.  **Asset Downloader**: Vulnerable to **Path Traversal**.
    - *Try*: `/download?file=../../app.py`
    - Caught and fixed by Gemini Code Assit in [#4](#4).
2.  **System Diagnostics**: Vulnerable to **Information Disclosure** (Env vars).
    - *Try*: `/health`
3.  **Quick-Link Generator**: Vulnerable to **Weak Cryptography**.
    - *Try*: Predicting the token (MD5 of timestamp).
4.  **Task Runner**: Vulnerable to **Insecure Deserialization**.
    - *Try*: Uploading a malicious pickle file.
5.  **Report Generator**: Vulnerable to **Vulnerable Dependency** (PyYAML 5.3).
    - *Try*: Uploading a YAML payload with `!!python/object/apply`.

## Configure GitHub Actions Workflow

To securely configure auth for Gemini CLI invoked from GitHub Actions workflows,
you should set up Workload Identify Federation.

From your local terminal, run the following commands:

1. Sign into GitHub. 
   ```bash
   gh auth login
   ```
1. Authenticate with Google Cloud.
   ```bash
   gcloud init
   ```
   You need to use an account that have at least the following IAM roles in a
   Google Cloud project:
   1. `roles/serviceusage.serviceUsageAdmin` - ability to enable and disable
   services
   1. `roles/iam.workloadIdentityPoolAdmin` - ability to create Workload
   Identity Pools and Providers
   1. `roles/iam.serviceAccountAdmin` - ability to create service accounts and
   manage IAM policies on service accounts
1. Download and run the official Gemini CLI script to create a Workload Identify
   Pool and add GitHub as a Workload Identify Provider.
   ```bash
   curl -L https://raw.githubusercontent.com/google-github-actions/run-gemini-cli/main/scripts/setup_workload_identity.sh -o setup_workload_identity.sh

./setup_workload_identity.sh

   ./setup_workload_identity.sh.
   ```

Alternatively, you can obtain a Gemini API key and store it as a secret in the
GitHub Actions settings of your repo. This is less recommended from a security
point of view because keys have broad permissions, hard to manage at scale, and
prone to getting leaked in code and logs.

1. Obtain a Gemini API key from Google AI Studio.
1. Go to your repository's Settings > Secrets and variables > Actions. 
   Click New repository secret.
   Name: GEMINI_API_KEY
   Value: your API key

## Configure Gemini Code Assist GitHub App

Visit https://github.com/marketplace/gemini-code-assist and install it for free.
Follow the on-screen instructions to accept the Google Term of Service.

If you are an enterprise user instead of a consumer user, follow these
[instructions][3].

## Start up the app

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Visit `http://127.0.0.1:5000` to access the dashboard.

[1]: https://github.com/gemini-cli-extensions/security
[2]: https://github.com/apps/gemini-code-assist
[3]: https://developers.google.com/gemini-code-assist/docs/set-up-code-assist-github#enterprise
