  # Raw Counts across tissues of given P2X gene 
from matplotlib import pyplot as plt
import os
gene = 'P2rx3' # ENTER P2X HERE e.g. 'P2rx3'
sub_dir = []
for dir1 in os.listdir('/home/bc234/IRP_data/MCA/MCA_tissues'):
    d = os.path.join('/home/bc234/IRP_data/MCA/MCA_tissues', dir1)
    if os.path.isdir(d):
        sub_dir.append(d)
ls = []
for dir1 in os.listdir('/home/bc234/IRP_data/MCA/MCA_tissues'):
    d = os.path.join('/home/bc234/IRP_data/MCA/MCA_tissues', dir1)
    if os.path.isdir(d):
        ls1=[]
        for file in os.listdir(d):
            ls1.append(file)
        ls.append(ls1)
ls2 = []
for i in ls:
    for e in i:
        if 'gene' in e:
            ls3 = [e]
            ls2.append(ls3)
c = 0
for i in ls:
    for e in i:
        if 'dge' in e:
            ls2[c].append(e)
            c = c + 1
c = 0
for i in ls:
    for e in i:
        if 'anno' in e:
            ls2[c].append(e)
            c = c + 1
genefiles = []
dgesfiles = []
annot = []
for i in ls2:
    for e in i:
        if 'gene' in e:
            genefiles.append(e)
        elif 'dge' in e:
            dgesfiles.append(e)
        elif 'anno' in e:
            annot.append(e)
for j,k,l,r in zip(genefiles,dgesfiles,annot,sub_dir):
    fo = open(r+'/'+j)
    print(j)
    ls = []
    for e in fo:
        e = e.strip()
        ls.append(e)
    fo.close()
    test = []
    for e in ls:
        if gene in e:
            s = ls.index(e) - 1
            test.append(e)
    for i in test:
        if gene not in i:
            print('NO P2RX3')
    fo1 = open(r+'/'+k)
    print(k)
    ls1=[]
    for e in fo1:
        e = e.strip()
        e = e.split(',')
        ls1.append(e)
    fo1.close()
    ls1.pop(0) #remove cell labels from dge file
    if len(test) > 0:
        ls1[s].pop(0) # remove index col from gene file
    
    file_len = len(ls1[1])-1 # num of samples
    print(file_len)
    fo2 = open(r+'/'+l)
    print(l)
    ls2 = []
    for i in fo2:
        i = i.strip()
        i = i.replace('"','')
        i = i.split(',')
        ls2.append(i[1])
    fo2.close()
    ls2.pop(0) # remove 'Idents.pbmc.' item
    
    if len(test) > 0:
        ls3 = []
        for i,j in zip(ls1[s],ls2):
            ls4=[]
            ls4.append(i)
            ls4.append(j)
            ls3.append(ls4)
        d1 = {}
        for i in ls3:
            if i[1] not in d1:
                d1[i[1]] = int(i[0])
            elif i[1] in d1:
                g = d1.get(i[1])
                g = g + int(i[0])
                d1[i[1]] = g
        for i in list(d1):
            e = d1.get(i)
            if e == 0:
                del d1[i]

        print(d1,'\n')
        plt.figure(figsize=(25,10))
        plt.title(r,fontsize=20)
        plt.bar(d1.keys(),d1.values())
        plt.savefig('/home/bc234/MCA/MCA_counts/'+r[24:]+'_counts'+gene+'.png')
        plt.close()
    else:
        print('NO '+gene,'\n')
