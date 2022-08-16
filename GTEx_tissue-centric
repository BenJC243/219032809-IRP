# TOTAL P2X COUNTS (tissue-centric) --> LOG NORM
file_ls = []
import matplotlib.pyplot as plt
import os
for file in os.listdir('/home/bc234/IRP_data/GTEx/tissue_samples_csv2'):
    fo = open('/home/bc234/IRP_data/GTEx/tissue_samples_csv2/'+file)
    file_ls.append(file)
    print(len(file_ls))
    fo1 = fo.readlines()
    fo.close()
    ls = []
    for i in fo1:
        i = i.strip()
        i = i.split('\t')
        ls.append(i)

    ls.pop(0)
    ls.pop(0)
    ls.pop(0)
    sub = 'P2RX'
    dict1 = {}
    for i in ls:
        if sub in i[2]:
            sum1 = 0
            for e in i:
                if e!=i[0] and e!=i[1] and e!=i[2]:
                    sum1 = sum1 + float(e)
                dict1[str(i[2])] = sum1
    
    plt.figure(figsize=(25,10))
    plt.title(file)
    plt.yscale('log')
    plt.ylim(1000,1000000) # lowerbound of 10^3
    plt.bar(dict1.keys(),dict1.values())
    plt.show()
    #plt.savefig(file+'_p2xcountsLOGNORM_10^3.png')
    #plt.close()
