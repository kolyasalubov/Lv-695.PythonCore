import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import wbdata as wb
import operator
import tkinter as tk
from tkinter import *
import requests

HEIGHT=800
WIDTH=800

indicator="NY.GDP.MKTP.PP.KD" 
all_countries=[]
country_years={}

def get_gdp(my_year, flag):
    """"This function get GDP data from wbdata"""
    print(type(my_year))
    print(type(flag))

    text.delete("1.0","end")
    try:
        year=int(my_year)
    except ValueError:
        text.insert(1.0, 'You entered incorrect data')
        return

    for item in wb.get_country():
        region=item['region']['value']
        if region!='Aggregates': 
            all_countries.append(item['iso2Code'])
    
    for item in wb.get_data(indicator=indicator):
        id=item['country']['id']
        if id in all_countries:
            country_name=item['country']['value']
            year=int(item['date'])
            value_gdp=item['value']
            if value_gdp:
                try:
                    country_years[country_name][year]=value_gdp
                except KeyError: 
                    country_years[country_name]={}
                    country_years[country_name][year]=float(value_gdp)
    
    country_values={}
    for i,j in country_years.items():
        for x,y in j.items():
            if x==int(my_year):
                    country_values[i]=float(y)
    
    if country_values=={}:
        text.insert(1.0, 'No data for this period')
    else:
        gdp_info=f'Country: GDP based on PPP by {my_year}, trln $\n'
        gdp_info+='-------------------------------------\n'
        for i,j in country_values.items():
            gdp_info+=f'{i}: {str(round((j*1e-12),4))}\n'
        gdp_info+='-------------------------------------\n'
        if flag==0:
            text.insert(1.0, gdp_info)
            sorted_d = sorted(country_values.items(), key=operator.itemgetter(1), reverse = True)
            sorted_d=sorted_d[0:10]

            #draw a diagram
            x=[]
            y=[]
            for _tuple in sorted_d:
                country_name=_tuple[0]
                pokazn=_tuple[1]
                y.append(pokazn)
                x.append(country_name)
 
            def trillions(x, pos):
                """This function converts values to trillions for the label on the vertical axis"""
                return f'$ {x * 1e-12} Trln'

            formatter = FuncFormatter(trillions)

            fig, ax = plt.subplots()
            ax.yaxis.set_major_formatter(formatter)
            plt.xlabel('Country', fontsize=10)
            plt.ylabel('GDP', fontsize=10)
            plt.bar(x, y)
            plt.title(f'GDP from World Bank by {my_year}, trln $', fontsize=20)

            for i, v in enumerate(x):
                val=round(y[i]/10**12,1)
                plt.text(i,y[i]/2, val, color='white', ha='center', fontweight='bold', fontsize=18)
        
            plt.show()

        else:
            text.insert(1.0, "Information saved in the file GDP_info.txt")
            with open('GDP_info.txt', mode='a', encoding='utf-8') as f:
                f.write(gdp_info)
                
root=tk.Tk()

canvas=tk.Canvas(root, height=HEIGHT, width=WIDTH)
print(type(canvas))
root.title("GDP based on purchasing power parity by selected year.")
canvas.pack()

frame=tk.Frame(root,bg="#87cefa",bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

label=tk.Label(frame, text='Enter the year:', font=('Courier',18), anchor='w')
label.place(relx=0, rely=0, relwidth=1, relheight=1)

entry_field=tk.Entry(frame, font=('Courier',18))
entry_field.place(relx=0.4, rely=0, relwidth=0.65, relheight=1)

button1=tk.Button(frame,
                text="Get GDP",
                bg="gray", fg="white",
                font=('Courier',12),
                command=lambda: get_gdp(entry_field.get(),0))
button1.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame=tk.Frame(root, bg='#90c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.8, relheight=0.6,anchor='n')

text=tk.Text(lower_frame, font=('Courier',18))
text.place(relx=0, rely=0, relwidth=1, relheight=1)

scrollbar = tk.Scrollbar(lower_frame, command=text.yview)
scrollbar.pack(side=tk.RIGHT)
text.config(yscrollcommand=scrollbar.set)

button2=tk.Button(root,
                text="Save results",
                bg="gray", fg="white",
                font=('Courier',12),
                command=lambda: get_gdp(entry_field.get(),1))
button2.place(relx=0.35, rely=0.85, relwidth=0.3, relheight=0.1)

root.mainloop()