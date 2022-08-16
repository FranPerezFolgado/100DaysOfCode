alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt(text, shift):
    encrypted= []
    for letter in text:
        encrypted.append(alphabet[alphabet.index(letter)+shift])
    
    encrypted_result = ''.join(encrypted)
    print(encrypted_result)

def decrypt(text, shift):
    decrypted = []
    for letter in text:
        decrypted.append(alphabet[alphabet.index(letter)-shift])
    
    decrypted_result = ''.join(decrypted)
    print(decrypted_result)