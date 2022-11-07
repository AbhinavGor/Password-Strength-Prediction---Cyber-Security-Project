# invert password munging
from markupsafe import string


def invert_munge(word: string):
    word = word.replace("@", "a")
    word = word.replace("8", "b")
    word = word.replace("(", "c")
    word = word.replace("6", "d")
    word = word.replace("3", "e")
    word = word.replace("#", "f")
    word = word.replace("9", "g")
    # word = word.replace("#", "h")
    word = word.replace("1", "i")
    word = word.replace("!", "i")

    word = word.replace("<", "k")
    # word = word.replace("1", "l")
    word = word.replace("0", "o")
    word = word.replace("9", "q")
    word = word.replace("5", "s")
    word = word.replace("$", "s")
    word = word.replace("+", "t")
    word = word.replace(">", "v")
    word = word.replace("2u", "w")
    word = word.replace("%", "x")
    word = word.replace("?", "y")
    # print(word)
    return word


# newpass = "@n93l"
# newpass=input("Enter new password: ")
# invert_munge(word=newpass)
