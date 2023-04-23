import pandas


def phonetics():
    p = pandas.read_csv("data.csv")
    pd = {row.letter: row.code for (index, row) in p.iterrows()}
    converter(pd)


def converter(pd):
    word = input("Enter a word: ").upper()
    try:
        word_p = {key: value for (key, value) in pd.items() if key in word}
        word_l = [pd[x] for x in word]
    except KeyError:
        print("Only alphabets are allowed")
        converter(pd)
    else:
        print(word_l)


if __name__ == '__main__':
    phonetics()
