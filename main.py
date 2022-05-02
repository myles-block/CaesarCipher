import sys


n = len(sys.argv)
if n > 1:
    key = sys.argv[1]
    print(sys.argv[1])#how to pull arguements after python3 main.py 1
    print("Enter Caesar Cipher phrase: (type q to stop)")
    for line in sys.stdin:
        line = line.rstrip()
        line = line.upper()
        print(line)


        if ('q' == line.rstrip() or 'Q' == line.rstrip()):
            break
else:
    print("You gave no key...")
    print("Remember type python3 main.py <key> in execution")
    print("")
