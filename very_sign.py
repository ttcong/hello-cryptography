from Crypto.Hash import SHA256, SHA, MD5
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
import argparse
import os
parse = argparse.ArgumentParser(prog='Verify Digital Signature', description='Support SHA1, SHA256, MD5', add_help=False);
parse.add_argument("-h", "--hash", help="Hash Althorigm")
parse.add_argument("data", help="Input data file.")
parse.add_argument("signature", help="Input signature file")
args = parse.parse_args()
args.hash = args.hash.lower()
if (args.hash != 'sha1' and args.hash != 'sha256' and args.hash != 'md5'):
    print('The althorigm is not supported')
else:
    #Create Hash value from data.
    print("Verifying this digital signature")
    block_size=256
    data=''
    fi = open(args.data,"rb")
    while (1):
        tmp = fi.read(block_size)
        if len(tmp) == 0:
            break;
        else: data += tmp
    fi.close()

    hash
    if (args.hash == 'sha1' ):
        hash = SHA.new(data)
    elif  (args.hash == 'sha256'):
        hash = SHA256.new(data)
    elif args.hash == 'md5':
        hash = MD5.new(data)
    print(hash.digest())

    #Read signature from signature
    fi = open(args.signature,"r")
    signature = fi.read()
    fi.close()


    if os.path.isfile("pubkey.pub"):
        #Read public key
        pubkey_file = open("pubkey.pub", "r")
        pubkey = RSA.importKey( pubkey_file.read() )
        pubkey_file.close()

        #verify
        verifier = PKCS1_v1_5.new(pubkey)
        if verifier.verify(hash, signature):
            print("It's true")
        else: print("It's false")
    else: print("Can not find public key file <pubkey.pub>...Can not complete verifying")

    print("Finished")