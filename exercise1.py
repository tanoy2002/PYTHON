#making a simple dictionary
d={"abundant":"existing or available in large quantities",  'redirection':"the action of assigning or directing something to a new or different place or purpose","apathy":"lack of interest, enthusiasm, or concern","agony":"extreme physical or mental suffering","veracious":"speaking or representing the truth"}
print("Enter your word: ")
a=input()#taking input from the user
print("Meaning: ",d[a])#finding the corresponding value of 'a' in dictionary 'd' and printing it
#second way of creating a dictionary
Dictionary = {'set':'Its a collection of well defined object','Mutable':'Changeable','Immutable':'Not changeable'}
search = input('Enter your word :')
print(Dictionary[search])
