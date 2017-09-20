typeword = eval(input("word to translate into pig latin? "))
firstletter = typeword[0]
restofword = typeword[1:]
piglatinword = restofword + firstletter + "ay"
print (piglatinword)
