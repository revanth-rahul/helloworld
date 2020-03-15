def binarysearch(l,h,key):
    if(l==h):
        if(A[l]==key):
            return l
        else:
            return 0
    else:
        mid=(l+h)//2
        if(key==A[mid]):
            return mid
        elif(key<A[mid]):
            return binarysearch(l,mid-1,key)
        else:
            return binarysearch(mid+1,h,key)
A=[11,22,33,44,55,66,77,88,99,100]
found=binarysearch(0,10,100)
print("the element :",found)
