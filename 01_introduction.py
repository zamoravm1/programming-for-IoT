# Functions

def sum(a,b):
    return a+b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b 
    
def sub(a,b):
    return a-b

if __name__=="__main__":
    '''
    # File managment
    # open, read, write and close (to save chenges)
    f = open('example.txt','w')
    #fileContent=f.read()
    f.write('NEW LINE WORKING')
    f = open('example.txt')
    fileContent=f.read()
    print(fileContent)
    f.close()

    # Create a file
    f = open('original.txt','x')
    f = open('original.txt','w')
    f.write("My original line")
    f.close()
    g = open('original.txt')
    var = g.read()
    f = open('copy.txt','x')
    f = open('copy.txt','w')
    f.write(var)
    f.close()  # add this line to ensure the changes are saved to the file
    f = open('copy.txt')
    var2 = f.read()
    print(f"Original file: {var}\nCopy file: {var2}")

    # if-else 
    a = int(input("Set first number: \n"))
    if a%2 == 0 and a%3 == 0:
        print(f"The number {a} is a multiple of the numbers 2 and 3")
    elif a%2 == 0:
        print(f"The number {a} is a multiple of 2 but not of 3")
    elif a%3 == 0:
        print(f"The number {a} is a multiple of 3 but not of 2")
    else:
        print(f"The number {a} is not a multiple of 2 or 3")
    
    # list + loops
    
    list = [0,1,2,3,4,5]
    # v1
    sum=0
    for i in list:
        sum+=i
    print (f"The sum of the list is: {sum}")

    list = [0,1,2,3,4,5]
    #v2
    sum=0
    for i in range(len(list)):
        sum+=list[i]
    print (f"The sum of the list is: {sum}")

    list = [0,1,2,3,4,5]
    #v3
    sum=0
    i=0
    while i<len(list):
        sum+=list[i]
        i+=1
    
    print (f"The sum of the list is: {sum}")

    list = [0,1,2,3,4,5]
    min= 10000
    max= 0
    sum= 0
    for i in list:
        if i>max:
            max=i
        elif i<min:
            min=i

        sum+=i
    
    avg=sum/len(list)

    print(f"The max number: {max} \n The min number: {min} \n The average: {avg}")

    #Dictionaries

    dicc_list= input("Insert Project Name, company, device ID, device name, device type, separated by comma: ")
    dicc_list= dicc_list.split(",")

    dicc={
    "projectName":dicc_list[0],
        "company":dicc_list[1],
        "deviceList": [
            {
                "deviceID": dicc_list[2],
                "deviceName" : dicc_list[3],
                "deviceType" : dicc_list[4]
            }
        ]
    }

    print(dicc)
    
    # JSON
    import json

    js= json.dump(dicc,open("first_json.json","w"))
    '''
    # Functions

    a=int(input("Set first number:"))
    b=int(input("Set second number:"))

    suma=sum(a,b)
    resta=sub(a,b)
    division=div(a,b)
    multiplicacion=mul(a,b)

    print(f"Los resultados para {a} y {b} fueron:\n")
    print(f"Sum={suma}\n Substract={resta} \n Multiplly: {multiplicacion} \n Divide: {division}")


    

    

    




    

    
    


    