import requests

headers = {
    "X-Auth-Email": "",  # Cloudflare account email
    "X-Auth-Key": "",  # Cloudflare Global API Key
}

json_data = {
    "type": "",  # A, CNAME, TXT, MX, etc.
    "name": "",  # subdomain
    "content": requests.get("https://api.ipify.org").text,  # your public IP
    "ttl": 60,
    "proxied": False,  # set to True if you want Cloudflare to proxy the DNS
}

response = requests.put("https://api.cloudflare.com/client/v4/zones/85e96ab652f97ac8c45cf0be461329be/dns_records/31eeac365622f34d6db3d4869affce82", headers=headers, json=json_data)
print(response.text)
