class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum=0
        pro = 1
        while n!=0:
            sum+= int(n%10)
            pro*= int(n%10)
            n = int(n/10)
        return pro - sum