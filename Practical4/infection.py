''' pseudocode
1. Define initial variables: initial infected student, increasing rate, total students, initial day
2. Print the initial infection status
3. Use a while loop: continue calculating daily infections while infected < total students 
4. Inside the loop: increment day counter
5. update infected count (previous * (1 + increasing rate))
6. print the daily infected count
7. After loop ends: print the total number of days required'''

a=5 #a is initial infected student
b=0.4 #b is increasing rate 
n=91 #n is the total students number
c=1 #c is initial day

while a<n: 
    print(c) #what is the day today
    print(a) #what is the  today
    c+=1 # Days increase
    a=a+b*a # infected students increase
print("The number of infected students in day 10 is more than 91. So it will take 9 days to infect all the students.")
#The numberof infected students in day 10 is more than 91. So it will take 9 days to infect all the students.(Count the number of days needed starting from the first day)    