def goat_latin(sentense: str):
    print("---")
    vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
    print(sentense)
    words = sentense.split(" ")
    rst = []
    index = 1
    for word in words:
        surfix =  "ma" + "a" * index
        if word[0] in vowels:
            rst.append(word + surfix)
        else:
            word_list = list(word)
            rst.append( "".join(word_list[1:]) + word[0] + surfix)
        index += 1
        
    return " ".join(rst)

print(goat_latin("I speak Goat Latin"))

print(goat_latin("The quick brown fox jumped over the lazy dog"))