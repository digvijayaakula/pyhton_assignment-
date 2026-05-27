def api_request(endpoint,*args,**kwargs):
    print("endpoint :",endpoint)

    print("args")
    for i in args:
        print(i)

    print("kwargs")
    for k,v in kwargs.items():
        print(k,v)

endpoint=input("enter endpoint : ")
n=int(input("how many params : "))

args=[]
for i in range(n):
    args.append(input("enter param : "))

m=int(input("how many key values : "))
kwargs={}

for i in range(m):
    key=input("enter key : ")
    value=input("enter value : ")
    kwargs[key]=value

api_request(endpoint,*args,**kwargs)