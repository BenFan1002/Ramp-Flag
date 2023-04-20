import requests

url = "https://0ijq1i6sp1.execute-api.us-east-1.amazonaws.com/dev/stream"

flag = set()
while True:
    response = requests.get(url)
    html_content = response.text[1]
    flag.add(html_content)
    if len(flag) == 7:
        break

print(''.join(flag))
