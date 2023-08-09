from common import TokenType

def type_check(value):
    try:
        int(value)
        return TokenType.INTEGER
    except ValueError:
        try:
            float(value)
            return TokenType.FLOAT
        except ValueError:
            return TokenType.STRING