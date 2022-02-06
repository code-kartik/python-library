# numpy library

import numpy

# list & array are different

egList = [4, 5, 8, 9, 6, 3]


egArray = numpy.array([4, 5, 8, 9, 6, 3])

print(egList*2, egArray*2)  # comparing lists with arrays

print()
print("One Dimension Array:")
oneDArray = numpy.array([7, 9, 6, 5, 10])  # one dimensional array
print(oneDArray)
print("Dimension ", oneDArray.ndim)  # dimension of the array
print("Shape ", oneDArray.shape)  # tells rows & columns
print("Size ", oneDArray.size)  # tells total number of elements
print(oneDArray[2])

print()

print("Two Dimension Array:")
twoDArray = numpy.array([[7, 9, 6, 5, 10], [4, 5, 1, 9, 6]])
print(twoDArray)
print("Dimension ", twoDArray.ndim)  # dimension of the array
print("Shape ", twoDArray.shape)  # tells rows & columns -> (row,column)
print("Size ", twoDArray.size)  # tells total number of elements
print(twoDArray[1, 3])  # element at index row=1 & column=3

print()

print("Operations on Arrays:")
print("Sum of all elements ", numpy.sum(twoDArray))  # sum of all the elements in array
print("Product of all elements ", numpy.prod(twoDArray))  # sum of all the elements in array
print("Maximum from the array ", numpy.max(twoDArray))  # returns the maximum integer from the array
print("Maximum from the array ", numpy.min(twoDArray))  # returns the minimum integer from the array
print("Mean of all elements ", numpy.mean(twoDArray))  # returns the mean of all elements from the array
print("Standard Deviation of all elements ", numpy.std(twoDArray))  # returns the standard deviation
print("Index of maximum integer ", numpy.argmax(twoDArray))  # returns index of maximum integer
print("Index of minimum integer ", numpy.argmin(twoDArray))  # returns index of minimum integer

print()

print("Three Dimensional Array:")
threeDArray = numpy.array