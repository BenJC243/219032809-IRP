# WHISKER PLOT 2 dirs
import statistics
from matplotlib import pyplot as plt
import numpy as np
import os
import pandas as pd
max_val2 = []
max_val = []
def score(models,models2):
    dict1={}
    dict2={}
    for dir1 in os.listdir(models):
        d = os.path.join(models, dir1)
        if os.path.isdir(d):
            for file in os.listdir(d):
                if file.endswith('ranking_debug.json'):
                    ls = []
                    fo = models+file
                    fo = open(models+dir1+'/'+file)
                    fo = fo.readlines()
                    if 'monomer' in d: 
                        for i in fo[2:7]:
                            i = i.strip()
                            i = i.replace('"','')
                            i = i.replace(',','')
                            i = i.split(' ')
                            ls.append(i)
                    else:
                        for i in fo[2:27]:
                            i = i.strip()
                            i = i.replace('"','')
                            i = i.replace(',','')
                            i = i.split(' ')
                            ls.append(i)
                    ls2 = []
                    for i in ls:
                        for e in i:
                            if e is i[1]:
                                if 'monomers' not in models:
                                    e = float(e)
                                    e = e*100
                                    e = str(e)
                                    ls2.append(e)
                                else:
                                    ls2.append(e)
                    std_ls1 = sorted(ls2) # sorted list of lddt scores only
                    f = max(ls2) #highest model score of a json file
                    min1 = min(ls2)
                    diff1 = float(f)-float(min1)
                    median1 = statistics.median(std_ls1)
                    print(d,median1,' = median1')
                    print(d,f, ' = max1')
                    max_val.append([float(f),d])

                    ls3 = []
                    for i in ls2:
                        ls3.append(float(i))
                    avg = sum(ls3)/len(ls3)
                    if 'monomers' in models or 'homo' in models or 'normed' in models:
                        dict1[d[-4:]] = ls3
                    elif 'hetero' in models:
                        if 'P2X2-4-7' in d:
                            s = d[-8:]
                            s = s.replace('-','/')
                            dict1[s] = ls3
                        if '-' in d[-12:] and 'P2X2-4-7' not in d:
                            s = d[-12:]
                            s = s.replace('-','/')
                            dict1[s] = ls3
  

    for dir2 in os.listdir(models2):
        d2 = os.path.join(models2, dir2)
        if os.path.isdir(d2):
            #print(d2,'models2')
            for file in os.listdir(d2):
                if file.endswith('ranking_debug.json'):
                    ls4 = []
                    fo1 = open(models2+dir2+'/'+file)
                    fo1 = fo1.readlines()
                    if 'monomer' in d2: 
                        for i in fo1[2:7]:
                            i = i.strip()
                            i = i.replace('"','')
                            i = i.replace(',','')
                            i = i.split(' ')
                            ls4.append(i)
                    else:
                        for i in fo1[2:27]:
                            i = i.strip()
                            i = i.replace('"','')
                            i = i.replace(',','')
                            i = i.split(' ')
                            ls4.append(i)
                    ls5 = []
                    for i in ls4:
                        for e in i:
                            if e is i[1]:
                                if 'monomers' not in models:
                                    e = float(e)
                                    e = e*100
                                    e = str(e)
                                    ls5.append(e)
                                else:
                                    ls5.append(e)
                                
                    max2 = max(ls5)
                    min2 = min(ls5)
                    diff2 = float(max2)-float(min2)
                    std_ls = sorted(ls5) # sorted list of lddt scores only
                    median2 = statistics.median(std_ls)
                    print(d2,median2, ' = median2')
                    print(d2, max2, ' = max2')
                    s = max(ls5) #highest model score of a json file
                    max_val2.append([float(s),d2])
                    ls6 = [] # contains sorted list of lddt scores only in float
                    for i in ls5:
                        ls6.append(float(i))

                    if 'monomers' in models or 'homo' in models or 'normed' in models:
                        dict2[d2[-4:]] = ls6
                    elif 'hetero' in models:
                        if 'P2X2-4-7' in d2:
                            s = d2[-8:]
                            s = s.replace('-','/')
                            dict1[s] = ls6
                        if '-' in d2[-12:] and 'P2X2-4-7' not in d2:
                            s = d2[-12:]
                            s = s.replace('-','/')
                            dict1[s] = ls6

    dict1 = {'Human '+k: v for k, v in dict1.items()}
    dict2 = {'Mouse '+s: e for s, e in dict2.items()}
    dict1.update(dict2)
    dict1 = sorted(dict1.items(),key=lambda x: x[0][-1],reverse=True) # order according to last str element in key
    dict1 = dict(dict1)
    plt.rcParams["figure.figsize"] = (20, 10)
    labels, data = dict1.keys(), dict1.values()
    plt.boxplot(data,whis=100,vert=False)
    plt.yticks(range(1, len(labels) + 1), labels)
    if 'monomer' in models: 
        plt.ylabel('Monomer',fontsize=15)
        plt.xlabel('Predicted TM-score (pTM)',fontsize=15)
        data = pd.DataFrame(dict1)
        for i,d in enumerate(data):
            x = data[d]
            y = np.random.normal(i + 1, 0, len(x))
            plt.scatter(x,y)
        plt.show()
    elif 'homotrimer' in models:
        plt.ylabel('Homotrimer',fontsize=15)
        plt.xlabel('Predicted TM-score (pTM)',fontsize=15)
        data = pd.DataFrame(dict1)
        for i,d in enumerate(data):
            x = data[d]
            y = np.random.normal(i + 1, 0, len(x))
            plt.scatter(x,y)
        plt.show()        
    elif 'heterotrimer' in models:
        plt.ylabel('Heterotimer',fontsize=15)
        plt.xlabel('Predicted TM-score (pTM)',fontsize=15)
        #plt.xlim(65,90)
        data = pd.DataFrame(dict1)
        for i,d in enumerate(data):
            x = data[d]
            y = np.random.normal(i + 1, 0, len(x))
            plt.scatter(x,y)
        plt.show()
