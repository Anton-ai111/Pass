import hashlib

def cracker():
    print("""
        sha1 = 0
        sha224 = 1
        sha256 = 2
    """)
    n=int(input("Whats ur guess: "))
    v=input("and after that type the pass: ")

    if n==0:
        hash = hashlib.sha1(v.encode('utf-8')).hexdigest()
    if n==1:
        hash = hashlib.sha224(v.encode('utf-8')).hexdigest()
    if n==2:
        hash = hashlib.sha256(v.encode('utf-8')).hexdigest()
    print(hash)

def banner():
    print("""
        
__________                        __________                       
\______   \_____    ______ ______ \______   \_____  ______   ____  
 |     ___/\__  \  /  ___//  ___/  |       _/\__  \ \____ \_/ __ \ 
 |    |     / __ \_\___ \ \___ \   |    |   \ / __ \|  |_> >  ___/ 
 |____|    (____  /____  >____  >  |____|_  /(____  /   __/ \___  >
                \/     \/     \/          \/      \/|__|        \/ 
            Made by Anton Hrlić
    """)

def main():
    banner()
    cracker()

if __name__=="__main__":
    main()
