# Genexis-JSON-RPC
Get info from your Genexis via JSON-RPC

Developed and tested on a Genexis Platinum 7840

The Genexis Platinum 7840 has a web interface on http://192.168.1.254/ . Under the hood, the Genexis talks JSON-RPC against http://192.168.1.254/api

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


