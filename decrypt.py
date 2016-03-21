import argparse
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

parser = argparse.ArgumentParser(usage='This is an AES de-encryption demo\n')

#-m MODE -i INIT <ten file input> <ten file output>
parser.add_argument("-m", "--mode", help="Mode")
parser.add_argument("input", help="Input file")
parser.add_argument("output", help="Output file")
args = parser.parse_args()

if ( args.mode != "CBC" and args.mode != "ECB" and args.mode != "CFB" and args.mode != "OFB"):
    print("This mode is not supported. This program has only CBC, ECB, CFB and 0FB.")
else:
    fin = open(args.input, "rb")
    fout = open(args.output, "wb")
    block_size=256

    key = SHA256.new('1312057').digest()

    #If encrypt with MODE ECB, not use IV
    if args.mode == "ECB":
        print("Start de-encryption process with mode: ECB")
        en = AES.new(key, AES.MODE_ECB)

    #else encrypt with MODE CBC,CFB or OFB use IV
    else:
        iv = hex(int(fin.readline()))[2:8].zfill(16)
        if args.mode == "CBC":
            print("Start de-encryption process with mode: CBC")
            en = AES.new(key, AES.MODE_CBC, iv)
        elif args.mode == "CFB":
            print("Start de-encryption process with mode: CFB")
            en = AES.new(key, AES.MODE_CFB, iv)
        elif args.mode == "OFB":
            print("Start de-encryption process with mode: OFB")
            en = AES.new(key, AES.MODE_OFB, iv)

    while 1:
        block = fin.read(block_size)
        if len(block) == 0:
            break
        elif len(block) % 16 != 0:
            block += ' ' * (16 - len(block) % 16)

        fout.write(en.decrypt(block))

    fin.close()
    fout.close()
    print("Finished")