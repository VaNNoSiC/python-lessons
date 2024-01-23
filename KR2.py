f = open("mat_dv.txt", "r")
L=[]

L_class = ['8', '9', '10', '11']
c_8 = {'name': '', 'famil': '', 'class': 8,'alg': 0, 'geom': 0, 'max': ''}
c_9 = {'name': '', 'famil': '', 'class': 9,'alg': 0, 'geom': 0, 'max': ''}
c_10 = {'name': '', 'famil': '', 'class': 10,'alg': 0, 'geom': 0, 'max': ''}
c_11 = {'name': '', 'famil': '', 'class': 11,'alg': 0, 'geom': 0, 'max': ''}

for i in f:
    i = i.strip('\n')
    L.append(i)



max_8 = 0
max_9 = 0
max_10 = 0
max_11 = 0

for i in L:
    L1 = i.split(' ')
    print(L1)
