'''
Created on 04-Aug-2020

@author: Lenovo
'''

print("hello");
print("hello world");

a=50;
b=500;
print(a);
print(id(a));
print(id(b));

#we can add same value to b then id will be same as a. object id

name="vagish";
_age=29;

print(name,_age);

# we can give same value to all variables like below or diff valyes ata time

a=b=c=50;
print(a,b,c);


#e=f=g=20,30,40;
#print e;
#print f;
#print g;

# automaticlly binds the object type with variable ..no need to mention datatype ..
#u can check with type() function
#Datatypes:-Numeric ,sequence(string,list,tuple), set, dictionary(key value pair), boolean
names="""complete nsma list"""
print(type(29));
print(type(names))
print (names[0:2]) #printing first two character using slice operator    
print (names[4]) #printing 4th character of the string    
print (names*2) #printing the string twice    
print (names + name) #printing the concatenation of str1 and str2  


#lists
list1  = [1, "hi", "Python", 2]    
#Checking type of given list  
print(type(list1))  
#Printing the list1  
print (list1)  
  
# List slicing  
print (list1[3:])  
  
# List slicing  
print (list1[0:2])   
  
# List Concatenation using + operator  
print (list1 + list1)  
  
# List repetation using * operator  
print (list1 * 3)  


#Set is the unordered collection of the data type. It is iterable, mutable(can modify after creation)

# Creating Empty set  
set1 = set()  
  
set2 = {'James', 2, 3,'Python'}  
  
#Printing Set value  
print(set2)  
  
# Adding element to the set  
  
set2.add(10)  
print(set2)  
  
#Removing element from the set  
set2.remove(2)  
print(set2) 

#dictionary

d = {1:'Jimmy', 2:'Alex', 3:'john', 4:'mike'}     
  
# Printing dictionary  
print (d)  
  
# Accesing value using keys  
print("1st name is "+d[1])   
print("2nd name is "+ d[4])    
  
print (d.keys())    
print (d.values())    

#boolean
