from cleaning import name,salary
from validation import validation

name="Krishna"
salary="500000"

name=name(name)
salary=salary(salary)

if validation(salary):
    print(name)
    print(salary)
    