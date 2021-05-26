#!//usr/bin/python3.6 

import requests
import json
import pprint
from aci_login import get_token


## gets subnet from apic and prints it by tenant, description, subnet and subnet mask


def get_tenants():
   token = get_token()

   url = "https://oiccapic2.icc.partners.org/api/node/class/fvSubnet.json"
   ## url = "https://oiccapic2.icc.partners.org/api/node/class/fvBD.json"   
   headers = {
      "Cookie" : f"APIC-Cookie={token}", 
   }

   requests.packages.urllib3.disable_warnings()
   response = requests.get(url, headers=headers, verify=False)

   return response

if __name__ == "__main__":
   response = get_tenants().json()
   tenants = response['imdata']
   
   listlen = len(response['imdata'])
   print(listlen)
   for subnet in range(len(response['imdata'])):
       subnetonly = response['imdata'][subnet]['fvSubnet']['attributes']['dn'].split('/')
       if subnetonly[1] == 'tn-PHS_Lab_Tenant':
           print(subnetonly[1:5])
   print('\n')

   for subnet in range(len(response['imdata'])):
       subnetonly = response['imdata'][subnet]['fvSubnet']['attributes']['dn'].split('/')    
       if subnetonly[1] != 'tn-PHS_Lab_Tenant':
           print(subnetonly[1:5])


