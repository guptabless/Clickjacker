# YouCanBeFramed
A tool which checks clickjacking vulnerability and generates the POC for it .

## Requirment:
### packages 
- os
- sys
- bcolors
- argparse
- requests

### python > 3.x 


## usage: 
clickjacking.py -d <valid domain name or text file containing list of domains > -o <output location for POC>

OPTIONS: 
```
-h           --help    
             	< show the available options>
-d            Valid Domain Name with https:// or http:// 
	  		<Domain To check Clickjacking or text file conatining list of domains >
-o	      Location where you want to save ClickJAcking POC
			<OutPut Location of POC>
```

