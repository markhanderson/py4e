# fname = input('Enter File: ')
# if len(fname) < 1 : fname = 'clown.txt'
# hand = open(fname)
#
# di = dict()
# for lin in hand:
#     lin = lin.rstrip()
#     # print(lin)
#     wds = lin.split()
#     # print(wds)
#     for w in wds:
#         if w in di :
#             di[w] = di[w] + 1
#             print('**EXISTING**')
#         else:
#             di[w] = 1
#             print('**NEW**')
#         print(w,di[w])
#
# print(di)




fname = input('Enter File: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    # print(lin)
    wds = lin.split()
    # print(wds)
    for w in wds:
        #print('**',w,di.get(w,-99))
        #if the key is not there the count is zero
        # oldcount = di.get(w,0)
        # print(w,'old',oldcount)
        # newcount = oldcount + 1
        # di[w] = newcount
        # idiom: retreive/create/update counter
        di[w] = di.get(w,0) + 1
        # print(w,'new',newcount)
        # vprint(w,'new',di[w])

        # if w in di :
        #     di[w] = di[w] + 1
        # else:
        #     di[w] = 1
        # print(w,di[w])

#print(di)

#now we want to find the most common word
largest = -1
theword = None
for k,v in di.items() :
    if v > largest :
        largest = v
        theword = k #capture/remember the word that was largest

print(theword, largest)
