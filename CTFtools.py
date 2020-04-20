# _*_ coding:UTF-8 _*_
# main.py

'''
This is a small tool to solove problem of CRYPTO in CTF.
'''

import urllib.request

import hashlib
import base64
from pycipher import Caesar


def caesar_decode(string, key):
    plaintext = Caesar(int(key)).decipher(string, keep_punct=True)
    return plaintext


def caesar_encode(string, key):
    plaintext = Caesar(int(key)).encipher(string, keep_punct=True)
    return plaintext


def b64en(string):
    a = base64.b64encode(string.encode())
    return a.decode()


def b64decode(string):
    a = base64.b64decode(string).decode()
    return a


def md5(string):
    a = hashlib.md5()
    a.update(string.encode())
    return a.hexdigest()


def URLDecode(a):
    b = urllib.request.quote(a, encoding='UTF-8')
    print(b)


def URLEncode(a):
    b = urllib.request.unquote(a, encoding='UTF-8')
    print(b)


def str_reverse(a):
    b = a[::-1]
    print(b)


def md5_net(hash='5d41402abc4b2a76b9719d911017c592'):
    import requests

    url = "https://www.md5online.org/md5-decrypt.html"
    print(f"Please decrypt the md5 at here: {url}")
    #
    # querystring = {"hash": '5d41402abc4b2a76b9719d911017c592'}
    #
    # headers = {
    #     'host': "www.md5online.org",
    #     'connection': "keep-alive",
    #     'content-length': "37",
    #     'cache-control': "no-cache",
    #     'origin': "https://www.md5online.org",
    #     'upgrade-insecure-requests': "1",
    #     'dnt': "1",
    #     'content-type': "application/x-www-form-urlencoded",
    #     'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
    #     'sec-fetch-dest': "document",
    #     'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    #     'sec-fetch-site': "same-origin",
    #     'sec-fetch-mode': "navigate",
    #     'sec-fetch-user': "?1",
    #     'referer': "https://www.md5online.org/md5-decrypt.html",
    #     'accept-encoding': "gzip, deflate, br",
    #     'accept-language': "en,zh-CN;q=0.9,zh;q=0.8",
    # }
    #
    # response = requests.post(url, headers=headers, params=querystring, timeout=10)
    #
    # print(response.text)


def b64de(string):
    return b64_moudle.b64decode(string)


def caesar_en(a, key):
    return caesar_encode(a, key)


def caesar_de(a, key):
    return caesar_decode(a, key)


def encoding(string):
    # encode with str reverse
    print(f"String Reverse: {string[::-1]}".center(50))

    # encode with Base64
    print(f"Base64: {b64en(string)}".center(50))
    # encode with Caesar
    for i in range(26):
        print(f"Caesar [key={i}]: {caesar_en(string, i)}".center(50))

    # encode with MD5
    print(f"MD5: {md5(string)}".center(50))


def decoding(string):
    # Decode with str reverse
    print(f"String Reverse: {string[::-1]}".center(50))

    # Decode with Base64
    try:
        print(f"Base64: {b64de(string)}".center(50))
    except:
        print(f"Base64: no result!".center(50))
    # Decode with Caesar
    # try:
    for i in range(26):
        print(f"Caesar [key={i}]: {caesar_de(string, i)}".center(50))
    # except:
    #     print(f"Caesar: no result!".center(50))

    # Decode with MD5
    print(f"{md5_net()}".center(50))


if __name__ == '__main__':
    # main()
    while True:
        print("\n\n\n -------------------------------------------------")
        selection = int(input("Are you going to encode  or decode?\n 1. encode\n 2. decode\nInput a number: "))
        string = input("String = ")
        print("-------------------------------------------------\n\n\n[Output]")

        if selection == 1:
            encoding(string)
        elif selection == 2:
            decoding(string)
