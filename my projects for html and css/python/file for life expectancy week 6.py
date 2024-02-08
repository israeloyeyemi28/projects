with open ("life_expectancy.csv") as file_set :
    
    for row in file_set :
        row = row.split(",")
        entity = row[0].strip()
        code = row[1].strip()
        year = int(row[2])
        life_expectancy = float(row[3])
        
        max_life = -1
        min_life = min(life_expectancy)
        avg_life = sum(life_expectancy) /     len(life_expectancy)
        
        max_country = " "
        max_year = max(year)
        min_country = min(entity)
        min_year = min(year)
        
        chosen_year =" "
        
print( )
check_year = input(float("Enter your year of interest :"))   
if chosen_year == check_year :
    chosen_year = check_year
    
print(f"for the year : {check_year}:\n")  
print(f"The average life expectancy throughout the countries was str{avg_life :.2f}\n")       
print(f"The max life_expectancy was in :{max_country} with {max_life:.2f}\n")
print(f"The min life expectancy was in {min_country} with {min_life:.2f}\n")

if life_expectancy > max_life :
         max_life = life_expectancy
         max_country = country
print( )
print(f"The overall max life expectancy is :{max_life:.2f} from {max_country} in {max_year:.2f}\n")
print(f"The overall min life expectancy is : {min_life:.2f} from {min_country} i  {min_year:.2f}.\n")     