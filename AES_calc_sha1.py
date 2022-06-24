#!/usr/bin/env python
#!coding=utf-8
# !/usr/bin/python
# -*- coding: UTF-8 -*-
import base64
from Crypto.Cipher import AES
from Crypto.Hash import SHA1
from Crypto.Util.Padding import pad, unpad


class CryptUtils:
    @classmethod
    def aes_en_sha1prng(cls, data, aes_key):
        """
        java AES- SHA1PRNG 方式 加密
        :param data:
        :param aes_key:
        :return:
        """
        aes_key = cls.get_sha1prng_key(aes_key)
        cipher = AES.new(bytes.fromhex(aes_key), AES.MODE_ECB)
        ct = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
        return base64.b64encode(ct).decode('utf-8')

    @classmethod
    def aes_de_sha1prng(cls, data, aes_key):
        """
        java AES- SHA1PRNG 方式 解密
        :param data:
        :param aes_key:
        :return:
        """
        key = cls.get_sha1prng_key(aes_key)
        cipher = AES.new(bytes.fromhex(key), AES.MODE_ECB)
        d_str = cipher.decrypt(base64.b64decode(data.encode('utf-8')))
        return unpad(d_str, AES.block_size).decode('utf-8')

    @staticmethod
    def get_sha1prng_key(key):

        """
        summary]
        encrypt key with SHA1PRNG
        same as java AES crypto key generator SHA1PRNG
        Arguments:
            key {[string]} -- [key]

        Returns:
            [string] -- [hexstring]
        :param key:
        :return:
        """
        signature = SHA1.new(key.encode()).digest()
        signature = SHA1.new(signature).digest()
        return ''.join(['%02x' % i for i in signature]).upper()[:32]


if __name__ == '__main__':
    key = 'zheng'
    content = 'chenguolin123.ee'

    ciphertext = CryptUtils.aes_en_sha1prng(content,key)
    print(content + '=' + ciphertext)

    plaintext = CryptUtils.aes_de_sha1prng(ciphertext,key)
    print(ciphertext + '=' + plaintext)
