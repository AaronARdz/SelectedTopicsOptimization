import math
import pandas as pd

data = {
    "Xn": [],
    "Xn / mod": [],
    "Xn + 1": []
}

def getRtgNumbers(a,Xn,mod,c):

    if(c < 0):
        c = 0

    n = int(mod / 4)
    rtg_list = []
    rtg_str = []

    for i in range(n - 1):

        if i == 0:
            temp = (a * Xn + c)
            mod_m = (temp % mod)
            data["Xn"].append(Xn)
            Xn = mod_m
            data["Xn / mod"].append(f'{Xn}/{mod}')
            data["Xn + 1"].append(Xn)

        temp = (a * Xn + c)
        mod_m = (temp % mod)
        data["Xn"].append(Xn)
        Xn = mod_m
        data["Xn / mod"].append(f'{Xn}/{mod}')
        data["Xn + 1"].append(Xn)

    return pd.DataFrame(data)


#1 results = getRtgNumbers(8,15,100,16)

results = getRtgNumbers(50,13,64,17)

#3  results = getRtgNumbers(5,7,64,0)

#4 results = getRtgNumbers(11,9,128,0)

print(results)