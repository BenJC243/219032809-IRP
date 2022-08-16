from matplotlib import pyplot as plt
import sys
get "https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE165553&format=file&file=GSE165553%5FSS2%2D16%2D225%5Fexpression%5Ffor%5FR%2Etab%2Egz"
get "https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE165553&format=file&file=GSE165553%5FSS2%2D16%2D227%5Fexpression%5Ffor%5FR%2Etab%2Egz"
get "https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE165553&format=file&file=GSE165553%5FSS2%2D16%2D259%5Fexpression%5Ffor%5FR%2Etab%2Egz"
get "https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE165553&format=file&file=GSE165553%5FSS2%2D16%2D303%5Fexpression%5Ffor%5FR%2Etab%2Egz"
get "https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE165553&format=file&file=GSE165553%5FSS2%2D16%2D304%5Fexpression%5Ffor%5FR%2Etab%2Egz"
fo1 = open('dir/to/csv')
fo1 = fo1.readlines()
ls1 = [] #ls1 contains ls of lists --> each list contiains a row - tab-sep.d 
for i in fo1:
    i = i.split('\t')
    ls1.append(i)

d = {}
for i in ls1:
    if 'P2RX' in i[0] and not i[0].endswith('6P'):
        c = 0
        for e in i[1:]:
            if e is i[-1]:
                e = e.replace('\n','')
            c+=int(e)
        d[i[0]] = c
        print(c, i[0])
    
d = sorted(d.items(),key=lambda x: x[0][-1])
d = dict(d)
print(d)
plt.figure(figsize=(15, 10))
plt.bar(d.keys(),d.values())
