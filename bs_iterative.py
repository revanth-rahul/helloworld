def binarysearch(A,k):
    l=0
    h=len(A)-1
    while(l<=h):
        mid=(l+h)//2
        if(k==A[mid]):
            return True
        elif(k<A[mid]):
            h=mid-1
        else:
            l=mid+1
    return False
A=[11,22,33,44,55,66,77,88,99,100]
B=[]
print("before append:",A)
A.append(123)
print('after append:',A)
A.insert(3,42)
print("after insert",A)
B.extend(A)
print("before list in B:",B)
B.remove(42)
print("after list in B:",B)
found=binarysearch(A,99)
print("the element :",found)
