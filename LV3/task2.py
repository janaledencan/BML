# Zadatak 3.4.2 Napišite programski kod koji ce prikazati sljedece vizualizacije:
# a) Pomocu histograma prikažite emisiju C02 plinova. Komentirajte dobiveni prikaz. (MISLIM DA VALJA)

# import pandas as pd
# import matplotlib.pyplot as plt

# data = pd. read_csv('data_C02_emission.csv')
# data ['CO2 Emissions (g/km)'].plot( kind ='hist', bins = 20)
# plt.show()


# b) Pomocu dijagrama raspršenja prikažite odnos izmedu gradske potrošnje goriva i emisije
# C02 plinova. Komentirajte dobiveni prikaz. Kako biste bolje razumjeli odnose izmedu
# velicina, obojite tockice na dijagramu raspršenja s obzirom na tip goriva.
  
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv( 'data_C02_emission.csv')

print(data['Fuel Type'].value_counts())

data['Fuel Type'] = data['Fuel Type'].map({'X':0, 'Z': 1, 'D': 2, 'E': 3, 'N':4})

data.plot.scatter (x='Fuel Consumption City (L/100km)' ,
                        y='CO2 Emissions (g/km)' ,
                        c='Fuel Type', cmap ="cool", s=50)
plt.show ()


# # Extract the data from the seventh column
# seventh_column = data.loc[:, 6]

# # Convert the data into numeric values
# numeric_values = pd.to_numeric(seventh_column, errors='coerce')

# Create a new DataFrame with the numeric values
# new_data = pd.DataFrame({'numeric_fuels': numeric_values})




# c) Pomocu kutijastog dijagrama prikažite razdiobu izvangradske potrošnje s obzirom na tip
# goriva. Primjecujete li grubu mjernu pogrešku u podacima?  (MISLIM DA VALJA)

# import pandas as pd
# import matplotlib.pyplot as plt

# data = pd. read_csv( 'data_C02_emission.csv')

# grouped = data.groupby ( 'Fuel Type')
# grouped.boxplot ( column =['Fuel Consumption Hwy (L/100km)'])
# data.boxplot ( column =['CO2 Emissions (g/km)'], by='Fuel Type')
# plt.show()

# d) Pomocu stupcastog dijagrama prikažite broj vozila po tipu goriva. Koristite metodu
# groupby. (VALJA)

# import pandas as pd
# import matplotlib.pyplot as plt

# data = pd. read_csv( 'data_C02_emission.csv')

# grouped = data.groupby ( 'Fuel Type')

# result=grouped['Fuel Type']
# fuel_group={}

# for group,r in result:
#     print(f"{group}:{len(r)}")
#     fuel_group[f"{group}"] = len(r)

# plt.bar(list(fuel_group.keys()),list(fuel_group.values()),color="m", width = 0.4)
# plt.show()

# e) Pomocu stupcastog grafa prikažite na istoj slici prosjecnu C02 emisiju vozila s obzirom na
# broj cilindara. (VALJA)

# import pandas as pd
# import matplotlib.pyplot as plt

# data = pd. read_csv( 'data_C02_emission.csv')

# # grouped = data.groupby('Cylinders')
# # result_cylinders=grouped['CO2 Emissions (g/km)']
# total={}

# # for group,g in result_cylinders:
# #     print(group, g)
# #     total[f"{group}"]=g


# grouped = data.groupby('Cylinders')['CO2 Emissions (g/km)'].sum()
# total=grouped
# print(grouped)
# plt.bar(grouped.keys(),grouped,width=0.4)
# plt.show()
