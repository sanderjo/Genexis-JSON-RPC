# Genexis-JSON-RPC
Get info from your Genexis via JSON-RPC

Developed and tested against a Genexis Platinum 7840


# Introduction

The Genexis Platinum 7840 has a web interface on http://192.168.1.254/ . Under the hood, the Genexis talks JSON-RPC against http://192.168.1.254/api

Please note: you need the Genexis admin password to do all this. It's on the back of your Genexis.

With Google Chrome's F12 (-> Network -> Headers), you can inspect those JSON-RPC calls, and then re-use them.

For example, the login sequence is a POST with the following Request Payload:

```
{"jsonrpc":"2.0","id":2,"method":"session.login","params":{"username":"admin","password":"7AHS8TEQ"}}
```

with answer:

```
{ "jsonrpc": "2.0", "result": { "sessionid": "53b1b42e64259d1aa84ab9991b05b2005c1103f672b1fcba5f408e9a9af4cf42", "result": 0 }, "id": 2 }
```

So: we get a sessionid for the real JSON-RPC requests


As an example, in the Genexis admin GUI, Google Chrome's F12 will show this for Interfaces:

The request:
```
{"jsonrpc":"2.0","id":8,"method":"interfaces.get","params":{"sessionid":"53b1b42e64259d1aa84ab9991b05b2005c1103f672b1fcba5f408e9a9af4cf42"}}
```

The answer:
```
{ "jsonrpc": "2.0", "result": { "lan": { "macaddr": "00:00:00:00:00:00", "ipaddr": "192.168.1.254", "netmask": "255.255.255.0", "domain name": "superman.com", "rx_packets": 0, "rx_octets": 0, "tx_packets": 0, "tx_octets": 0, "ip6addr": [ "fdd6:5a2d:3f20::1", "fe80::36e3:80ff:fe14:7131" ] }, "wlan": [ { "bssid": "00:00:00:00:00:00", "macaddr": "00:00:00:00:00:00", "speed": 0, "rx_packets": 22097184, "rx_octets": 3677634152, "tx_packets": 61482512, "tx_octets": 1625163940 }, { "bssid": "00:00:00:00:00:00", "macaddr": "00:00:00:00:00:00", "speed": 0, "rx_packets": 4743809, "rx_octets": 2717906944, "tx_packets": 26171959, "tx_octets": 199837592 } ], "lanports": [ { "status": "Up", "speed": 1000, "duplex": "Full", "rx_packets": 41620, "rx_octets": 5003989, "tx_packets": 3678928, "tx_octets": 651167873 }, { "status": "Up", "speed": 100, "duplex": "Full", "rx_packets": 2047720, "rx_octets": 653957621, "tx_packets": 18495545, "tx_octets": 3518358985 }, { "status": "Up", "speed": 100, "duplex": "Full", "rx_packets": 23762101, "rx_octets": 2672049195, "tx_packets": 70566765, "tx_octets": 805554428 }, { "status": "Up", "speed": 1000, "duplex": "Full", "rx_packets": 55860510, "rx_octets": 3921315694, "tx_packets": 238628815, "tx_octets": 1222954265 } ], "internet": { "status": "Up", "macaddr": "00:00:00:00:00:00", "ipaddr": "12.45.237.150", "netmask": "255.255.252.0", "gateway": "12.45.236.1", "dns": { "dynamic_dns": [ "12.128.0.3", "12.45.46.69" ] }, "rx_packets": 463140377, "rx_octets": 2147483647, "tx_packets": 2820478, "tx_octets": 253114598 }, "wanport": { "status": "Up", "speed": 0, "duplex": "Full", "rx_packets": 0, "rx_octets": 0, "tx_packets": 0, "tx_octets": 0 }, "result": 0 }, "id": 8 }
```
So ... a lot of nice JSON info!

# Manual CLI session with curl

