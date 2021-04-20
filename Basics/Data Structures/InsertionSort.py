#INSERTION SORT
def insertion_sort(array):

    # We start from 1 since the first element is trivially sorted
    for index in range(1, len(array)):
        currentValue = array[index]
        currentPosition = index

        
        while currentPosition > 0 and array[currentPosition - 1] > currentValue:
            array[currentPosition] = array[currentPosition -1]
            currentPosition = currentPosition - 1
        array[currentPosition] = currentValue
        print("array now : ")
        print(array)
if __name__ == '__main__': 
  array = []
  n = int(input("Enter number of elements : ")) 
  for i in range(0, n): 
      ele = int(input()) 
      array.append(ele) # adding the element 
  print("sorted array: " + str(insertion_sort(array)))
