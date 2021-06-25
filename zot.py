import requests

zot_url = "http://localhost:23119/better-bibtex/json-rpc"

payload_bibliography = {
    "jsonrpc": "2.0",
    "method": "item.bibliography",
    "params": [
        [
            "@vukolicQuestScalableBlockchain2016",
            "lamportByzantineGeneralsProblem1982"
        ],
        {
            "id": "http://www.zotero.org/styles/ieee",
            "contentType": "text"
        },
    ]
}

r = requests.post(zot_url, json=payload_bibliography)

print(r.json()["result"])
print()
