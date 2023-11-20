from storage_sys_es import Variable
from util_es import type_check, convert # utils_es contains lexer_es
from common import TokenType

var_class=Variable()

# Step 3: Syntactic analysis (Parsing)
def parse(tokens):
    current_pos = 0
    current_token = tokens[current_pos]

    def eat(token_type):
        nonlocal current_pos, current_token
        if current_token.type == token_type:
            current_pos += 1
            current_token = tokens[current_pos]
        else:
            raise Exception("Expected {}, but got {}".format(token_type, current_token.type))

    def expr(expression):
        return eval(expression)
    
    def get_expr():
        nonlocal current_pos, current_token
        if current_token.type == TokenType.OE:
            rez=""
            eat(current_token.type)
            while current_token.type != TokenType.CE:
                if current_token.type == TokenType.VARIABLE:
                    current_token.type = type_check(var_class.var[current_token.value])
                    current_token.value = var_class.var[current_token.value]
                rez+=str(current_token.value)
                current_pos+=1
                current_token=tokens[current_pos]
            eat(current_token.type)
            return rez
        else:
            cp=current_pos-1
            tkb=tokens[cp]
            raise Exception(f"Error 001: Expected an expression after {tkb}.")
    def get_expr_wp():
        nonlocal current_pos, current_token
        if current_token.type != TokenType.EOF:
            rez=""
            while current_token.type != TokenType.EOF:
                if current_token.type == TokenType.VARIABLE:
                    current_token.type = type_check(var_class.var[current_token.value])
                    current_token.value = var_class.var[current_token.value]
                rez+=str(current_token.value)
                current_pos+=1
                current_token=tokens[current_pos]
            try:
                rez=convert(rez)
            except:
                pass
            return rez
        else:
            cp=current_pos-1
            tkb=tokens[cp]
            raise Exception(f"Error 001-2: Expected an expression after {tkb} but got EOL.")
    
    def statement():
        if current_token.type == TokenType.PRINT:
            eat(TokenType.PRINT)
            value = expr(get_expr_wp())
            print(value)  # Print the result of the expression
        elif current_token.type == TokenType.GOTO:
            eat(TokenType.GOTO)
            return "goto "+str(current_token.value)
        elif current_token.type == TokenType.IF:
            eat(TokenType.IF)
            val=expr(get_expr())
            if val==False:
                return 'ifnotentered'
        elif current_token.type == TokenType.DEFINE:
            eat(TokenType.DEFINE)
            name=current_token.value
            try: # idunno whats happening here
                eat(TokenType.UNEXPECTED_KEYWORD)
            except:
                eat(TokenType.VARIABLE)
            eat(TokenType.DOUBLE_EQUALS) # apparently the lexer treats = as ==
            var_class.add_variable(name,expr(get_expr_wp()))
        elif current_token.type == TokenType.VARIABLE:
            name=current_token.value
            eat(TokenType.VARIABLE)
            eat(TokenType.DOUBLE_EQUALS)
            var_class.add_variable(name,expr(get_expr_wp()))
        else:
            return expr(get_expr_wp())

    while current_token.type != TokenType.EOF:
        result = statement()  # Store the result of statement() function
        if result:
            result=str(result)
            if result.startswith("goto"):
                return result  # Return the result if it's "goto"
            elif result == 'ifnotentered':
                return result  # Return the result if it's "if (notentered)"