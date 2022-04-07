song="""by the rivers of babylon, there we sat down
yeah we wept, when we remember zion.
when the wicked carried us away in captivity
required from us a song
now how shall we sing the lord's song in a strange land"""

alphabet=dict()
for c in song:
    if c.isalpha()==False: #알파벳이니?
        continue
    c=c.lower() #소문자로 바꿈
    if c not in alphabet:
        alphabet[c]=1
    else:
        alphabet[c]+=1

print(alphabet)