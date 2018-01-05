"""this project about find a certain string or sub string in a string"""
import _string
z=[]
def func(x,y,i):
    print(z)
    w=y.find(x)
    print(w)
    if w == -1:
       return z
    else:
        z.append(w+i)
        """print(z)"""
        index=len(z)

        i=z[index-1]+len(x)
        func(x,y[i:],i)
while(1):
    try:
        y=input("enter the full string:  ")
        x=input("enter the sub string:  ")
        if x == "" or y == "":
            print("Enter a valid string please!")
            quit()
        x=x.strip()
        y=y.strip()
        w=func(x,y,0)
        if w == -1 or w== []:
            print("the sub strint not found")
        else:
            print("the substring founded its at the positions: "+str(z))
        z=[]
    except Exception as e:
        print("Error ! "+str(e))