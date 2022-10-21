# --Work in progress--

import os, sys

def recon(targetIp):
    os.system(f"nmap -A -p- -Pn {targetIp} -v")
    os.system(f"dirb {targetIp}")

def main():
    try:
        targetIp = sys.argv[1]
        recon(targetIp)
    except:
        print("(+) Usage: %s '127.0.0.1' % sys.argv[0])                       # Print example usage
        print("(+) Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)                                                     # Exit program after incorrect run

if __name__ == "__main__":
    main()
    
