# Week 2 Solutions

The best documentation was submitted by:
- Anirudh Nayak
- Yarra Puja Sri

Folks who've solved both the questions:
- Lucky Verma
- Sucheth K Katte
- Anirudh Nayak
- Ankit Kumar

## Solution for CTF0:BeginnersMania:
The question had a function that had to be called for printing a flag but wasn't called in the main-function. Therefore, there are many ways of exploiting this as the flag-function wasn't scrambled/encrypted for simple operations to not expose. Some ways:
- A simple `strings ChainedWithin` in Linux (open it on NotePad for windows) and find for the flag
- Use `Pwn` library to exploit binaries to call an uncalled function.
- Use **decompilers** to find the scope of the decompiled source-code. 

The flag is: `PacketVSocket{D@ym_U_Str17g_n_61n4ry!}`

## Solution for CTF1:FishFish!WhereAreU?
Flag was divided into two-parts, where one-half was in the visible description of the image, while the other was encrypted and hidden in the File's Extended Parameters/Metadata.
- To find the **first-half**, Open the Image in an image-viewer: `packetvsocket{th15_15_17`
- For the **second-half**, follow the steps:
    - Using `exiftool Inside_N_Invisible_hidden.png` will give you `Encryption                      : WxHfEkhjrE0LemgXHHSMJQ==` in the Metadata. (It's not just Base64 encoded, but encrypted by TwoFish-CBC)
    - To find out the other information, you'd have to find for decrypting the steganography. One of the Most prominant/popular steganography on images is by [ChrisL - styleuxx](github.com/stylesuxx/steganography), and has the page [here](stylesuxx.github.io/steganography/).
    - After decoding the steganography, you'd get:
    ```text
    PacketVSocket
    TwoFish(CBC)
    ```
    - The text `PacketVSocket` is the Key through the encryption method of `TwoFish - CBC mode`
    - Since the question speaks about **tools4noob**, the expect place for you to decrypt this was at [tools4noobs.com](https://www.tools4noobs.com/online_tools/decrypt/) and select `Algorithm:TwoFish` and `Mode: CBC` and finally `decode the input using base64`
        - Here, the Initialization-Vector is randomized by programming, and you can find the working of this tool [here](https://www.php.net/manual/en/function.mcrypt-encrypt.php)
    - And behold you'll get `c73d16l3!}`.
- Append both the halves to get your final flag.

The flag is: `packetvsocket{th15_15_17c73d16l3!}`

---

This is the solution for both the CTF questions :) They were/are simple compared to actual CTF questions; therefore, looking forward for y'all levels after level-ups. :')
