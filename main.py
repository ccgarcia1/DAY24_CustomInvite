#TODO: Create a letter using starting_letter.txt
with open(r"./Input/Letters/starting_letter.txt", mode="r") as file:
    starting_letter = file.read()

#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
with open(r"./Input/Names/invited_names.txt", mode="r") as file:
    names = file.readlines()
    for name in names:
        #print(name)
        invited_name = name.strip()
        formatted_letter = starting_letter.replace("[name]", invited_name)
        print(formatted_letter)
        # Save the letters in the folder "ReadyToSend".
        with open("./Output/ReadyToSend/%s_birthDay_invite.txt"%invited_name, mode="w") as file2:
            file2.write(formatted_letter)
    file.close()

