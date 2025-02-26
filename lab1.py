
nume = input("Cum te numești?: ")
print(f"Hello, {nume}!")




a = 21  
b = 5.7  
c = "Emiliana" 
d = """Eu m-am săturat să lucrez
vreau să stau acasă să dorm
și să mă joc cu Tommy""" 




print(type(a))   
print(type(c))  


print(len(c)) 


print(c.upper())  



subsir = c[2:5]  
print(subsir)



# Metoda .format()
mesaj1 = "Eu am {} ani și mă numesc'{}'.".format(a, c)
print(mesaj1)

# Metoda f-string
mesaj2 = f"Numărul real este {b}, iar ceea ce vreau este:\n{d}"
print(mesaj2)




txt = "More results from text..."
substr = txt[4:12]
print(substr)
print(substr.strip()) 



txt = "More results from text..."
print(txt.split())



age = 36
txt = "My name is Mary, and I am {}"
print(txt.format(age))
