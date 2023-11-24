class Difference:  
    # maximumDifference = 0
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0


    def computeDifference(self):
        df = 0
        for i in self.__elements:
            for j in self.__elements:
                if df < abs(i-j):
                    df = abs(i-j)
        # Difference.maximumDifference = df
        self.maximumDifference = df


# End of Difference class

# _ = input()
a = [int(e) for e in input().split(' ')]
b = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()


# print(d.maximumDifference)

c = Difference(b)
c.computeDifference()

# d.maximumDifference = 7
# Difference.maximumDifference = 8



print(d.maximumDifference)
print(c.maximumDifference)
# print(Difference.maximumDifference)