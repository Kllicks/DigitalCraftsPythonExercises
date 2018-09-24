#***use if in or not in for skipping over spaces***


# Given a string, print the Caesar Cipher (or ROT13) of that string.
# Use your solution to decipher the following text: "lbh zhfg hayrnea jung lbh unir yrnearq"

cipher = input("Are you going to decrypt or encrypt? ")
cipher = cipher.lower()
alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
         "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
offset = 13
# offset = int(input("Provide an offset (0-25): "))
encryption = []
decryption = []

def encrypt(e, offset):
    for i in e:
        index = alpha.index(i)
        crypt = (index + offset) % 26 #modulus operator
        newLetter = alpha[crypt]
        encryption.append(newLetter)
    return encryption

def decrypt(d, offset):
    for i in d:
        index = alpha.index(i)
        crypt = (index + offset) % 26
        newLetter = alpha[crypt]
        decryption.append(newLetter)
    return decryption        

if cipher == "encrypt" or cipher == "e":
    response = input("What do you want encrypted? ")
    response = response.lower()
    response = response.replace(" ", "")
    code = encrypt(response, offset)
    # print(code)
    for i in encryption:
        print(i, end = "")
    print()
elif cipher == "decrypt" or cipher == "d":
    response = input("What do you want decrypted? ")
    response = response.lower()
    response = response.replace(" ", "")
    code = decrypt(response, offset)
    # print(code)
    for i in decryption:
        print(i, end = "")
    print()    
else:
    print("Please choose to Encrpyt or Decrpyt")
