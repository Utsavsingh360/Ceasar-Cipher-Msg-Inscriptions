# import logo
# print(gogo)


alphabet= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]

#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
#text = input("Type your massege: \n").lower()
#shift = int(input("Type the shift number: \n"))


#NOTIC- DUE TO "ceaser()" FUNCTION 'encrypt()' or 'decrypt()' function will re remove(or in comment).
# 1.1 Create a function called 'encrypt() that takes 'original_text' and 'shift_amount' as 2 inputed
#def encrypt(original_text, shift_amount):
#    # 1.2 Inside the 'encrypt()' function, shift each letter of the 'original_text' formate in the alphabet by shift amount and print the encrypted text.
#    cipher_text = ""
#    for letter in original_text:
#        shifted_position = alphabet.index(letter) + shift_amount
#
#        shifted_position %= len(alphabet) # 0 -> 25 # 1.4 What happens if you try to shift z forward by 9 ? Can you fix the code?
#        cipher_text += alphabet[shifted_position]
#    print(f"Here is the encoded result: {cipher_text}")

# NOTIC- DUE TO "ceaser()" FUNCTION 'encrypt()' or 'decrypt()' function will re remove(or in comment).

# 2.1 Create a function called 'decrypt()' thank takes 'original_text' and 'shift_amount' as inputs.
# def decrypt(original_text, shift_amount):
#     # 2.2 Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet by shift amount and print the decrypted text.
#     output_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) - shift_amount
#
#         shifted_position %= len(alphabet)  # 0 -> 25 # 1.4 What happens if you try to shift z forward by 9 ? Can you fix the code?
#         output_text += alphabet[shifted_position]
#     print(f"Here is the encoded result: {output_text}")

# 2.3 Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#     Use the value of the user chosen 'direction' variable to determine which functionality to use.

def ceaser(original_text, shift_amount, encode_or_decode ):
    output_text = ""

    if encode_or_decode == "decode":     # This line of code come from line number 53 and 54.
        shift_amount *= -1

    for letter in original_text:

        if letter not in alphabet:   # This resolve the issue, if numbers, symbols or spaces comes in massage.
            output_text += letter


        else:
            # if encode_or_decode == "decode" :     #This line of code get Paseted upper side, for we encode a msg and
            #     shift_amount *= -1                # then also want to decode that msg, then it will help you a lot for this.

            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)  # 0 -> 25 # 1.4 What happens if you try to shift z forward by 9 ? Can you fix the code?
            output_text += alphabet[shifted_position]

    print(f"Here is the {encode_or_decode}d result: {output_text}")


# By the help of this, we can restart the game after asking from user.
should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    text = input("Type your massege: \n").lower()
    shift = int(input("Type the shift number: \n"))


    ceaser(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Good Bye !!")



# 1.3 Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a message.

# encrypt(original_text= text, shift_amount= shift)
#decrypt(original_text= text, shift_amount= shift)