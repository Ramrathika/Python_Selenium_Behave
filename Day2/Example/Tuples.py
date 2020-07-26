country = ('US', 'UK', 'Spain', 'NZ', 'Ind', 'Germany', 'Aus', 'Ind', 'Spain')
print(country)
print(type(country))

print(country.index('Ind'),"Index of Ind")

print(country.count("Ind"))
print(len(country))

for c in country:
    print(c)