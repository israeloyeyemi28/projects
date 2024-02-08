# for creativity i added my name at the buttom
with open("life-expectancy.csv") as data_file :
    life_expectancies = []
    countries = []
    years = []
    
    # Skip the header row
    header = next(data_file)
    
    for data in data_file:
        row = data.split(",")
        entity = row[0].strip()
        code = row[1].strip()
        year = int(row[2])
        life_expectancy = float(row[3])
        
        life_expectancies.append(life_expectancy)
        countries.append(entity)
        years.append(year)
        
    max_life = -float('inf')
    min_life = float('inf')
    average_life = sum(life_expectancies)/ len(life_expectancies)
    
    max_country = ""
    max_year = -float('inf')
    min_country = ""
    min_year = float('inf')
    
    chosen_year = None 
    checked_year = float(input("Enter your year of interest: "))
    
    for i in range(len(years)):
        if years[i] == checked_year:
            chosen_year == checked_year
        
        if life_expectancies[i] > max_life:
            max_life = life_expectancies[i]
            max_country = countries[i]
            max_year == years[i]
        
        if life_expectancies[i] < min_life:
            min_life = life_expectancies[i]
            min_country = countries[i]
            min_year = years[i]
            
    print()
    print(f"For the year {checked_year}:")
    print(f"The average life expectancy throughout the countries was {average_life:.2f}")
    print(f"The maximum life expectancy was in \n: {max_country} with \n{max_life:.2f}")
    print(f"The minimum life expectancy was in: {min_country} with {min_life:.2f}")
    print(f"The overall minimum life expectancy is: {min_life:.2f} from {min_country} in {min_year}")
    print("this program was created vy isreal")
    print(f"{min_year}")
    print("thanks for using my program")