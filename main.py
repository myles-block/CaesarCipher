import sys

def remove(string):
    return string.replace(" ", "")

def caesar_encrpyt(string, cipher_number):
    encode = str("")
    for letter in string:
        ascii = ord(letter)
        if ascii in range(65, 91):# checks if ascii value is uppercase and resolves overlap if necessary
            ascii = ascii + cipher_number
            if ascii > 90:
                ascii = (ascii - 90) + 64
        else:
            continue#moves past punctuation
        transfer_back = chr(ascii)
        encode = encode + transfer_back
    return encode

def formatting(code):
    formatted = str("")
    count = 1
    jump = 0
    for letter in code:
        if(not(count % 5 == 0)):
            formatted += letter
            count = count + 1
        elif(count % 5 == 0):
            formatted += letter
            formatted += " "
            count = count + 1
            jump = jump + 1
            if(jump % 10 == 0):
                formatted += "\n"
    return formatted
        
n = len(sys.argv)
all = str("")
if n > 1:
    k = int(sys.argv[1])#how to pull arguements after python3 main.py 1
    print("Enter Caesar Cipher phrase: (type q to stop)")
    for line in sys.stdin:
        line = line.rstrip()
        line = line.upper()
        line = remove(line)#removes all the spaces from line
        coded = caesar_encrpyt(line, k)#coded version of line
        # all += line
        if ('q' == line.rstrip() or 'Q' == line.rstrip()):
            break
        format = formatting(coded)#puts into respective formatting
        print(format)
    # all = all.rstrip(all[-1])
    # print(all)
else:
    print("You gave no key...")
    print("Remember type python3 main.py <key> in CLI")
    print("")
