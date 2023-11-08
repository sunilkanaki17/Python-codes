class Solution:
    def interpret(self, command: str) -> str:
        result=""
        op={"G":'G',"()":'o',"(al)":'al'}
        for i in range(len(command)):
            if command[i]=="G":
                result+="G"
            elif command[i]=="(":
                if command[i+1]==")":
                    result+="o"
                    i+=2
                elif command[i+1]=='a':
                    if command[i+3]==')':
                        result+="al"
        return result
                        

        