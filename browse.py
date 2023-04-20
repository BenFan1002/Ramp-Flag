import requests

url = 'https://0ijq1i6sp1.execute-api.us-east-1.amazonaws.com/dev/browser'
headers = {'User-Agent': 'Mozilla/8.8 (Macintosh; Intel Mac OS X 8888_8888) AppleWebKit/888.8.88 (KHTML, like Gecko) Version/88.8.8 Safari/888.8.88'}

error = "  File \"/var/task/app.py\", line 258, in get\n    raise InvalidUserAgent(expected_user_agent)\nMozilla/8.8 (Macintosh; Intel Mac OS X 8888_8888) AppleWebKit/888.8.88 (KHTML, like Gecko) Version/88.8.8 Safari/888.8.88"
response = requests.get(url, headers=headers)
print(response.text)