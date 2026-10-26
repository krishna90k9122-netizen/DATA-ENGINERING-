marks=[10,20,30,40,87,50,60,70,80]


total=sum(marks)
student=len(marks)
average=total/student
highest=max(marks)
lowest=min(marks)


if total >=850:
     print("you are passed")
else:
    print("You are failed")


sorted_marks=sorted(marks)

print(marks)
print(student)
print(average)
print(highest)
print(lowest)
  