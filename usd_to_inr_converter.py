name = input("PLEASE ENTER YOUR NAME HERE: ")
    
print("WELCOME DEAR",name,"!")



usd=int(input("PLEASE ENTER AMOUNT OF USD YOU WANT TO CONVERT:"))
    



print("PLEASE KEEP IN MIND MY CURRENT USD TO INR RATE",end= " ")
print("IS SET BY MY PROGRAMMER MR SHORYA TO 94.61")
    
def usd_2_inr_converter(a):
    inr_rate=94.61
    inr= inr_rate*a
    return inr
    

    
print("DEAR",name,"THE CURRENT RATE FOR" ,usd, end= " ")
print("USD IS:",usd_2_inr_converter(usd))
    
    