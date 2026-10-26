employee=(
    ("krishna","developer",50000),
    ("rahul","data analyst",45000),
    ("priya","developer",55000)
     )

print("==============EMPLOYEE SALARY==========")

print()

for employees in employee:
 name=employees[0]
 role=employees[1]
 salary=employees[2]

 add_salary=salary+(salary*10/100)
 
# max_salary=max(add_salary)

 if salary>=50000:
  print("YES UR SLAARY IS ABOVE 50000")
 else:
  print("NOT YOUR SALARY  IS NOT SCORE ABOVE 50000")  

 print(name)
 print(role)
 print(salary)
 print(add_salary)
#  print(max_salary)
 print()

