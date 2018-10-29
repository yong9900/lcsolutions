with open('streetin.txt', 'r') as infile:
    with open('streetout.txt', 'w') as outfile:
        data = infile.readline().split(' ')
        a,b = int(data[0]), int(data[1])
        if a==b:
            outfile.write('0')
        else: 
            c = (a-b)//(b+1)
            d = (a-b)%(b+1)
            if d==0:
                outfile.write('%d' % c)
            else:
                outfile.write('%d' % (c+1) )
