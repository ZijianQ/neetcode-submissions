class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []


        def valid(s):
            open =0
            for c in s:
                if c=="(" :
                    open+=1 
                else: open-=1

                if open <0 or open> n:
                    return False

            return not open

                


        def dfs(s):

            if len(s)== n*2:
                if valid(s):
                    res.append(s)

                return

            dfs(s +"(")
            dfs(s +")")

        dfs("")
        return res



        