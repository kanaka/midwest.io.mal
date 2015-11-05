#!/usr/bin/env python

import sys
import numpy as np
import matplotlib.pyplot as plt

# These are the "Tableau 20" colors as RGB.    
tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),    
             (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),    
             (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),    
             (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),    
             (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)] 

# Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.    
for i in range(len(tableau20)):    
    r, g, b = tableau20[i]    
    tableau20[i] = (r / 255., g / 255., b / 255.)  

syntax_names = ['C', 'Algol', 'Lisp', 'ML', 'Python', 'Stack', 'JSON', 'OTHER']
syntax_colors = {'C': tableau20[4],
                 'Algol': tableau20[6],
                 'Lisp': tableau20[0],
                 'ML': tableau20[10],
                 'Python': tableau20[8],
                 'Stack': tableau20[18],
                 'JSON': tableau20[15],
                 'OTHER': tableau20[2]}
type_names = ['Static', 'Dynamic', 'OTHER']
type_colors = {'Static': tableau20[1],
               'Dynamic': tableau20[3],
               'OTHER': tableau20[13]}

# read CSV data file
durl = 'language_data.csv'
rdata = np.genfromtxt(durl,dtype='S12,S10,S12,f,f,f',
                      delimiter=' , ',autostrip=True,names=True,
                      comments=";")

data = []
for d in rdata:
    data.append({'name': d[0],
                 'syntax': d[1],
                 'type_checking': d[2],
                 'plpc': d[3],
                 'perf': d[4],
                 'size': d[5]})

# rewrite PLPC ranking
data.sort(key=lambda x: x['plpc'], reverse=True)
for idx in range(len(data)): data[idx]['plpc'] = idx

# rewrite performance ranking
data.sort(key=lambda x: x['perf'])
for idx in range(len(data)):
    if data[idx]['perf'] > 0:
        data[idx]['perf'] = idx

# Plot data
for d in data:
    sct = plt.scatter(d['plpc'], d['perf'],
                      s=d['size'],
                      c=type_colors[d['type_checking']],
                      edgecolor=syntax_colors[d['syntax']],
                      linewidths=3)
    sct.set_alpha(0.75)

    # Labels
    plt.text(d['plpc'], d['perf'], 
             d['name'],size=11,
             verticalalignment='center',
             horizontalalignment='center')

# Legends
p1 = []
for s in syntax_names:
    p1.append(plt.scatter(None,None,
                          s=100, linewidths=2,
                          c='w',
                          edgecolor=syntax_colors[s],
                          label=s))

###p2 = []
###for t in type_names:
###    p2.append(plt.scatter(None,None,
###                          s=100,
###                          c=type_colors[t],
###                          edgecolor='w',
###                          label=t))
###
###p3 = []
####loc_sizes = [500, 1000, 1500]
###loc_sizes = [1000]
###loc_names = ["1 kLOC"]
###for sz in loc_sizes:
###    p3.append(plt.scatter(None,None,
###                          s=sz,
###                          c='grey',
###                          edgecolor='w',
###                          label=sz))
###
###legend1 = plt.legend(p1, syntax_names, title="Syntax Family", loc="lower right")
###legend2 = plt.legend(p2, type_names, title="Type Discipline", loc="upper left")
####legend3 = plt.legend(p3, loc_names, title="Radius = Code Size\n(excluding comments/blanks)", loc="lower left",
####                     prop = {'size': 20})
####legend3 = plt.legend(p3, loc_names, title="Radius = Code Size\n(excluding comments/blanks)", loc="lower left")
###legend3 = plt.legend([], [], title="Radius = Code Size\n(excluding comments/blanks)", loc="lower left")
###plt.gca().add_artist(legend1)
###plt.gca().add_artist(legend2)
###plt.gca().add_artist(legend3)

plt.xlabel('Increasing Popularity (PLPC: langpop.corger.nl) -->')
plt.xticks([])
plt.ylabel('Increasing Performance (make perf) -->')
plt.yticks([])
plt.show()
