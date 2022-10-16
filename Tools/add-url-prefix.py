# This script appends "https://" and "http://" (respectively) to the beginning of every line in a text file.
# It creates a new file in the process, leaving the original one untouched.

# Example: 
# If we have example.com on its own line in a txt file and run the script, a new txt file would be created containing "https://example.com" and "http://example.com"

def addHttps():
    httpsPrefix, httpPrefix = "https://", "http://"
    with open("D:\\Projects\\Bug-Bounty\\amass-domains.txt", "r") as src:
        with open('D:\\Projects\\Bug-Bounty\\amass-domains-https.txt', 'w') as dest:
            for line in src:
                dest.write('%s%s\n' % (httpsPrefix, line.rstrip('\n')))
                dest.write('%s%s\n' % (httpPrefix, line.rstrip('\n')))

def main():
    print("(+) Creating file of urls...")
    addHttps()
    print("All done!")

if __name__ == "__main__":
    main()
