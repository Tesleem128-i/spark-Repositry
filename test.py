import pandas as pd 
pd.DataFrame({"fish":[100,200,300,400],
              "egg":[400,300,200,100]},
             index=['product1','product2',"product3","product4"])
import matplotlib as plt
x = [100,200,300,400]
y = [400,300,200,100]
plt.plot(x,y,color="blue",marker="o",linstyle="--",alpha=0.5)
plt.xlabel("fish")
plt.ylabel("egg")
plt.title("ppt")
plt.show()