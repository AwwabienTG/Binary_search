import array
import numpy as np

user_array = array.array('i', [])

array_size = int(input("How many mubers do you want to sort: "))
for i in range(0, array_size):
    num = int(input("Enter array element %d: " % (i + 1)))
    user_array.append(num)

search_num = int(input("\nWhat number do you want to find: "))
np.sort(user_array)

def search (ar, l, r, x):

        if r >= l:
            mid = l + (r - l) // 2
            if ar[mid] == x:
                return mid
            elif ar[mid] > x:
                return search(ar, l, mid-1, x)
            else:
                return search(ar, mid + 1, r, x)
        else:
            return -1


result = search(user_array, 0, len(user_array)-1, search_num)
if result != -1:
    print("All array elements are: ", end="")
    for i in np.sort(user_array):
        print(i, end=" ")
    print ("\nElement is present at index % d" % (result+1))
else:
    print ("Element is not present in array")
