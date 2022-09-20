from numpy import append


l=[2,35,6,86,32,3354,23]
n=len(l)
def search_min(l,n):
    min=l[0]
    id=0
    element=1
    while element<n:
        if n<1:
            return min,id
        
        v = l[element]
        if v<min:
            min=v
            id=element
        element=element+1
    return min,id
#---------------------------------------------------------------------------------------------------------------    
#a,b=search_min(l,n)              
#print("min is :", a,"and id is :" ,b)
#===============================================================================================================
def sort(l,n):
    l2=[]
    i=1
    while i<=n:
        a,id =search_min(l,n)
        l2.append(a)
        del(l[id])
        n=n-1
    return l2
#=================================================================================================================
l3=[68,7,-2124,-3,4445,667,33,6,4,0,323,6]   
m=len(l3) 
d=sort(l3,m)    
print(d)        


