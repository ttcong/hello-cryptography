import argparse
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
parser = argparse.ArgumentParser(usage='This is an AES encryption demo\n')

#-m MODE -i INIT <ten file input> <ten file output>
parser.add_argument("-m", "--mode", help="Mode")
parser.add_argument("-i", "--iv", help="Initialization vector",type=int)
parser.add_argument("input", help="Input file")
parser.add_argument("output", help="Output file")
args = parser.parse_args()

if ( args.mode != "CBC" and args.mode != "ECB" and args.mode != "CFB" and args.mode != "OFB"):
    print("This mode is not supported. This program has only CBC, ECB, CFB and 0FB.")
else:
    #check input
    if  ( args.mode == "CBC"  or args.mode == "CFB" or args.mode == "OFB" ) and ( args.iv is None ):
        print ("This mode requires an Initialization vector, use default Initialization vector")
        iv = 1312057
    else:
        iv = args.iv

    fin = open(args.input, "rb")
    fout = open(args.output, "wb")
    block_size=256
    fout.write(str(iv) + '\n')

    key = SHA256.new('1312057').digest()
    iv = hex(iv)[2:8].zfill(16)
    #If encrypt with MODE ECB, not use IV
    if args.mode == "ECB":
        print("Start encryption process with mode: ECB")
        en = AES.new(key, AES.MODE_ECB)
        if args.iv is not None:
            print("Hint: This mode doesn't require an Initialization vector")

    #else encrypt with MODE CBC,CFB or OFB use IV
    elif args.mode == "CBC":
        print("Start encryption process with mode: CBC")
        en = AES.new(key, AES.MODE_CBC, iv)
    elif args.mode == "CFB":
        print("Start encryption process with mode: CFB")
        en = AES.new(key, AES.MODE_CFB, iv)
    elif args.mode == "OFB":
        print("Start encryption process with mode: OFB")
        en = AES.new(key, AES.MODE_OFB, iv)

    while 1:
        block = fin.read(block_size)
        if len(block) == 0:
            break
        elif len(block) % 16 != 0:
            block += ' ' * (16 - len(block) % 16)

        fout.write(en.encrypt(block))

    fin.close()
    fout.close()
    print("Finished")