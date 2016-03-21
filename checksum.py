from Crypto.Hash import SHA256, SHA, MD5
import argparse

parse = argparse.ArgumentParser(prog='Checksum',description='Support SHA1, SHA256, MD5', add_help=False);
parse.add_argument("-h", "--hash", help="Hash Althorigm")
parse.add_argument("-c", "--checksum", help="Checksum Input")
parse.add_argument("input", help="Input file")

args = parse.parse_args()
args.hash = args.hash.lower()
if (args.hash != 'sha1' and args.hash != 'sha256' and args.hash != 'md5'):
    print('The althorigm is not supported')
else:

    block_size=256
    data=''
    fi = open(args.input,"rb")
    while (1):
        tmp = fi.read(block_size)
        if len(tmp) == 0:
            break;
        else: data += tmp
    fi.close()

    hashvalue = ''
    if (args.hash == 'sha1' ):
        tmp = SHA.new(data)
        hashvalue += tmp.hexdigest()
    elif  (args.hash == 'sha256'):
        tmp = SHA256.new(data)
        hashvalue += tmp.hexdigest()
    elif args.hash == 'md5':
        tmp = MD5.new(data)
        hashvalue += tmp.hexdigest()

    if args.checksum is not None:
        if (args.checksum == hashvalue):
            print('True')
        else: print('False')
    print("Checksum is: ")
    print(hashvalue)


