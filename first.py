print("Hello")

my_list=[1,2,3,4,'sai',23,43]

print(type(my_list))

my_string="my name is althaf"

print(type(my_string))

print(my_string)

my_tuple =tuple(my_list)
print(my_tuple)

my_list.append("basha")

print(my_list)

my_list[7]="ali basha"
print(my_list)

# class 2

my_varb=[1,2,3,4,5,6]
my_varb.pop()
print(my_varb)

# convert a list to tuple

my_tuple=tuple(my_varb)
print(type(my_tuple))

my_set={"a","b","c","d","a","b",True}
print(my_set) 
my_set.add("e")
print(my_set)
my_string1=["hello"]
my_string2=["althaf is bad boy's"]
print(my_string2[0:2])


my_dict={
    "01":"jagadesh",
    "02":"ajay",
    "03":"sandy"
}

print(my_dict.get("01"))
my_dict.update({"03":"basha"})
print(my_dict.get("03"))


my_num=100
if my_num%3==0:
    print("even number")
else:
    print("odd number")    
