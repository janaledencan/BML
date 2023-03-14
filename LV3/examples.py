
#3.1
# import pandas as pd
# import numpy as np
# s1 = pd. Series (['crvenkapica', 'baka', 'majka', 'lovac', 'vuk'])
# print (s1)
# s2 = pd. Series (5., index =['a','b','c','d','e'], name = 'ime_objekta')
# print (s2)
# print (s2['b'])
# s3 = pd. Series (np. random . randn (5))
# print (s3)
# print (s3[3])


#3.2
# import pandas as pd
# import numpy as np
# data = {'country ': ['Italy','Spain','Greece','France','Portugal'],
# 'population': [59 , 47 , 11 , 68 , 10 ],
# 'code': [39 , 34 , 30 , 33 , 351 ]}
# countries = pd. DataFrame (data , columns =['country', 'population', 'code'])
# print ( countries )


#3.4
# import pandas as pd
# data = pd. read_csv ( 'data_C02_emission.csv')
# # konvertiranje kategorickih velicina u tip category
# print ( len ( data ))
# print ( data )
# print ( data . head (5))
# print ( data . tail (3))
# print ( data . info ())
# print ( data . describe ())
# print ( data . max ())
# print ( data . min ())


#3.5
# import pandas as pd
# import numpy as np
# data = pd. read_csv ( 'data_C02_emission.csv')
## izdvajanje pojedinog stupca
# print ( data ['Cylinders'])
# print ( data . Cylinders )
## izdvajanje vise stupaca
# print ( data [['Model','Cylinders']])
## izdvajanje redaka koristenjem iloc metode
# print ( data . iloc [2:6, 2:7])
# print ( data . iloc [:, 2:5])
# print ( data . iloc [:, [0,4,7]])
# logicki uvjeti na pojedine stupce
# print ( data . Cylinders > 6)
# print ( data [ data . Cylinders > 6])
# print ( data [( data ['Cylinders'] == 4) & ( data ['Engine Size (L)'] > 2.4)]. Model
# )
## dodavanje novih stupaca
# data ['jedinice'] = np. ones ( len ( data ))
# data ['large'] = ( data ['Cylinders'] > 10)
# print(data)


#3.6
# import pandas as pd
# import numpy as np
# data = pd. read_csv ( 'data_C02_emission.csv')
# new_data = data . groupby ( 'Cylinders')
# print ( new_data . count ())
# print ( new_data . size ())
# print ( new_data . sum ())
# print ( new_data . mean ())


#3.7
# import pandas as pd
# data = pd. read_csv ( 'data_C02_emission.csv')
# # provjera koliko je izostalih vrijednosti po svakom stupcu DataFramea
# print ( data . isnull (). sum ())
# # brisanje redova gdje barem vrijednost jedne velicine nedosta je
# data . dropna ( axis =0)
# # brisanje stupaca gdje barem jedna vrijednost nedostaje
# data . dropna ( axis =1)
# # brisanje dupliciranih redova
# data . drop_duplicates ()
# # kada se obrisu pojedini redovi potrebno je resetirati indekse retka
# data = data . reset_index ( drop = True )
# print(data)


#3.8
# import pandas as pd
# import matplotlib.pyplot as plt
# data = pd. read_csv( 'data_C02_emission.csv')
# plt.figure ()
# data ['Fuel Consumption City (L/100km)'].plot( kind ='hist', bins = 20)
# plt.figure ()
# data ['Fuel Consumption City (L/100km)'].plot( kind ='box')
# plt.show ()


#3.9
# import pandas as pd
# import matplotlib.pyplot as plt
# data = pd. read_csv( 'data_C02_emission.csv')
# grouped = data . groupby ( 'Cylinders')
# grouped . boxplot ( column =['CO2 Emissions (g/km)'])
# data . boxplot ( column =['CO2 Emissions (g/km)'], by='Cylinders')
# plt . show ()



#3.10
# import pandas as pd
# import matplotlib . pyplot as plt
# data = pd. read_csv ( 'data_C02_emission.csv')
# data . plot . scatter (x='Fuel Consumption City (L/100km)' ,
#                         y='Fuel Consumption Hwy (L/100km)' ,
#                         c='Engine Size (L)', cmap ="hot", s=50)
# plt . show ()


#3.11
import pandas as pd
data = pd. read_csv ( 'data_C02_emission.csv')
print ( data.corr(numeric_only=True))
#print ( data.max(numeric_only=True))