students={
   "11":{ "HIMANSHI":[81,90,98,74,79]},
   "9":{"KHUSHI":[70,70,70,70,68,95]}
}

name=input("Enter name: ")
cls=input("Enter class:")
name=name.upper()

if cls not in students:
	print("invalid syntex")
	exit()

if name not in students[cls]:
	print("invalid syntex")
	exit()

def get_grades(ptg):
   if ptg>=90:
   	return "A"
   elif ptg>=75:
   	return "B"
   else:
   	return "C"
   
marks=students[cls][name]
total=sum(marks)
ptg=total/len(marks)
grades=get_grades(ptg)

print("NAME:", name)
print("CLASS:", cls)
print("GRADE:", grades)
print("percentage:", ptg)

             