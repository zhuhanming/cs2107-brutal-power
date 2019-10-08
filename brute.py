import subprocess
import itertools
import logging
import binascii

logging.basicConfig(level=logging.INFO)

def brute_force():
    bashCommand = "openssl enc -d -aes-128-ecb -md sha256 -base64 -nosalt -in flag.txt.enc -pass pass:"
    tries = list(itertools.product("abcdefghijklmnopqrstuvwxyz", repeat = 3))
    # tries.reverse()
    # resumed = False
    for password in tries:
        test = "".join(x for x in password)
##        if test=="txnpo":
##            resumed = True
##        if not resumed:
##            continue
##        if test=="tefaq":
##            logging.info("All tested, no flag found :(")
##            break
        code = bashCommand+"os"+test
        process = subprocess.Popen(code.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        with open('output.txt', 'a+') as f:
            f.write(output + '\n')
    process = subprocess.Popen('cat output.txt | grep "flag{"'.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    logging.info(output)
        
##        f = open("flag.txt","r").read()
##        if "flag" in f:
##            logging.info("flag found!")
##            logging.info("os"+ test)
##            logging.info(f)
##            break
    
brute_force()
