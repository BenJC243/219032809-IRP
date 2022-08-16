# Somatosensory neuron types identified by high-coverage single-cell RNA-sequencing and functional heterogeneity
from matplotlib import pyplot as plt
import sys
wget "https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE63576&format=file&file=GSE63576%5FDRG%5FRNA%5FSeq%2Etxt%2Egz"
#fo = open('dir/to/csv/file)

# counts' in FPKM
fo = fo.readlines()
ls = []
for i in fo:
    i = i.split('\t')
    ls.append(i)
ls1 = []
for i in ls:
    if 'P2rx' in i[0]:
        i[0] = i[0].upper()
        ls1.append(i)
d = {}
for i in ls1:
    c = 0
    for e in i[1:]:
        c += float(e)
    d[i[0]] = c
d = sorted(d.items(),key=lambda x: x[0][-1])
d = dict(d)
print(d)
plt.figure(figsize=(15, 10))
plt.bar(d.keys(),d.values())
#plt.savefig('/home/bc234/IRP_data/sc_studies/\
