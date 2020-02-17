import math
import random
import datetime

random.seed(datetime.datetime.now())

asistens = []
praktikans = []
total_as = 0
total_prak = 0

f = open('asistens.txt', 'r')
for line in f:
    line = line.rstrip().split(';')
    asistens.append({'kelompok':line[0], 'jml':int(line[1])})
    total_as += int(line[1])

f = open('praktikans.txt', 'r')
for line in f:
    line = line.rstrip().split(';')
    jml = int(line[1])
    for i in range(jml):
        praktikans.append(line[0]+str(i+1))
    total_prak += jml

maksimal = math.ceil(total_prak/total_as)
minimal = math.floor(total_prak/total_as)
plot = {}

for asisten in asistens:
    for i in range(asisten['jml']):
        prak_plot = []
        for j in range(3):
            #randomize
            randval = random.randint(0,len(praktikans))
            while(praktikans[randval-1][0] == asisten['kelompok']):
                randval = random.randint(0,len(praktikans))

            #assign
            prak_plot.append(praktikans[randval-1])
            del praktikans[randval-1]
        plot[asisten['kelompok']+str(i+1)] = prak_plot

for prak in praktikans:
    randval = random.randint(0,5)
    kelompok = chr(65+randval)
    while(prak[0] == kelompok):
        randval = random.randint(0,5)
        kelompok = chr(65+randval)
    randval = random.randint(1,4)
    while(len(plot[kelompok+str(randval)])>minimal):
        randval = random.randint(1,4)
    plot[kelompok+str(randval)].append(prak)

f = open('output.csv', 'w')
f.writelines('kelompok;asisten;\n')
for p in plot:
    for prak in plot[p]:
        f.writelines(prak+';'+p+';\n')
f.close()