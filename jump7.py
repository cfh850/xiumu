for i in range(1,101):
    string='{}'.format(i)
    a=int(string[0])
    b=int(string[-1])
    if i%7==0 or a==7 or b==7:
        continue
    else:
        print(i)
