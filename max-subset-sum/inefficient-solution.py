#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumSum function below.
def maximumSum(a, m):
    s1=list()
    s=set(a)
    maxsum=0
    for i in s:
        #if i%m > maxsum:
        s1.append(i%m)
        maxsum=i%m

        #if i%m == m-1:
        #    return m-1
        
    #print(maxsum)
    i=0;j=1;k=1
    while(i<n-1 and j<n):
        while((j+k)<n+1):
            #if sum(a[i:j+k])%m > maxsum:
            s1.append(sum(a[i:j+k])%m)
            maxsum=sum(a[i:j+k])%m
                #print(maxsum)
            #if(maxsum == m-1):
            #    break 

        #if(maxsum == m-1):
         #   break 

            k+=1  
        k=1;i+=1;j+=1
        
    print(s1)

    '''
    maxsum=0
    #print(len(s1[6]))y
    for ele in s1:
        if type(ele) is list:
            if sum(ele)%m > maxsum:
                maxsum=sum(ele)%m
        else:
            if ele%m > maxsum:
                maxsum=ele%m
    #print(sum1)
    return maxsum
    '''

            
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0]) #no of elements in array

        m = int(nm[1]) # modulo number

        a = list(map(int, input().rstrip().split())) # array

        result = maximumSum(a, m)

        fptr.write(str(result) + '\n')

    fptr.close()

