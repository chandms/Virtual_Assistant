import wikipedia

while True:
    my_input = input("Q : ")
    # wikipedia.set_lang("bn")
    print (wikipedia.summary(my_input, sentences=2))
