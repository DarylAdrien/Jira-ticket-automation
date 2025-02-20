# Jira-ticket-automation

This project is a Flask-based webhook listener that integrates GitHub issue comments with Jira. It automatically creates a Jira issue when a GitHub comment contains `/jira`.

## Features
- Listens for GitHub webhook events.
- Checks if a comment on an issue contains `/jira`.
- If `/jira` is found, creates a new Jira issue using the issue's body as the summary.
- Uses Flask to handle incoming webhook requests.

## Prerequisites
- Python 3.x installed
- A Jira account with API access
- A GitHub repository configured with a webhook

## Setup Instructions

### 1. Clone the Repository
```sh
git clone https://github.com/your-username/jira-webhook.git
cd jira-webhook
```

### 2. Install Dependencies
```sh
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Set the following environment variables:
```sh
export JIRA_EMAIL="your-email@example.com"
export JIRA_API_TOKEN="your-jira-api-token"
export JIRA_URL="https://yourdomain.atlassian.net/rest/api/3/issue"
export JIRA_PROJECT_KEY="YOUR_PROJECT_KEY"
export JIRA_ISSUE_TYPE_ID="10009"  # Change this based on your Jira issue type
```


### 4. Run the Flask Application
```sh
python app.py
```

The application will start running on `http://0.0.0.0:5000`.

## Configuring GitHub Webhook

1. Go to your GitHub repository.
2. Navigate to **Settings > Webhooks**.
3. Click **Add webhook**.
4. Set the **Payload URL** to `http://your-server-ip:5000/github-webhook`.
5. Set the **Content type** to `application/json`.
6. Choose **Just the push event** or **Issue comments**.
7. Click **Add webhook**.

## How It Works

1. A user comments `/jira` on a GitHub issue.
2. The webhook sends the payload to this Flask app.
3. The app checks if the comment contains `/jira`.
4. If true, a new Jira issue is created with the issue's body as the summary.

## Deployment
You can deploy this on any server (e.g., AWS, DigitalOcean) and expose it using `ngrok`, Nginx, or another reverse proxy.

Example using `ngrok`:
```sh
ngrok http 5000
```
Use the provided `https://` URL as your webhook payload URL in GitHub.

## License
This project is licensed under the MIT License.

