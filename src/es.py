from parser_es import parse
from lexer_es import lexer
import argparse
import time

#python -m PyInstaller es.py

use_interpreter = False

# Step 4: Interpreter
def interpret(input_text):
    tokens = lexer(input_text)
    result = parse(tokens)
    return result

def parse_lines_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return lines
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return []

def command():
    parser = argparse.ArgumentParser(description='ESplit')
    parser.add_argument('run', help='run')
    args = parser.parse_args()

    if args.run.endswith('.es'):
        code=parse_lines_from_file(args.run)
        return code
    else:
        print('please enter .es file')
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
    else:
        i+=1
final_time=time.perf_counter()
print(f"/finished in: {final_time-start_time}/")