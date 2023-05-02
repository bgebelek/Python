#Edabit - The Karaca's Encryption Algorithm 


class KaracaEncrypt:
    def __init__(self, word):
        self.word = word

    def cipher_text(self):
        if self.word.islower():
            reverse = self.word[-1::-1]
            reverse_list = [character for character in reverse]
            reverse_list_copy = reverse_list.copy()
            vowels = {
                "a": "0",
                "e": "1",
                "i": "2",
                "o": "2",
                "u": "3"
            }
            for index, character in enumerate(reverse_list_copy):
                if character in vowels:
                    reverse_list[index] = vowels[character]
            return "".join(reverse_list) + "aca"
        else:
            return "Error: Input must be lowercase"


test = KaracaEncrypt("alpaca")
print(test.cipher_text())
