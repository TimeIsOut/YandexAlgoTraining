int1 = int(input())
int2 = int(input())
col1 = int(input())
col2 = int(input())
min1 = col1 + int1 * (col1 - 1 ) 
max1 = col1 + int1 * (col1 + 1 ) 
min2 = col2 + int2 * (col2 - 1 ) 
max2 = col2 + int2 * (col2 + 1 ) 
if min1 > min2 :              
    totalmin = min1
else :
    totalmin = min2
if max1 > max2 :              
    totalmax = max2
else :                        
    totalmax = max1
if totalmin > totalmax :      
    print(-1)
else :
    print(totalmin , totalmax)