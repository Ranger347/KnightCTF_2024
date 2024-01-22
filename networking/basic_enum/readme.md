# Basic Enum

## Prompt

```
Basic Enum

100 Points

What tool did the attacker use to do basic enumeration of the server?

Please use the attachment of the first challenge.

Flag Format: KCTF{toolname}

Author: 0xt4req
```

## Actual Solution

I didn't solve this problem during the competition. We looked through the packets for a while and we could determine it was a directory search. 

We knew some tools which would usually be used to search for files or directories on a server such as gobuster, dirbuster, dirb, and nmap, but none of those tools worked.

We also tried to limit our results in the packages with filters in wireshark such as the desination ip and source ip with `ip.dst==192.168.1.8 && ip.src==192.168.1.7` but still didn't see any packets with anything. 

Another writeup also used a filter `http.request.method!=GET` because one of the first packets should be a PUT command that involves a Nikto test file. 

There were a lot of packets to sort through and we must have just missed packet 7505 which said: `PUT /nikto-test-BoMcySIt.html HTTP/1.1`

Turns out the flag was `KCTF{nikto}`. 

I always seem to forget about nikto. Hindsight is always 20-20. :(

