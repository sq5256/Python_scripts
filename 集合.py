def main():
    fp = open("grade.txt", 'w')
    for i in range(2):
        name = input("姓名：")
        math = int(input("数学："))
        English = int(input("英语："))
        line = name + " " + str(math) + " " + str(English) + '\n'
        fp.write(line)
    fp.close()
    ifile = open("grade.txt", "r")
    for line in ifile:
        L = line.split()
        avg = (float(L[1]) + float(L[2]))/2
        print(L[0], L[1], L[2], avg)
    ifile.close()
main()