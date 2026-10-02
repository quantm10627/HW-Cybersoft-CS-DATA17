data = [
    [1,5,"MQ",2,9],
    [4,2,"HG",7,5]
]
def bubble_sort(arr, column):
    for i in range (len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j][column] > arr[j+1][column]:
                arr[j][column] , arr[j+1][column]  = arr[j+1][column] , arr[j][column] 
bubble_sort(data,1)
print(data)