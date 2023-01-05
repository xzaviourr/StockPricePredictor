with open('models/archives/train_log.txt') as f:
  l = []
  for lines in f:
    x = lines.split('\n\n')
    if(x!=['\n']):  
      for w in x:
        temp = w.split(': ')
        if(len(temp)==2):
          temp = temp[-1].split('\n')
          l.append(float(temp[0]))
f = []
for i in range(int(len(l)/12)):
  f.append(l[12*i:12*i+12])
print(f[0])


import matplotlib.pyplot as plt
import pandas as pd
labels = ["SUNPHARMA", "TCS", "WIPRO", "SBIN", "DRREDDY", "INFY", "POWERGRID", "CIPLA", "COALINDIA", "HDFCBANK", "BPCL", "AXISBANK"]
figure = plt.figure(figsize=(20,6))
data = pd.DataFrame(f)
for i in range(12):
  plt.plot(data[i], label=labels[i])
plt.legend(loc=0)
plt.show()