# Example to show sorting of structured array 

# set alias names for dtypes 

dtypes = [('name', 'S10'), ('grad_year', int), ('cgpa', float)] 



# Values to be put in array 
import numpy as np
values = [('Ram', 2025, 8.5), ('Shyam', 2024, 8.7), 

		('Ramu', 2023, 7.9), ('Shyamu', 2022, 9.0)] 

			

# Creating array 

arr = np.array(values, dtype = dtypes) 

print ("\nArray sorted by names:\n", 

			np.sort(arr, order = 'name')) 

			

print ("Array sorted by grauation year and then cgpa:\n", 

				np.sort(arr, order = ['grad_year', 'cgpa']))