# README

## Prompt

```
README

305 Points

Read me if you can!!

N:B: There is no need to do bruteforce.

Author: saif
Target : http://66.228.53.87:8989/
```

## What I did

I did not solve this challenge during the competition but I wanted to include what I did, and then after how to actually solve it. 

After going to the target, I can see there is a `flag.txt` and a `text.txt` on the website with a prompt to `Enter anything` to read. I looked at the source code and found that there is an event listener on the form which encodes the input prompt and goes to `\`/fetch?file=$encodeURIComponent(url)}\`` and prints the response. I went to the `target/fetch?file=text.txt` and the response was a json format of the following: `Yes! You can read files! Dont ask for hint its ezz!!`. You can also type it into the read prompt on the home screen of the target and it displays the same thing. 

So I tried to input `flag.txt` into the prompt, to which it responded with a `403 Access Denied`. After this I realized it could be an injection attack to specify the credentails weren't required to get the page. This is as far as I got.

## Actual Solution

The actual solution automated this with python (which I should have done and would have done if I knew how to do it with python [but that's why I'm doing it now]). 

The actual solution starts where I ended off (which is good because that means I was on the right track). Although it was an easy script when automated in python. 

Apparently theres a [403 bypass](https://book.hacktricks.xyz/network-services-pentesting/pentesting-web/403-and-401-bypasses) after a quick google. 

Including the headers in the python script and after running it, gives the flag: `{"result":"KCTF{kud05w3lld0n3!}"}`

[Original Solution](https://github.com/Aryt3/writeups/tree/main/jeopardy_ctfs/2024/knight_ctf_2024/README)


