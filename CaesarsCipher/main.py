from logofile import logo

# printing logo
print(logo)

#declaring variables
app_closed = 0
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#conditions
while app_closed != 1:
    operation = input("""Do you want to encode or decode?
Press e for encode or d for decode or q to exit: """).lower()
    if operation == "e":
        word = input("Enter the message to be encoded: ")
        shift = int(input("Type the shift number: "))
        word_list = list(word)
        new_word_list = []
        for letter in word_list:
            if letter.lower() in alphabet:
                position = alphabet.index(letter)
                new_position = (position + shift) % 26
                new_word_list.append(alphabet[new_position])
            else:
                new_word_list.append(letter)
        print(f"The encoded message is -> {''.join(new_word_list)}")
    elif operation == "d":
        word = input("Enter the message to be decoded: ")
        shift = int(input("Type the shift number: "))
        word_list = list(word)
        new_word_list = []
        for letter in word_list:
            if letter.lower() in alphabet:
                position = alphabet.index(letter)
                new_position = (position - shift) % 26
                if new_position < 0:
                    new_position*= -1
                new_word_list.append(alphabet[new_position])
            else:
                new_word_list.append(letter)
        print(f"The decoded message is -> {''.join(new_word_list)}")
    elif operation == "q":
        app_closed = 1
    else:
        print("oops thats a typo!")


   
