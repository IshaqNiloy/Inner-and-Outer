import numpy

class Numpy():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    #Finds the inner product
    def find_inner(self):
        print(int(numpy.inner(a, b)))#Converted to int to print only the integer value
    
    #Finds the outer product
    def find_outer(self):
        print(numpy.outer(a, b))

if __name__ == '__main__':
    a = numpy.array([input().split()], int)
    b = numpy.array([input().split()], int)
    my_object = Numpy(a, b)
    my_object.find_inner()
    my_object.find_outer()