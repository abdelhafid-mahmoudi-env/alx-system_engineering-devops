import requests

url = 'https://www.whatismybrowser.com/'
response = requests.get(url)

# Get the User-Agent string from the response headers
user_agent = response.request.headers['User-Agent']

print("User-Agent:", user_agent)
