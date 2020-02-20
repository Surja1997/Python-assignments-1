class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    def computeDifference(self):

        self.__elements.sort()
        sortedElements=self.__elements
        print(sortedElements)
        self.maximumDifference=abs(sortedElements[len(sortedElements)-1]-sortedElements[0])
# End of Difference class

a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)