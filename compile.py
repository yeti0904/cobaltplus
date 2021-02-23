import os
os.system("clear")
print("Please type the filename of your Cobalt+ program")
filename = input("> ")
with open(filename) as f:
    src = f.readlines()
#print(src)
bin = []
progress = 1
error = 0
for codeln in src:
    if codeln[:5] == "print":
        if codeln[6:9] == "str":
            bin.append("ps" +str(codeln[11:]).replace("\n","") +"!")
        elif codeln[6:9] == "var":
            if not len(codeln) == 11 and not len(codeln) >= 11:
                print("ERROR at line" +str(progress) +": line not long enough")
            else:
                bin.append("pv" +codeln[11])
    elif codeln[:4] == "var.":
        if codeln[4:9] == "create":
            bin.append("vc" +codeln[11])
        if codeln[4:7] == "set":
            bin.append("vs" +codeln[9] +codeln[11:])
    else:
        error = 1
        print("ERROR at line " +str(progress) +"!")
    progress += 1
    if error != 1:
        print("Compiled line " +str(progress))

#print(bin)
#now print code
print("Converting to 1 line format..")
bin1ln = ""
for line in bin:
    bin1ln += line
print("Done! Here is your operating code to paste into LithiumPC:\n" +bin1ln)