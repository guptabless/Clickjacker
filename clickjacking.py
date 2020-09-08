import requests
import os
import bcolors
import sys, argparse

def banner():
    print("""


            ░█████╗░██╗░░░░░██╗░█████╗░██╗░░██╗░░░░░██╗░█████╗░░█████╗░██╗░░██╗██╗███╗░░██╗░██████╗░
            ██╔══██╗██║░░░░░██║██╔══██╗██║░██╔╝░░░░░██║██╔══██╗██╔══██╗██║░██╔╝██║████╗░██║██╔════╝░
            ██║░░╚═╝██║░░░░░██║██║░░╚═╝█████═╝░░░░░░██║███████║██║░░╚═╝█████═╝░██║██╔██╗██║██║░░██╗░
            ██║░░██╗██║░░░░░██║██║░░██╗██╔═██╗░██╗░░██║██╔══██║██║░░██╗██╔═██╗░██║██║╚████║██║░░╚██╗
            ╚█████╔╝███████╗██║╚█████╔╝██║░╚██╗╚█████╔╝██║░░██║╚█████╔╝██║░╚██╗██║██║░╚███║╚██████╔╝
            ░╚════╝░╚══════╝╚═╝░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚═════╝░
                                                                                                    
          """)


if len(sys.argv) > 1:
    banner()
    if ((sys.argv[1] == '-d') | (sys.argv[1] == '-o')):
        try:
            input_url = sys.argv[2]
            input_location = sys.argv[4]

            input_header = requests.get(input_url)
            input_Frame = input_header.headers.get('X-Frame-Options')

            parser = argparse.ArgumentParser()
            parser.add_argument("-d", required=True)
            parser.add_argument("-o", required=True)
            args = parser.parse_args()

            print(bcolors.BITALIC + "Testing for Clickjacking")

            if ((input_Frame == 'SAMEORIGIN') or (input_Frame == 'DENY')):
                print(bcolors.ERR + "Clickjacking Vulnerability not possible")
            else:
                print("Clickjacking Vulnerability possible")
                filename = ".Clickjacking" + ".html"
                os.path.exists(input_location)
                f = open(input_location + filename, "w")
                wrapper = """<html>
                    <head>
                    <title>Website</title>
                    </head>
                    <body>
   		            <p>website is vulenrable</p>
   		            <iframe src=\"%s\" width="500" height="500"></iframe>
   	                </body>
                    </html>"""
                whole = wrapper % (input_url)
                f.write(whole)
                f.close()
                print("Click-Jacking POC generated and saved in " + input_location + filename)
        except:
            print('Please enter python clickjacking.py -d <valid domain name> -o <output location for POC>')
            print("Give Domain with http:// or https://")

    elif ((sys.argv[1] == '-h') | (sys.argv[1] == '--help')):
        print(bcolors.BOLD + 'usage: DNSRecord.py [-h] -d DOMAIN' '\n' 'OPTIONS:' '\n' '-h,--help    '
                             'show this help message and exit' '\n''-d Domain,   --domain Domain' '\n' '-o output    Output Save location of POC')
    elif (((sys.argv[1] != '-d') | (sys.argv[1] != '-o'))):
        print('Please enter -d <valid domain name> -o <output location>')
else:
    banner()
    print(bcolors.ERR + 'Please select atleast 1 option from (-d,-o) or -h, with a valid domain name')
