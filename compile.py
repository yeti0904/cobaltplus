import os
os.system("clear")
print("Please type the filename of your Cobalt+ program")
filename = input("> ")
src = open(filename).read().splitlines()
#print(src)
binvar = ""
bin = []
progress = 0
error = 0
for codeln in src:
    if codeln[:10] == "print str ":
        bin.append("ps" +codeln[10:] +"!")
    elif codeln[:10] == "print var ":
        bin.append("pv" +codeln[10:] +"!")
    elif codeln[:11] == "var.create ":
        bin.append("vc" +codeln[11:] +"!")
    elif codeln[:8] == "var.set ":
        findprogress = 1
        while not findprogress == len(codeln):
            if codeln[findprogress] == ",":
                commalocation = findprogress
            findprogress += 1

        bin.append(str("vs" +codeln[8:findprogress] +"!" +codeln[findprogress +1:]).replace(",","!"))
    elif codeln[:10] == "var.input ":
        bin.append("vi" +codeln[10:] +"!")
    elif codeln == "console.clear":
        bin.append("cc")
    elif codeln == "console.hide":
        bin.append("ch")
    elif codeln == "console.show":
        bin.append("cs")
    elif codeln[:7] == "run.me ":
        bin.append("rm" +codeln[7:] +"!")
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
    bin1ln += line.replace("\n","")
print("Done! Here is your operating code to paste into LithiumPC:\n" +bin1ln)