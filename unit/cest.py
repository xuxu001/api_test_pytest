import requests
url = 'http://multi-chat-test.jihepai.com/api/group/notice/query/group/30028'
token = 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIzMDAyOCIsInJvbGVzIjpbImFkbWluIl0sImV4cCI6MTU1OTE4NjQ5Nn0.moJ7Ohmnp-1v2BfO-0r1bz-iRKvMdbdJhxg8Xc_rMaY'
header = {
    "Content-Type": "application/json",
    'Authorization':'Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIzMDAyOCIsInJvbGVzIjpbImFkbWluIl0sImV4cCI6MTU1OTE5Njc4MX0.RUUZ1SZFii0KbiBEN0RTErHM0JiDMctGo7h5LVNUTiQ'
}

requests = requests.get(url=url,headers=header)
print(requests.text)