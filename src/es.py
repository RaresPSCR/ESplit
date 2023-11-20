from parser_es import parse
from lexer_es import lexer
import argparse
import time

#python -m PyInstaller es.py

# bugs to solve:
#   no=nt uxk t

ctas = 0

use_interpreter = True

# Step 4: Interpreter
def interpret(input_text):
    tokens = lexer(input_text)
    for i in tokens:
        pass
        #print(i.type,i.value)
    result = parse(tokens)
    return result

def parse_lines_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return lines
    except FileNotFoundError:
        raise Exception(f"Error C01: File '{file_path}' not found.")

def command():
    parser = argparse.ArgumentParser(description='ESplit')
    parser.add_argument('file', help='file')
    args = parser.parse_args()

    if args.file.endswith('.es'):
        code=parse_lines_from_file(args.file)
        return code
    else:
        raise Exception(f"Error C02: File is not .es")
if use_interpreter:
    source_code = parse_lines_from_file(input('>'))
else:
    source_code = command()

print('/start/')
start_time=time.perf_counter()
i=0
while i < len(source_code):
    result = interpret(source_code[i])
    if result:
        if result.startswith('goto'):
            split_goto=result.split(' ')
            i=int(split_goto[1])-1
        if result=='ifnotentered':
            while not source_code[i].startswith("endif"):
                i+=1
            else:
                i+=1
    else:
        i+=1
final_time=time.perf_counter()
print(f"/finished in: {final_time-start_time}/")