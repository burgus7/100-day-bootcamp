#Create a letter using starting_letter.txt

with open("./Input/Letters/starting_letter.txt", mode="r") as start:
    template = start.read()

#for each name in invited_names.txt

with open("./Input/Names/invited_names.txt") as names:
    for name in names:
        f_name = name.strip()
        letter = template.replace("[name]", f"{f_name}")
        file_name = f"letter_for_{f_name}"
        with open(f"./Output/ReadyToSend/{file_name}", mode="w") as file:
            file.write(f"{letter}")

print("done")




#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp