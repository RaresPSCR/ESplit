from common import TokenType
from parser_es import var_class

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

# Lexer
def lexer(input_text):
    tokens = []
    double_eq=False
    str_enable=False
    current_pos = 0
    keyword = ''

    while current_pos < len(input_text):
        char = input_text[current_pos]

        if char=='"' or char=="'":
            if str_enable:
                str_enable=False
                keyword+=char
                current_pos+=1
                tokens.append(Token(TokenType.STRING,keyword))
            else:
                str_enable=True
        
        if not str_enable:

            if char=="=":
                current_pos+=1
                if char=='=':
                    current_pos+=1
                    word="=="
                    double_eq=True
                    tokens.append(Token(TokenType.DOUBLE_EQUALS, word))
                else:
                    tokens.append(Token(TokenType.EQUALS, word))

            if char.isalpha() or char=='"' or char=="'":
                word = ''
                if current_pos < len(input_text):
                    try:
                        while input_text[current_pos].isalpha() or input_text[current_pos]=='"' or input_text[current_pos]=="'":
                            word += input_text[current_pos]
                            current_pos += 1
                    except:
                        if word == 'print':
                            tokens.append(Token(TokenType.PRINT, word))
                        elif word == 'def':
                            tokens.append(Token(TokenType.DEFINE, word))
                        elif word == 'true':
                            tokens.append(Token(TokenType.TRUE, word))
                        elif word == 'false':
                            tokens.append(Token(TokenType.FALSE, word))
                        elif word == 'if':
                            tokens.append(Token(TokenType.IF, word))
                        elif word == 'endif':
                            tokens.append(Token(TokenType.ENDIF, word))
                        elif word == 'goto':
                            tokens.append(Token(TokenType.GOTO, word))
                        elif word in var_class.var:
                            tokens.append(Token(TokenType.VARIABLE, word))
                        elif word.startswith('"') and word.endswith('"') or word.startswith("'") and word.endswith("'"):
                            tokens.append(Token(TokenType.STRING, word))
                        else:
                            tokens.append(Token(TokenType.UNEXPECTED_KEYWORD, word))
                        tokens.append(Token(TokenType.EOF, None))
                        return tokens
                
                if word == 'print':
                    tokens.append(Token(TokenType.PRINT, word))
                elif word == 'def':
                    tokens.append(Token(TokenType.DEFINE, word))
                elif word == 'if':
                    tokens.append(Token(TokenType.IF, word))
                elif word == 'endif':
                    tokens.append(Token(TokenType.ENDIF, word))
                elif word == 'goto':
                            tokens.append(Token(TokenType.GOTO, word))
                elif word in var_class.var:
                    tokens.append(Token(TokenType.VARIABLE, word))
                elif word.startswith('"') and word.endswith('"') or word.startswith("'") and word.endswith("'"):
                    tokens.append(Token(TokenType.STRING, word))
                else:
                    tokens.append(Token(TokenType.UNEXPECTED_KEYWORD, word))

            if char.isdigit(): #
                digits = ''
                while current_pos < len(input_text) and input_text[current_pos].isdigit():
                    digits += input_text[current_pos]
                    current_pos += 1
                tokens.append(Token(TokenType.INTEGER, int(digits)))
            
            elif char == '+':
                tokens.append(Token(TokenType.PLUS, char))
                current_pos += 1
            
            elif char == '-':
                tokens.append(Token(TokenType.MINUS, char))
                current_pos += 1
            
            elif char == '*':
                tokens.append(Token(TokenType.MULTIPLICATION, char))
                current_pos += 1
            
            elif char == '/':
                tokens.append(Token(TokenType.DIVIDE, char))
                current_pos += 1

            elif char == '=' and double_eq==False:
                tokens.append(Token(TokenType.EQUALS, char))
                current_pos += 1
            
            elif char == '(':
                tokens.append(Token(TokenType.OE, char))
                current_pos += 1
            
            elif char == ')':
                tokens.append(Token(TokenType.CE, char))
                current_pos += 1

            elif char.isspace():
                current_pos += 1
        else:
            keyword+=char
            current_pos += 1
    tokens.append(Token(TokenType.EOF, None))
    return tokens