# GENE-CENTRIC PLOTS
genes = []
dict1 = {}
count = 0
file_ls = []
import matplotlib.pyplot as plt
import os
gene = 'P2RX3' # ENTER P2X HERE e.g. 'P2RX3'
print(gene)
for file in os.listdir('/home/bc234/IRP_data/GTEx/tissue_samples_csv2'):
    fo = open('/home/bc234/IRP_data/GTEx/tissue_samples_csv2/'+file)
    count = count + 1
    print(count)
    print(len(file_ls))
    fo1 = fo.readlines()
    fo.close()
    ls = []
    for i in fo1:
        i = i.strip()
        i = i.split('\t')
        ls.append(i)
    ls = ls[3:]
    for i in ls:
        if gene in i[2]:
            sum1 = 0
            for e in i:
                if e!=i[0] and e!=i[1] and e!=i[2]:
                    sum1 = sum1 + float(e)
                    if e is i[-1]:
                        genes.append(sum1)
                        file = file.replace('.csv','')
                        if 'esophagus_gastroesophageal_junction' in file:
                            file = file.replace('esophagus_','')
                        if 'nucleus_accumbens_basal_ganglia' in file:
                            file = file.replace('_basal_ganglia','')
                        if 'small_intestine_terminal_ileum' in file:
                            file = file.replace('terminal_','')
                        if '_' in file:
                            file = file.replace('_',' ')
                        if 'ebv-transformed' in file:
                            file = file.replace('ebv-transformed ','')
                        if 'brain' in file:
                            file = file.replace('brain','')
                        if 'lower' in file:
                            file = file.replace('lower','')
                        dict1[file] = sum1
gene_keys = sorted(dict1,key=dict1.get,reverse=True)[:10]
gene_vals = sorted(dict1.values(),reverse=True)[:10]
print(dict1)

    # LOG --> y lim of 10^3
plt.figure(figsize=(20,10))
#plt.title('P2X3',fontsize=15)
plt.yscale('log')
plt.ylim(10**3,1000000)
plt.xlabel('Tissue',fontsize=15)
plt.ylabel('Total counts (Log10)',fontsize=15)
plt.bar(gene_keys,gene_vals)
#plt.savefig('/home/bc234/IRP_data/GTEx/top10_final/'+gene+'_top10_10^3.png')
plt.show()
