print ("Enter your list of items to buy line by line and once done press ctrl + d" ) 
glist = {}
#loop
while True:
    try:
        item = input().lower()
        if item in glist:
            glist[item] += 1
        else:
            glist[item] = 1
    except EOFError:
        break

for key in sorted(glist):
   print (glist[key], key.upper())


