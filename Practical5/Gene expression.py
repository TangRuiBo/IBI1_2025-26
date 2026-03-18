import matplotlib.pyplot as plt 

plt.ion() # I find that if I don't write down this, the code after the chart can't run unless I turn off the chart.
Gene_expression = {"TP53":12.4,"EGFR":15.1,"BRCA1":8.2,"PTEN":5.3,"ESR1":10.7}
Gene_expression["MYC"]=11.6
Gene_name=["MYC","TP53","EGFR","BRCA1","PTEN","ESR1"]
Gene_level=[11.6,12.4,15.1,8.2,5.3,10.7]
plt.bar(Gene_name,Gene_level)
plt.title("Gene expression")
plt.ylabel("Expression level")
plt.show()

a=str(input('What kind of gene do you want to search?(You should take care of yhe capital and small letter)\n'))  #a is what the name the users input
if a in Gene_expression:
    print("exist")
    print("The expression is",Gene_expression[a])
else:
    print("Not exist(error)")

b=sum(Gene_expression.values()) #b is the total number of all level 
c=b/5 # c is the average number of all level
print("The average level is",c)