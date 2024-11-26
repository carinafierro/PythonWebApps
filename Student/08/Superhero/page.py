from requests import get

resp = get('https://shrinkingworld.com')
print('Google', resp)
print(resp.text)