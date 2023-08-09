from storage_sys_es import Variable
from util_es import type_check # utils_es contains lexer_es
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

    def expr():
        nonlocal current_token

        if current_token.type == TokenType.VARIABLE:
            current_token.type = type_check(var_class.var[current_token.value])
            current_token.value = var_class.var[current_token.value]

        result = current_token.value
        result_type = current_token.type
        if result_type == TokenType.STRING:
            if result.startswith('"') and result.endswith('"') or result.startswith("'") and result.endswith("'"):
                result=result[1:-1]

        eat(current_token.type)

        while current_token.type in (TokenType.PLUS, TokenType.MINUS,TokenType.MULTIPLICATION, TokenType.DIVIDE):
            op = current_token.type
            eat(current_token.type)
            if current_token.type == TokenType.VARIABLE:
                current_token.type = type_check(var_class.var[current_token.value])
                current_token.value = var_class.var[current_token.value]
            if result_type == TokenType.STRING:
                if current_token.value.startswith('"') and current_token.value.endswith('"') or current_token.value.startswith("'") and current_token.value.endswith("'"):
                    current_token.value=current_token.value[1:-1]
            if op == TokenType.PLUS:
                result += current_token.value
            elif op == TokenType.MINUS:
                result -= current_token.value
            elif op == TokenType.MULTIPLICATION:
                result *= current_token.value
            elif op == TokenType.DIVIDE:
                result /= current_token.value
            eat(current_token.type)

        return result
    
    def statement():
        if current_token.type == TokenType.PRINT:
            eat(TokenType.PRINT)
            value = expr()
            print(value)  # Print the result of the expression
        elif current_token.type == TokenType.DEFINE:
            eat(TokenType.DEFINE)
            name=current_token.value
            try: # idunno whats happening here
                eat(TokenType.UNEXPECTED_KEYWORD)
            except:
                eat(TokenType.VARIABLE)
            eat(TokenType.EQUALS)
            var_class.add_variable(name,current_token.value)
        else:
            return expr()

    while current_token.type != TokenType.EOF:
        statement()