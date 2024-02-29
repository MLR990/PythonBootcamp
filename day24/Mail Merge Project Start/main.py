PLACEHOLDER = "[name]"
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        clean_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, clean_name)
        with open(f"./Output/ReadyToSend/letter_for_{clean_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter )
