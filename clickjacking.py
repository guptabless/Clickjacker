import requests
import os

print("-----------------------------------------------")
print("Click-Jacking")
print("Code By : NG")
print("Usage: python ClickJacking.py and then follow the instructions")
print("Give URl with http:// or https://")
print("-----------------------------------------------")

input_url = str(input("Enter the website URL on which you want to check click-jacking"))
print("..........Testing for Clickjacking .....................")

input_header = requests.get(input_url)
input_Frame = input_header.headers.get('X-Frame-Options')

if ((input_Frame == 'SAMEORIGIN')  or (input_Frame == 'DENY')):
    print("..........Clickjacking Vulnerability not possible..................")
else:
    print("..........Clickjacking Vulnerability possible.........................")
    print("You Want POC of Clickjacking" "  1. 'YES' "  "  2.'NO' ")
    input_sel = input("select at least one operation")
# POC generation
    if input_sel == '1':
        filename = "Clickjacking" + ".html"
        input_location = input(print("Enter the location where you want to save clickjacking poc"))
        os.path.exists(input_location)
        f = open(input_location+filename,"w")
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
        print("Click-Jacking POC generated")
    elif input_sel == '2':
        print("Click-Jacking POC NOT generated")







