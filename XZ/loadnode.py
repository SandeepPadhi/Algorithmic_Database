import pickle
from pickling.py
dbfile=open('./nodefile','rb')
N=pickle.load(dbfile)
print(N.giveName())
dbfile.close()