class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry=0
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        c=0
        r=[]
        
        for i in range(max_len-1,-1,-1):
            s1=c+int(a[i])+int(b[i])
            r.append(str(s1%2))
            c=s1//2

        if c:
            r.append('1')


        return "".join(r[::-1])



        
