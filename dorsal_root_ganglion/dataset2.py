from matplotlib import pyplot as plt
import sys
wget "https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE59739&format=file&file=GSE59739%5FDataTable%2Etxt%2Egz"
#fo = open('dir/to/csv/file')
fo = fo.readlines()
ls = []
for i in fo:
    i = i.split('\t')
    ls.append(i)

d = {}
for i in ls:
    if 'P2rx' in i[0]:
        i[0] = i[0].upper()
        c = 0
        for s,e in zip(i,ls[4]):
            if 'cell' in e and e.startswith('c'):
                c += float(s)
        d[i[0]] = c
        print(i[0],c)
d = sorted(d.items(),key=lambda x: x[0][-1])
d = dict(d)
plt.figure(figsize=(15, 10))
plt.bar(d.keys(),d.values())
plt.ylabel('Total Counts',fontsize=15)
plt.xlabel('P2X Gene',fontsize=15)
#plt.savefig('/home/bc234/IRP_data/sc_studies/\
