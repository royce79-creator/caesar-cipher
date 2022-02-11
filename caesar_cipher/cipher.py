from nltk.util import pr
from caesar_cipher.corpus import name_list, word_list
import string

def encrypt(text, key):
    alphabet_low = string.ascii_lowercase
    alphabet_up = string.ascii_uppercase

    shifted_alphabet_low = alphabet_low[key:] + alphabet_low[:key]
    shifted_alphabet_up = alphabet_up[key:] + alphabet_up[:key]
    low_transform = str.maketrans(alphabet_low, shifted_alphabet_low)
    up_transform = str.maketrans(alphabet_up, shifted_alphabet_up)
    
    low_encrypted = text.translate(low_transform)
    combined_encrypted = low_encrypted.translate(up_transform)

    return combined_encrypted

def decrypt(encrypted, key):
    return encrypt(encrypted, -key)

def crack(encrypted):
    for i in range(26):
        word_count = 0
        words = encrypt(encrypted, i)
        list = words.split()
        for text in list:
            if text in name_list or text.lower() in word_list:
                word_count += 1
        
        if (word_count/len(list)) > .5:
            return " ".join(list)
    return ""

# import nltk

# # nltk.download()

# def encrypt(text,s):
#     result = ''

#     # traverse text
#     for i in range(len(text)):
#         char = text[i]

#         # Encrypt uppercase characters
#         if (char.isupper()):
#             result += chr((ord(char) + s - 65) % 26 + 65)
#         elif char == ' ':
#           result += char

#         # Encrypt lowercase characters
#         elif (char.islower()):
#           result += chr((ord(char)) + s - 97 % 26 - 65)
#         else:
#             result += chr((ord(char)) + s - 97 % 26 + 97)

#     return result

# #check the above function
# text = "ATTACKATONCE"
# s = 4
# print ("Text  : " + text)
# print ("Shift : " + str(s))
# print ("Cipher: " + encrypt(text,s))

# def decrypt(encrypted, key):
#     return encrypt(encrypted, -key)

# def crack(encrypted):
#     for i in range(26):
#         word_count = 0
#         words = encrypt(encrypted, i)
#         list = words.split()
#         for text in list:
#             if text in name_list or text.lower() in word_list:
#                 word_count += 1
        
#         if (word_count/len(list)) > .5:
#             return " ".join(list)
#     return ""

# if __name__ == "__main__":
#     enc1 = encrypt('12345', 2)
#     assert enc1 == ('34567')

#     # enc2 = encrypt('678', 2)
#     # assert enc2 == ('890')

#     # enc3 = encrypt('1234', 28374)
#     # print(enc3)

#     enc4 = decrypt('34567', 2)
#     assert enc4 == '12345'
