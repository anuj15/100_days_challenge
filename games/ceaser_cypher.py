from data import alphabets


class Ceaser:
    CODE_UNITS = 3

    def encode(self, string_to_encode):
        crypto_text = ""
        for i in string_to_encode:
            if i in alphabets:
                index = alphabets.index(i)
                new_index = (index + self.CODE_UNITS) % 26
                crypto_text += alphabets[new_index]
            else:
                crypto_text += i
        return crypto_text

    def decode(self, string_to_decode):
        crypto_text = ""
        for i in string_to_decode:
            if i in alphabets:
                index = alphabets.index(i)
                new_index = (index + 26 - self.CODE_UNITS) % 26
                crypto_text += alphabets[new_index]
            else:
                crypto_text += i
        return crypto_text


if __name__ == '__main__':
    ceaser = Ceaser()
    word = input("Enter a word or phrase to encode: ")
    encoded_text = ceaser.encode(word)
    print(f"The encoded phrase is: {encoded_text}")
    decode = input("Do you wish to decode your phrase? Type 'yes' or 'no': ")
    if decode == 'yes':
        decoded_text = ceaser.decode(encoded_text)
        print(f"The decoded phrase is: {decoded_text}")
