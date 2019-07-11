import requests, urllib

# r = requests.get('http://127.0.0.1:5000/create', params={"index":"abaa", 'name': 'abc', 'quantity':40})
r = requests.get('http://127.0.0.1:5000/retrieve/abaa', params={"index":"abaa", 'name': 'abc', 'quantity':40})

print(r.text)