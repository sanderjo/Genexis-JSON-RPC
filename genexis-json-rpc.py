#!/usr/bin/python3
import requests
import json
import sys


def main():
    url = "http://192.168.1.254/api"  # Genexis API URL
    headers = {"content-type": "application/json"}

    GenexisPassword = "ANX5WUJL"
    GenexisPassword = "6LHS7TEQ"  # The password for 'admin', on the back of the Genexis Platinum 7840
    try:
        GenexisPassword = sys.argv[1]
    except:
        print("Please specify Genexis as first parameter on the CLI")
        sys.exit(0)

    payload = {
        "jsonrpc": "2.0",
        "id": 90,
        "method": "session.login",
        "params": {"username": "admin", "password": GenexisPassword},
    }

    response = requests.post(url, data=json.dumps(payload), headers=headers).json()

    # print response
    print(json.dumps(response, sort_keys=True, indent=4, separators=(",", ": ")))
    print("response -> result:", response["result"])
    print("response -> result -> result:", response["result"]["result"])

    if response["result"]["result"] == 0:
        print("I got a OK response")
    else:
        print("Error getting sessions id ... ")
        exit(0)

    """
    if response["result"]['message'].find('Cannot create session - please try again later') >= 0:
    	print("too much sessions ...")
    	exit(0)
    """

    sessionid = response["result"]["sessionid"]

    print("\n\nInterface info:")
    payload = {"jsonrpc": "2.0", "id": 78, "method": "interfaces.get", "params": {"sessionid": sessionid}}
    response = requests.post(url, data=json.dumps(payload), headers=headers).json()
    # print response
    print(json.dumps(response, sort_keys=True, indent=4, separators=(",", ": ")))

    # print "Received octets:", response["result"]["internet"]["rx_octets"]
    # print "Transmitted octets:", response["result"]["internet"]["tx_octets"]

    print("Received MB:", int(response["result"]["internet"]["rx_octets"]) / (1024 * 1024))
    print("Transmitted MB:", int(response["result"]["internet"]["tx_octets"]) / (1024 * 1024))

    print("\n\nSystem info:")
    # {"jsonrpc":"2.0","id":106,"method":"genui.info","params":{"sessionid":"b7399ace0139cfc33833d888036b00fb7241c0fc136e2215a487c10d468477fe"}}
    payload = {"jsonrpc": "2.0", "id": 106, "method": "genui.info", "params": {"sessionid": sessionid}}
    response = requests.post(url, data=json.dumps(payload), headers=headers).json()
    # print response
    print(json.dumps(response, sort_keys=True, indent=4, separators=(",", ": ")))

    print("\n\nVoIP info:")
    # VOIP:
    # {"jsonrpc":"2.0","id":104,"method":"voip.get","params":{"sessionid":"b7399ace0139cfc33833d888036b00fb7241c0fc136e2215a487c10d468477fe"}}
    payload = {"jsonrpc": "2.0", "id": 104, "method": "voip.get", "params": {"sessionid": sessionid}}
    response = requests.post(url, data=json.dumps(payload), headers=headers).json()
    # print response
    print(json.dumps(response, sort_keys=True, indent=4, separators=(",", ": ")))

    # CATV:
    # {"jsonrpc":"2.0","id":104,"method":"catv.get","params":{"sessionid":"b7399ace0139cfc33833d888036b00fb7241c0fc136e2215a487c10d468477fe"}}

    # Access List:
    # {"jsonrpc":"2.0","id":99,"method":"accesslist.get","params":{"sessionid":"b7399ace0139cfc33833d888036b00fb7241c0fc136e2215a487c10d468477fe"}}

    # Parental Control:
    # {"jsonrpc":"2.0","id":96,"method":"parental_control.get","params":{"sessionid":"7cea9b7efd18fa5d2ea2059c9d2e9240f2a8d26df85f2ac48678b044e6279678"}}

    # Clients get
    # {"jsonrpc":"2.0","id":122,"method":"clients.get","params":{"sessionid":"b7399ace0139cfc33833d888036b00fb7241c0fc136e2215a487c10d468477fe"}}

    # DHCP get
    # {"jsonrpc":"2.0","id":122,"method":"dhcp.get","params":{"sessionid":"b7399ace0139cfc33833d888036b00fb7241c0fc136e2215a487c10d468477fe"}}


if __name__ == "__main__":
    main()
