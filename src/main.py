from parser_es import parse
from lexer_es import lexer
import time
print('/start/')

# Step 4: Interpreter
def interpret(input_text):
    tokens = lexer(input_text)
    result = parse(tokens)
    return result

# Test the interpreter
start_time=time.perf_counter()
source_code = ['print "2*2"']
for i in source_code:
    result = interpret(i)
final_time=time.perf_counter()
print(f"/finished in: {final_time-start_time}/")