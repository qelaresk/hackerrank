class Calculator():
    def power(self,n,p):
        assert n >=0 and p >=0, 'n and p should be non-negative'
        return pow(n,p)


myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   