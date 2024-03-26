from wonderwords import RandomWord

while True:
    r = RandomWord()

    wordRandom = r.word()
    print(wordRandom)
    wordType = input("Type: ")


    print("Success\n\n" if wordRandom == wordType else "Fail\n\n")
