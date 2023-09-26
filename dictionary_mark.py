no_of_subject=int(input("Enter no of subject:"))
mark_dictionary={}
  
for i in range(no_of_subject):
    sub_name=input("Enter your subject name:")
    sub_mark=input("Enter your subject mark:")
    mark_dictionary.update({sub_name:sub_mark}) 
print(mark_dictionary)
      