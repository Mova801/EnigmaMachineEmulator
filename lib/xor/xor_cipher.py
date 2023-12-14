import string

# TODO: fix

def xor_letter(letter: str, key: str) -> str:
    """

    :param letter:
    :param key:
    :return:
    """
    return chr(ord(letter) ^ ord(key))


def xor_cipher(text: str, cipher_key: str) -> str:
    """

    :param text:
    :param cipher_key:
    :return:
    """
    final_text: str = ""
    for i, char in enumerate(text):
        if char not in string.ascii_letters:
            final_text += char
            continue
        cipher_letter: str = cipher_key[i % len(cipher_key)]
        final_text += xor_letter(char, cipher_letter)
    return final_text
