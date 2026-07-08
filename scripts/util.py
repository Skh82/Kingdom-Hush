import numpy as np

def info_reader(file):
    f = open(file, "r")
    a = f.readlines()
    lsst = list()
    lst = list()
    tot_arr = list()
    for item in a:
        lsst.append(item.strip())
    x1, x2 = map(int, lsst[0].split())
    for i in range(x1):
        for j in range(x2):
            lst.append(list(map(int, lsst[(i)*x2+(j+1)].split())))
        myarr = np.array(lst)
        tot_arr.append(myarr)
        lst = list()
    lst2 = list(map(np.linalg.det, tot_arr))
    return lst2, tot_arr

def func(lst:list, tot_arr):
    a = lst[0] * lst[1]
    ind1, ind2 = 0, 1
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if a < lst[i] * lst[j]:
                a = lst[i] * lst[j]
                ind1, ind2 = i, j
    arr_lst = [tot_arr[ind1], tot_arr[ind2]]
    arr_lst.sort(key=lambda x:np.linalg.det(x), reverse=True)
    mult = np.dot(arr_lst[0], arr_lst[1])
    inve = np.linalg.inv(mult)
    return inve

lst2, tot_arr = info_reader('input2.txt')
inve = func(lst2, tot_arr)
for row in inve:
    line = ""
    for itm in row:
        line += f"{itm:.3f} "
        if len(line.split()) == len(row):
            print(line.strip())  
            line = ""
    if line.strip(): 
        print(line.strip())