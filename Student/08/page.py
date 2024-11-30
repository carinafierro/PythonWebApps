from requests import get

word = get('https://shrinking-world.com')
print('Google', word)
print(word.text)