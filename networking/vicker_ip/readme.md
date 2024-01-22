# Vicker IP

## Prompt

```
Vicker IP

50 Points

Hi! It's good to see you again in my networking series. There are total 18 challenges in this series & based on real life events of how can a server be compromised. Please download the attachment which will be used to answer all the questions. Don't make it too complex. Just keep it simple. Hope you'll solve them all. Wish you all a very good luck.

Scenario: Recently one of Knight Squad's asset was compromised. We've figured out most but need your help to investigate the case deeply. As a SOC analyst, analyze the pacp file & identify the issues.

So let's start with the basic.

Attachment

What is the victim & attacker ip?

Flag Format: KCTF{victimIp_attackerIp} 
```

## Solution

This one took a bit of time for me because I had not touched wireshark in a bit. However, after looking through the packets for a bit, I realized there were a ton of get requests from 192.168.1.7 to 192.168.1.8 which looked like a directory search. 

I tried `KCTF{192.168.1.7_192.168.1.8}` and it turned out to be right.
 
