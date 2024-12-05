def caesar_cipher(message, shift):
    encrypted_message = '' #initializes the encrypted message as an empty string first

    for char in message: #iterates through each character in the 'message' string
        if char.isalpha(): #only runs if the string is a character or characters
            if char.isupper():
                shifted_value= (ord(char) - ord("A") + shift) #calculates the shifted value
                new_char = chr(shifted_value % 26 + ord("A")) #converts the shifted value into a new char
            elif char.islower():
                shifted_value = (ord(char) - ord("a") + shift) #calculates the shifted value
                new_char = chr(shifted_value % 26 + ord("a")) #converts the shifted value into a new char
            encrypted_message += new_char #adds the shifted character to the encrypted message
        else:
            encrypted_message += char # if numerals are included in the parameters, the above code will not apply to them and they will remain unchanged

    return encrypted_message #return the final encrypted message

print(caesar_cipher("XYZ", 2)) #calling the function and then printing it