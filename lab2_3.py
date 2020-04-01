import os

musicd = r'music'
listenf = r'music\listen.txt'

try:
    with open(listenf, 'r') as f:
        names = f.readlines()
except IOError as err:
    print(err)
    names = []

names = list(map(lambda x: x.rstrip(), names)) #названия из файла

namef = os.listdir(musicd)
namef = [name for name in namef if name.endswith('.mp3')] #названия сущ. *.mp3

tuplenames = []

for i in range(len(names)):
    for j in range(len(names)):
        if names[i][4:len(names[i])-8] == namef[j][:len(namef[j])-4]:
            tuplenames.append((namef[i],names[j]+'.mp3'))

for naz1,naz2 in tuplenames:
    naz1 = os.path.join(musicd,naz1)
    naz2 = os.path.join(musicd,naz2)
    if os.path.exists(naz1):
        os.rename(naz1, naz2)
