from Crypto.Hash import SHA256, SHA, MD5
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto import Random
import argparse
import os.path

parse = argparse.ArgumentParser(prog='Make Digital Signature', description='Support SHA1, SHA256, MD5', add_help=False);
parse.add_argument("-h", "--hash", help="Hash Althorigm")
parse.add_argument("input", help="Input data file.")
parse.add_argument("output", help="Output signature file")
args = parse.parse_args()
args.hash = args.hash.lower()
if (args.hash != 'sha1' and args.hash != 'sha256' and args.hash != 'md5'):
    print('The althorigm is not supported')
else:
    #Create Hash value from data.
    print("Creating digital signature")
    block_size=256
    data=''
    fi = open(args.input,"rb")
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

    if os.path.isfile("prvkey.prv"):
        prvkey_file = open("prvkey.prv","r")
        key = RSA.importKey(prvkey_file.read())
        prvkey_file.close()
    else:
        # create random key
        random_generator = Random.new().read
        key = RSA.generate(1024, random_generator)

        # save private key
        prvkey_file = open("prvkey.prv","w")
        prvkey_file.write(key.exportKey())
        prvkey_file.close()

    # sign by private key
    signer = PKCS1_v1_5.new(key)
    signature = signer.sign(hash)
    print("The digital signature for your file is: ")
    print(signature)

    # export public key
    pubkey_file = open("pubkey.pub","w")
    pubkey_file.write(key.publickey().exportKey())
    pubkey_file.close()
    print("Public key is: ")
    print(key.publickey().exportKey())
    print("Public key has been exported into <pubkey.pub>")

    #export signature
    fo = open(args.output,"wb")
    fo.write(signature)
    fo.close()
    print("Digital signature has been saved into file " + args.output)
    print("Finished")