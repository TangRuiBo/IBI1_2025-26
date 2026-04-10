import matplotlib.pyplot as plt 

#plt.ion() # I find that if I don't write down this, the code after the chart can't run unless I turn off the chart.
Gene_expression = {"TP53":12.4,"EGFR":15.1,"BRCA1":8.2,"PTEN":5.3,"ESR1":10.7}
print(Gene_expression)
Gene_expression["MYC"]=11.6
Gene_name=["MYC","TP53","EGFR","BRCA1","PTEN","ESR1"]
Gene_level=[11.6,12.4,15.1,8.2,5.3,10.7]
plt.bar(Gene_name,Gene_level)
plt.title("Gene expression")
plt.ylabel("Expression level")
plt.show()

a= "MYC"  #a can be any other gene you are interested in
if a in Gene_expression:
    print("exist")
    print("The expression is",Gene_expression[a])
else:
    print("Not exist(error)")

b=sum(Gene_expression.values()) #b is the total number of all level 
c=b/6 # c is the average number of all level
print("The average level is %.2f"%c)