class Solution:
    def isValid(self, s: str) -> bool:
        
        st=[]

        for i in range(len(s)):

            if s[i]=='(' or s[i]=='{' or s[i]=='[':

                st.append(s[i])

            else:

                if len(st)==0:

                    return False

                else:

                    val=st.pop()

                    if s[i]==')' and val=='(' or s[i]=="}" and val=='{' or s[i]==']' and val=='[':

                        continue

                    else:

                        return False

        return True if len(st)==0 else False