import pandas as pd
data = pd. read_csv ( 'data_C02_emission.csv')


# A)
data.info()
print(f"There is:{data.duplicated().sum()} duplicated values")
data.drop_duplicates()

for column in ['Make', 'Model', 'Vehicle Class', 'Transmission', 'Fuel Type']:
    data[column] = data[column].astype('category')

data.info()


# B) 

sorted_data = data.sort_values(by='Fuel Consumption City (L/100km)')
sorted_data = sorted_data.reset_index(drop=True)
print(sorted_data.head(3)[['Make', 'Model', 'Fuel Consumption City (L/100km)']])
print(sorted_data.tail(3)[['Make', 'Model', 'Fuel Consumption City (L/100km)']]) 


# C) 

engine_data=data[(data['Engine Size (L)']>= 2.5)& (data['Engine Size (L)']<=3.5)]
print(len(engine_data))

print(engine_data['CO2 Emissions (g/km)'].mean())


# D)

audi = data[(data['Make'] == 'Audi')]
print(f"{len(audi)} Audi cars")

four_cylinders_audi = audi[(audi['Cylinders']) == 4]
print(four_cylinders_audi['CO2 Emissions (g/km)'].mean())


# E) 

grouped = data.groupby('Cylinders')

for group,cylinder_group in grouped:
    print(f"Number of vehicles with {group} cylinders: {len(cylinder_group)}")
    print(f"Mean for {group} cylinders: {cylinder_group['CO2 Emissions (g/km)'].mean()}")


# F)

grouped_fuel_types = data.groupby('Fuel Type')
for group,group_data in grouped_fuel_types:
    print(group)

diesel_vehicles_mean = data[data['Fuel Type'] == 'D']['Fuel Consumption City (L/100km)'].mean()
print(diesel_vehicles_mean)
diesel_consumption_median = (data[data['Fuel Type'] == 'D'])['Fuel Consumption City (L/100km)'].median()
print(diesel_consumption_median)

petrol_consumption_mean = (data[data['Fuel Type'] == 'X'])['Fuel Consumption City (L/100km)'].mean()
petrol_consumption_median = (data[data['Fuel Type'] == 'X'])['Fuel Consumption City (L/100km)'].median()
print(petrol_consumption_mean)
print(petrol_consumption_median) 

# G) 

vehicles_wih_diesel_motor_4_cylinders = data[(data['Fuel Type'] == 'D')  &  (data['Cylinders'] == 4)]
max_city_consumption_D4 = vehicles_wih_diesel_motor_4_cylinders['Fuel Consumption City (L/100km)'].max()
result = vehicles_wih_diesel_motor_4_cylinders[vehicles_wih_diesel_motor_4_cylinders['Fuel Consumption City (L/100km)'] == max_city_consumption_D4]
print(result)

# H) 

print(len(data[data['Transmission'].str.contains('M') & ~(data['Transmission'].str.contains('AM'))]))


# I) 

print(data.corr())
