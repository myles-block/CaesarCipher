# An encoder/decoder for our spies to secretly send messages.

encryption_option = input("Would you like to Encode or Decode? ")

# should_encode will be true if the user
should_encode = "encode" in encryption_option.lower()
should_decode = "decode" in encryption_option.lower()

# Ask the user for their message and cipher number.
cipher_number = int(input("What is your cipher number? "))
message = str(input("What is your message? "))

encode = str("")  # empty encode string
decode = str("")    # empty decode string

if should_encode:
    for substring in message:
        # Handles spaces in message
        if substring == " ":
            encode = encode + substring
            continue
        # ascii conversion from substring
        ascii = ord(substring)
        # checks if ascii value is uppercase and resolves overlap if necessary
        if ascii in range(65, 91):
            ascii = ascii + cipher_number
            if ascii > 90:
                ascii = (ascii - 90) + 64
        # checks if ascii value is lowercase and resolves overlap if necessary
        elif ascii in range(97, 123):
            ascii = ascii + cipher_number
            if ascii > 122:
                ascii = (ascii - 122) + 96
        # makes sure punctuation stays the same
        else:
            ascii = ascii
        # transfers ascii values back to alphabet and adds to encode
        transfer_back = chr(ascii)
        encode = encode + transfer_back
    print(encode)
    pass
elif should_decode:
    for substring in message:
        # Handles spaces in message
        if substring == " ":
            decode = decode + substring
            continue
        # ascii conversion from substring
        ascii = ord(substring)
        # checks if ascii value is uppercase and resolves overlap if necessary
        if ascii in range(65, 91):
            ascii = ascii - cipher_number
            if ascii < 65:
                ascii = 91 - (65 - ascii)
        # checks if ascii value is lowercase and resolves overlap if necessary
        elif ascii in range(97, 123):
            ascii = ascii - cipher_number
            if ascii < 97:
                ascii = 123 - (97 - ascii)
        # makes sure punctuation stays the same
        else:
            ascii = ascii
        # transfer ascii values back to alphabet and adds to decode
        transfer_back = chr(ascii)
        decode = decode + transfer_back
    print(decode)
    pass
else:
    # Print a nice notice that we only support encrypt/decrypt
    print("We only support encrypt/decrypt")
    pass
