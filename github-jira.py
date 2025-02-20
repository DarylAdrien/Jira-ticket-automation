import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Jira credentials (use environment variables in production for security)
JIRA_EMAIL = ""
JIRA_API_TOKEN = ""
JIRA_URL = ""
JIRA_PROJECT_KEY = ""
JIRA_ISSUE_TYPE_ID = ""

@app.route("/github-webhook", methods=["POST"])
def github_webhook():
    data = request.json
    
    # Check if it's an issue comment event
    if data.get("action") == "created" and "comment" in data:
        comment_body = data["comment"].get("body", "")
        issue_body = data["issue"].get("body", "No description provided")
        
        if comment_body.strip() == "/jira":
            return create_jira_issue(issue_body)
    
    return jsonify({"message": "No Jira action taken"}), 200


def create_jira_issue(summary):
    auth = HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN)
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    
    payload = json.dumps({
        "fields": {
            "issuetype": {"id": JIRA_ISSUE_TYPE_ID},
            "project": {"key": JIRA_PROJECT_KEY},
            "summary": summary,
        }
    })
    
    response = requests.post(JIRA_URL, headers=headers, auth=auth, data=payload)
    
    if response.status_code == 201:
        return jsonify({"message": "Jira issue created", "response": response.json()}), 201
    else:
        return jsonify({"message": "Failed to create Jira issue", "error": response.text}), response.status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
