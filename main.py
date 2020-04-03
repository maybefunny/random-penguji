import math
import random
import datetime
from operator import itemgetter

random.seed(datetime.datetime.now())

asistens = []
praktikans = []
kelompoks = []
total_as = 0
total_prak = 0

f = open('asistens.txt', 'r')
for line in f:
    line = line.rstrip().split(';')
    kelompoks.append(line[0])
    asistens.append({'kelompok':line[0], 'jml':int(line[1])})
    total_as += int(line[1])

f = open('praktikans.txt', 'r')
for line in f:
    line = line.rstrip().split(';')
    praks = line[1].rstrip().split(',')
    for i in praks:
        praktikans.append(line[0]+i)
    total_prak += len(praks)

maksimal = math.ceil(total_prak/total_as)
minimal = math.floor(total_prak/total_as)
plot = {}

print('>>assigning praktikans to asisten')
for asisten in asistens:
    for i in range(asisten['jml']):
        prak_plot = []
        for j in range(minimal):
            #randomize
            randval = random.randint(0,len(praktikans))
            while(praktikans[randval-1][0] == asisten['kelompok']):
                randval = random.randint(0,len(praktikans))

            #assign
            prak_plot.append(praktikans[randval-1])
            del praktikans[randval-1]
        plot[asisten['kelompok']+str(i+1)] = prak_plot

print('>>assigning last {} praktikans to asisten'.format(len(praktikans)))
for prak in praktikans:
    randval = random.randint(0,5)
    kelompok = chr(65+randval)
    while(prak[0] == kelompok):
        randval = random.randint(0,5)
        kelompok = chr(65+randval)
    randval = random.randint(1,4)
    while(len(plot[kelompok+str(randval)])>minimal):
        randval = random.randint(0,5)
        kelompok= chr(65+randval)
        while(prak[0] == kelompok):
            randval = random.randint(0,5)
            kelompok= chr(65+randval)
        randval = random.randint(1,4)
    plot[kelompok+str(randval)].append(prak)

plot_per_kelas = {}

for kel in kelompoks:
    plot_per_kelas[kel] = []
    for p in plot:
        for prak in plot[p]:
            if(prak[0] == kel):
                plot_per_kelas[kel].append([prak,p])

for kel in kelompoks:
    plot_per_kelas[kel] = sorted(plot_per_kelas[kel],key=itemgetter(0))

print('>>writing result to output file')
f = open('output.csv', 'w')
for p in plot_per_kelas:
    f.writelines('kelompok;asisten;\n')
    for plot in plot_per_kelas[p]:
        f.writelines(plot[0]+';'+plot[1]+';\n')
    f.writelines('\n')
print('done')
f.close()
