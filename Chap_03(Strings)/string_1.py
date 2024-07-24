a = 'Python'   # single quote 
b = " Python"     # double quote
c = '''Python '''      # triple quote

#String Slicing 

print(c[1:4])


#Negative Slicing

print ( a [-5: -1])
print(a [1: 5 ])

#String Function 

d = "Coding in Python Today "
print("String is : ", d)
print("Length: ", len(d))
print ("Is ends with Today? ", d.endswith("Today"))
print ("Is starts with Today? ", d.startswith("Today"))
print ("Count letter i : " , d.count("i"))
capitalized_string = d.capitalize()
print(capitalized_string) 

replace = d.replace("y", "l")
print(replace) 


# Escape Sequence Characters 

d = "Coding in Python Today \n Its Fun to learn Python \t I'm enjoying alot "
print(d)