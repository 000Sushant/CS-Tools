import hashlib
import argparse

parser = argparse.ArgumentParser(description="MD5 Creacker")
parser.add_argument("-md5",dest="hash", help="md5 hash", required=True)
# parser.add_argument("-sha1",dest="hash", help="sha1 hash", required=True)
parser.add_argument("-w", dest="wordlist", help="wordlist", required=True)
parser_args = parser.parse_args()

def main():
    hash_creacked = ""
    with open(parser_args.wordlist) as file:
        for line in file:
            line = line.strip()
            if hashlib.md5(bytes(line, encoding="utf-8")).hexdigest() == parser_args.hash:
                hash_creacked = line
                print("\n md5 hash has been successfully cracked: "+line)
                exit()
    
    if hash_creacked == "":
        print("failed to acquire the hash, try using a bigger different dictionary")

#if the program is runned on the terminal, main() will automatically executed
if __name__ == "__main__":
    main()

#use
#python hashcracker.py -md5 hash -w dict.txt