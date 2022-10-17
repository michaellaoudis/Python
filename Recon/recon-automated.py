import os, sys

def recon(targetIp):
    os.system(f"nmap -A -p- -Pn {targetIp} -v")
    os.system(f"dirb {targetIp}")

def main():
    if len(sys.argv) !=1:                                                # If input is NOT: <program name> <target URL>
        print("(+) Usage: %s <url>" % sys.argv[0])                       # Print example usage
        print("(+) Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)                                                     # Exit program after incorrect run
    
    recon(input("Enter target IP: "))


if __name__ == "__main__":
    main()
    