# Creation of Empty list of AWS services 

Costoptimization_tools =[]

# Populate the list with AWS cost optiimization services 

Costoptimization_tools.append('AWS Cost Optimizer')
Costoptimization_tools.append('AWS Trusted Advisor')
Costoptimization_tools.append('AWS Quicksight')
Costoptimization_tools.append('AWS Cost Explorer')
Costoptimization_tools.append('AWS data lifecycle manager')
Costoptimization_tools.append('AWS Cost anomaly monitor')

# Print the list of services and the length 

print("List of AWS Costoptimization_tools are : \n " , Costoptimization_tools)
print (len(Costoptimization_tools))

#Remove two specific services from the list by name or by index.
del Costoptimization_tools[2]
del Costoptimization_tools[0]

#Print the new list and the new length of the list

print(Costoptimization_tools)
print(len(Costoptimization_tools))
