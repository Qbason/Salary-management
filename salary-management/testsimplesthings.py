import tkinter as tk
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


data2 = {'Year': [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010],
         'Unemployment_Rate': [9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]
        }
data3 = {'Year': [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010],
         'Unemployment_Rate': [10,12,8,7.82,6.9,7,6.55,6.92,5.5,6.93]
        }

df2 = DataFrame(data2,columns=['Year','Unemployment_Rate'])



#root= tk.Tk() 
  
figure2 = plt.Figure(figsize=(5,4), dpi=100)
ax2 = figure2.add_subplot(111)
ax2.plot(data2["Year"],data2["Unemployment_Rate"],color='g')
ax2.plot(data2["Year"],data3["Unemployment_Rate"],color='r')

plt.show()

#scatter2 = FigureCanvasTkAgg(figure2,root)
#scatter2.get_tk_widget().grid(row=0,column=0,sticky="nsew")



# line2 = FigureCanvasTkAgg(figure2, root)
# line2.get_tk_widget().grid(row=0,column=1,sticky="nsew")
# df2 = df2[['Year','Unemployment_Rate']].groupby('Year').sum()
# df2.plot(kind='line', legend=True, ax=ax2, color='r',marker='o', fontsize=10)
# ax2.set_title('Year Vs. Unemployment Rate')


#root.mainloop()