Login, and get the sessionid:
```
$ curl --header "Content-Type: application/json"   --request POST   --data '{"jsonrpc":"2.0","id":2,"method":"session.login","params":{"username":"admin","password":"AB7EBCDE"}}'   http://192.168.1.254/api

{ "jsonrpc": "2.0", "result": { "sessionid": "007d94855a7bbf01b9740c89a11e7bd7c4558dad7182084c1b0278b19d018d84", "result": 0 }, "id": 2 }
```
Using that sessionid, get the Interface info:

```
$ curl --header "Content-Type: application/json"   --request POST   --data '{"jsonrpc":"2.0","id":8,"method":"interfaces.get","params":{"sessionid":"007d94855a7bbf01b9740c89a11e7bd7c4558dad7182084c1b0278b19d018d84"}}'   http://192.168.1.254/api


{ "jsonrpc": "2.0", "result": { "lan": { "macaddr": "00:00:00:00:00:00", "ipaddr": "192.168.1.254", "netmask": "255.255.255.0", "domain name": "superman.com", "rx_packets": 0, "rx_octets": 0, "tx_packets": 0, "tx_octets": 0, "ip6addr": [ "fdd6:5a2d:3f20::1", "fe80::36e3:80ff:fe14:7131" ] }, "wlan": [ { "bssid": "00:00:00:00:00:00", "macaddr": "00:00:00:00:00:00", "speed": 0, "rx_packets": 22107550, "rx_octets": 3679161041, "tx_packets": 61516160, "tx_octets": 1649486062 }, { "bssid": "00:00:00:00:00:00", "macaddr": "00:00:00:00:00:00", "speed": 0, "rx_packets": 4743809, "rx_octets": 2717906944, "tx_packets": 26187271, "tx_octets": 202828522 } ], "lanports": [ { "status": "Up", "speed": 1000, "duplex": "Full", "rx_packets": 41729, "rx_octets": 5016737, "tx_packets": 3693184, "tx_octets": 653782687 }, { "status": "Up", "speed": 100, "duplex": "Full", "rx_packets": 2049965, "rx_octets": 654692902, "tx_packets": 18511161, "tx_octets": 3521473040 }, { "status": "Up", "speed": 100, "duplex": "Full", "rx_packets": 23765508, "rx_octets": 2672432409, "tx_packets": 70585272, "tx_octets": 812438078 }, { "status": "Up", "speed": 1000, "duplex": "Full", "rx_packets": 55978631, "rx_octets": 3931679823, "tx_packets": 239475759, "tx_octets": 2479463034 } ], "internet": { "status": "Up", "macaddr": "00:00:00:00:00:00", "ipaddr": "2.45.237.150", "netmask": "255.255.252.0", "gateway": "12.45.236.1", "dns": { "dynamic_dns": [ "12.128.0.3", "12.45.46.69" ] }, "rx_packets": 463310384, "rx_octets": 2147483647, "tx_packets": 2829930, "tx_octets": 253805636 }, "wanport": { "status": "Up", "speed": 0, "duplex": "Full", "rx_packets": 0, "rx_octets": 0, "tx_packets": 0, "tx_octets": 0 }, "result": 0 }, "id": 8 }
```
The get pretty ouput, pipe through `python -m json.tool`, for example:

```
$ curl -s --header "Content-Type: application/json"   --request POST   --data '{"jsonrpc":"2.0","id":8,"method":"interfaces.get","params":{"sessionid":"007d94855a7bbf01b9740c89a11e7bd7c4558dad7182084c1b0278b19d018d84"}}'   http://192.168.1.254/api | python -m json.tool
{
    "id": 8,
    "jsonrpc": "2.0",
    "result": {
        "internet": {
            "dns": {
                "dynamic_dns": [
                    "12.128.0.3",
                    "12.45.46.69"
                ]
            },
            "gateway": "12.45.236.1",
            "ipaddr": "12.45.237.150",
...
```

# Python script



```
$ python genexis-json-rpc.py ALHS7TEQ | grep -A3 ip6
            "ip6addr": [
                "fdd6:5a2d:3f20::1",
                "fe80::36e3:80ff:fe14:7131"
            ],
```




