# What does this piece of code do?
# Answer: This code calculates and prints the sum of 11 random integers between 1 and 10 (inclusive).

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5 (NOTE: ceil is imported but not used in this code)
from math import ceil

# Initialize total_rand to 0 (will store the sum of random numbers)
total_rand = 0
# Initialize progress to 0 (loop counter)
progress=0

# While loop: runs as long as progress is ≤ 10 (total 11 iterations)
while progress<=10:
    # Increment loop counter by 1 (first iteration: progress becomes 1, last: 11)
    progress+=1
    # Generate a random integer between 1 and 10 (inclusive)
    n = randint(1,10)
    # Add the random number to the total sum
    total_rand+=n

# Print the final sum of the 11 random numbers
print(total_rand)
