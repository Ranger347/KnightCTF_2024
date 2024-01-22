# Oceanic

## Prompt

```
Oceanic

100 Points

The ocean's beauty is in its clear waters, but its strength lies in its dark depths.

Attachment 1
Attachment 2

Flag Format: KCTF{S0m3th1ng_h3re}

Author: Ibrahim Saify {YCF}
```

## My Partial Solution

I pulled out every trick in the book for this problem, and I still didn't solve it. There must be some tool I am unaware of because I tried everything I could think of.

After downloading the files, `clue.jpg` and `peaceful.wav` I tried to do some simple information gathering on them.

I ran them both through exiftool. The wav file had nothing interesting but clue had the following: 

```bash
ExifTool Version Number         : 12.70
File Name                       : clue.jpg
Directory                       : .
File Size                       : 20 kB
File Modification Date/Time     : 2024:01:04 06:25:01-05:00
File Access Date/Time           : 2024:01:22 10:28:06-05:00
File Inode Change Date/Time     : 2024:01:20 16:32:21-05:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 300
Y Resolution                    : 300
Comment                         : 8qQd3iMYmtsyto7aXUuw1KVRpQFCRxqRtJiRgP85e36y
Image Width                     : 612
Image Height                    : 344
Encoding Process                : Progressive DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:4:4 (1 1)
Image Size                      : 612x344
Megapixels                      : 0.211
```

Clue had a comment with some random gibberish, which I put into [Cyberchef](https://gchq.github.io/CyberChef/) and it said it was base58 and translated to `theoceanisactuallyreallydeeeepp`.

I tried to use steghide to see if I could extract anything from either file with that as a password but no luck. 

Usually with audio files in CTF challenges, you can put it into Audacity or Sonic Visualizer and look at the spectrogram to reveal a secret message or hint of some sorts. However, I put peaceful into Audacity and looked at the spectrogram and nothing interesting seemed to jump out at me. 

There's a tool called [stegoveritas](https://github.com/bannsec/stegoVeritas) which can be used to generate red, green, and blue images of an image and sometimes that reveals a message or a hint, but also no luck there. 

The final thing I did was actually look closely at the image. At the bottom of the image, there was something the looked like bubbles coming from the depths. I tried this as a flag but no luck. 

