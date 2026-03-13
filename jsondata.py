import json
#with open('r1.json') as file:
#    data = json.load(file)

router_dict ={
    "router": "R1",
    "interfaces": [
        {
            "id": "0",
            "enabled": "true",
            "ip":"192.168.1.254",
            "mask":"255.255.255.0"
        },
        {
            "id": "1",
            "enabled": "false",
            "ip":"172.12.1.1",
            "mask":"255.255.255.0"
        }
    ],
    "routing": {
        "routes": [
            {
                "destination":"10.1.1.0",
                "mask":"255.255.255.0",
                "gateway":"192.168.1.253"
            },
            {
                "destination":"10.2.2.0",
                "mask":"255.255.255.0",
                "gateway":"192.168.1.253"
            }
        ]

    }
}

print(type(router_dict))

#data = json.loads(router_json)
router_json = json.dumps(router_dict)
print(router_json)

with open('data.json','w') as file:
    json.dump(router_dict,file,indent=2)

