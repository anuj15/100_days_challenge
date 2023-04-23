def send_letters():
    with open("Input/Names/invited_names.txt") as f:
        names = f.readlines()

    names = [x.replace("\n", "") for x in names]
    letters = []
    print(names)

    for i in names:
        with open("Input/Letters/starting_letter.txt") as f:
            letter_text = f.readlines()
        letter_text = [x.replace("[name]", i) for x in letter_text]
        letters.append(letter_text)

    for i in range(len(names)):
        with open(f"./Output/ReadyToSend/letter_for_{names[i].title()}.txt", 'w') as f:
            f.write("".join(letters[i]))


if __name__ == '__main__':
    send_letters()
