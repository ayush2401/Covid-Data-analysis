# %%
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Sample Data.csv")
x = ['0-9','10-19','20-29','30-39','40-49' , '50-59','60-69' , '70-79' , '80 above']
age = data.iloc[:,2]
disease = ['Rhinorrhea','breathing' , 'Odynophagia' , 'diarrhoea' , 'Asthma' , 'Heart Disease' , 'Diabetes' , 'Hyper Tension' , 'Fatigue']
positives = [0]*9
a = data.iloc[:,3]
MAX = 49

def show():
    plt.legend()
    plt.show()

for i in range(MAX):
    if a[i] == "YES":
        positives[age[i]//10] += 100/49;
    
for i in range(7 , 16):
    dy = data.iloc[:,i]
    y = [0]*9
    for j in range(MAX):
        if dy[j] == "YES":
            y[age[j]//10] += 1
    
    for j in range(9):
        y[j] = (100 * y[j]) / MAX
    plt.plot(x , y , label=disease[i-7])
    # show()
plt.xlabel("age")
plt.ylabel(" % of symptomatic covid-19 cases")    
show()
   





        




# %%
plt.plot(x , positives)
plt.xlabel("age")
plt.ylabel("% of covid-19 cases")
show()


