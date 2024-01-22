# Kitty

## Prompt

```
Kitty

50 Points

Tetanus is a serious, potentially life-threatening infection that can be transmitted by an animal bite.

N:B: There is no need to do bruteforce.

Author: Munazir (YCF)
Target : http://45.33.123.243:5020/
```

## Solution

After clicking on the target, there presented is a login page with a username and password. My first instinct was to try some default usernames and passwords. I tried `admin` as the username and `password` as the password and it let me into the dashboard. After looking at some other writeups, I also found that there was a static javascript script in `/static/script.js`, which you could use to find even after authenticating, it sends to the `/dashboard` link anyway. 

After logging into the `/dashboard` page and looking at the source code, in the <script> tag there is code for when a post starts with `cat flag.txt` to make the body of the post have the contents of the flag. In the `Enter Post:` prompt on the website, type `cat flag.txt` and a `Flag Post` appears with the contents of the flag which is: `KCTF{Fram3S_n3vE9_L1e_4_toGEtH3R}`. 

