#!/usr/bin/env python

from Crypto.Cipher import AES
import base64
import sys

class Encrypt():
    def __init__(self):
        self.PADDING = '{'
        self.BLOCK_SIZE = 32
        self.secret = '9\xcc0a\x12\xb7\xb9\x1d\xe4\xee\xce\xf8\xf9\x83\xd3\x92\x15\xecjUiKlZ\xdatd\xb6n\x0b\x81\x9a'
        self.cipher = AES.new(self.secret)
    def encrypt(self,string_to_enc):
        #string_to_enc = string_to_enc.replace('@','/AT-THE-RATE-OF/')
        string_to_enc = string_to_enc + (self.BLOCK_SIZE - len(string_to_enc) % self.BLOCK_SIZE) * self.PADDING
        #print string_to_enc
        enc_str =  base64.b64encode(self.cipher.encrypt(string_to_enc))
        enc_str = enc_str.replace('+','_P4L5U6S98')
        enc_str = enc_str.replace('/','_SL143_SH')
        return enc_str
    
    def decrypt(self,string_to_dec):
        str_dec = string_to_dec.replace('_P4L5U6S98','+')
        str_dec = str_dec.replace('_SL143_SH','/')
        str_dec = self.cipher.decrypt(base64.b64decode(str_dec))
        #print str_dec 
        return str_dec.rstrip(self.PADDING)


if __name__ == '__main__':
    enc = Encrypt()
    string_val = sys.argv[1]
    enca = enc.encrypt(string_val)
    print 'encrypted string =  : ', enca , ' len is :', len(enca)
    dec = enc.decrypt(enca)
    print 'decrypted string = :', dec, ' len is : ' , len(dec)


