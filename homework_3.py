import pandas as pd

columns = ['name', 'landmass', 'zone', 'area', 'population', 'language', 'religion', 'bars', 'stripes', 
           'colours', 'red', 'grenn', 'blue', 'gold', 'white', 'black', 'orange', 'mainhue', 'circles',
           'crosses', 'saltires', 'quarters', 'sunstars', 'crescent', 'triangle', 'icon', 'animate',
           'text', 'topleft', 'botright']

df = pd.read_csv('flag.data', names = columns)


north_america_countries = (df['landmass'] == 1).sum()
print("North American Countries: " + str(north_america_countries))
print()

"""
Calling on df[landmass] selects just the landmass column and counts each of the countries who
are a part of a certain landmass. So it individually counts how many countries are in each
landmass
"""
landmass_count = df['landmass'].value_counts().sort_index()
landmasses = ['N.America', 'S.America', 'Europe', 'Africa', 'Asia', 'Oceania']

"""
Explicit Loop printing out each value
Zip value used to print out continent and its corresponding count of countries
Learned zip keyword from ChatGPT
"""
for landmass, count in zip(landmasses, landmass_count):
    print(landmass + ": " + str(count))

print()

"""
Printing out the same output but in an implicit loop with the same zip command
used to be able to print two values of two different lists at the same time
"""
[print(landmass + ": " + str(count)) for landmass, count in zip(landmasses, landmass_count)]
print()

"""
Grouping the language and population columns and cumulating the sum in order to
print out each population based on the language
"""
total_population = df.groupby('language')['population'].sum().reset_index()
#Learned how to sort from ChatGPT
total_population = total_population.sort_values(by = 'population', ascending = False)
print(total_population)
print()

"""
Created a dataframe which just has populouses below 50 and then grouped language and population
columns to change the total population data frame to consist of the new populations

We can come to the conclusions that when it comes to a limited size population, "other"
languages take over and when it comes to no limit, Chinese population reigns superior
"""
below_50_population = df[df['population'] < 50]
total_population = below_50_population.groupby('language')['population'].sum().reset_index()
total_population = total_population.sort_values(by = 'population', ascending = False)
print(total_population)
print()


employee_data = {
    'name': ['Max', 'Jill', 'Fong', 'Juanita', 'Nya'],
    'language': [1, 2, 5, 5, 8]
}
"""
Merging the employee information and flag data information with the merge function.
The total countries was calculated by grouping the languages spoken by the employees
by the amount of countries that deem that language the national language and adding
all thhose countries up.
"""
firm_df = pd.DataFrame(employee_data)
merged_df = pd.merge(firm_df, df, on = 'language')
total_countries = merged_df.groupby('language')['name_y'].count().sum()

print("Representative-countries:" + str(total_countries))

"""
NaN means that such possibility of landmass and language does not exist, for example
there are no American countries that speak Arabic or Chinese.
"""
area_df = df.groupby(['landmass', 'language'])['area'].sum().reset_index()
pivot_table = area_df.pivot(index = 'landmass', columns = 'language', values = 'area')
print(area_df)
print(pivot_table)