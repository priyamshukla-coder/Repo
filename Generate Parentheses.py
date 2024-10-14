class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def f(l1=[],l=0,r=0):
            if len(l1)==2*n:
                res.append("".join(l1))
                return
            if l<n:
                l1.append("(")
                f(l1,l+1,r)
                l1.pop()
            if r<l:
                l1.append(")")
                f(l1,l,r+1)
                l1.pop()
        res=[]
        f()
        return res