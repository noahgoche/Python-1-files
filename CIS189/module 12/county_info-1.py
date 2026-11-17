"""
* Name         : M12 T1: CSV Import to Class Object Assignment
* Author       : Noah Goche
* Created      : 7/25/2026
* Course       : CIS189 30546
* IDE          : Visual Studio Code Version 1.129.1
* Description  : Program creates reads a csv to create county objects that contains their rank, name, per capita income,
median household income, population, and number of households and return county information
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""
"""
CIS189 Module 12 CSV Import to Class Object Assignment script.

Remove all instances of pass before running/submitting your code.
Submitted files with pass included will receive 0 points.
"""
import csv

class County:

    def __init__(self, rank, county, per_capita_income, median_household_income, population, number_of_households):
        self.rank = rank
        self.county = county
        self.per_capita_income = per_capita_income
        self.median_household_income = median_household_income
        self.population = population
        self.number_of_households = number_of_households


    def get_population(self):
        """
        Return the population as a float.
        """
        return float(self.population.replace(",", ""))

    def __repr__(self):
        return (f"County({self.rank=}, {self.county=}, {self.per_capita_income=}, {self.median_household_income=}, {self.population=}, {self.number_of_households=})")
             


def main():
    # Use the DictReader object to read in the CSV file. Each row will be represented
    # as a dictionary, with the column name as the key and the associated value 
    # the value. 
    # Create a County object for each county. 
    # Finally, print the total population for all counties in Iowa by by calling
    # get_population for each, and maintaining a running total. 
    
    population_total = 0
    county_List = {}
    with open("Iowa 2010 Census Data Population Income-1.csv", newline='') as fcsv:
        read = csv.DictReader(fcsv)
        for county in read:
            if county["Rank"] == '':
                pass
            else:
                new_County = County(county["Rank"], county["County"], county["Per capita income"], county["Median household income"],
                                                    county["Population"], county["Number of households"])
                county_List[county["County"]] = new_County
                population_total = population_total + new_County.get_population()
                print(new_County)

    print(f"The total population is {population_total}")



if __name__ == "__main__":

    main()
