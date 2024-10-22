from string import punctuation

text = "Florin Rădoi, inginer și fondator al firmei Stratos Aerospace Technologies, spune la rândul său că o astfel de țintă de mici dimensiuni este greu de identificat!"
print(len(text))

sir_1 = text[0:81]
print("sirul 1: ", sir_1)

sir_2 = text[81:161]
print("sir 2: ", sir_2)

# sir 1

print(sir_1.upper())
print(sir_1.strip())

#sir 2
invers = sir_2[::-1]
print(invers)

punctuation = ['.', ',','!','?']
for i in punctuation:
    invers = invers.replace(i, "")
print("sirul inversat", invers)
print(invers.capitalize())

final = sir_1 + invers
print(sir_1 + " " + invers)




#sir_1 = text[::-1]
#print(sir_1)
