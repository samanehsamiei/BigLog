x=open('C:/access_log_Jul95.txt','r')
out=open('C:/result1,4.txt','w')
i=0
while 1:
    i=i+1
    line = x.readline()
    if line=='':
        break
    splitt = line.split("- -")
    firstcolumn = splitt[0].replace(" ", "")
    splittt = splitt[1].split('"')
    secoundcolum = splittt[2]
    ss = secoundcolum.split(" ")
    out.write(str(firstcolumn))
    out.write('|')
    out.write(str(ss[1]))
    out.write("\n")