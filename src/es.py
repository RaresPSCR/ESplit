from parser_es import parse
from lexer_es import lexer
import argparse
import time

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

source_code = []

def command():
    parser = argparse.ArgumentParser(description='ESplit')
    parser.add_argument('run', help='run')
    args = parser.parse_args()

    if args.run.endswith('.es'):
        source_code=parse_lines_from_file(args.run)
    else:
        print('please enter .es file')
command()

print('/start/')
start_time=time.perf_counter()
for i in source_code:
    result = interpret(i)
final_time=time.perf_counter()
print(f"/finished in: {final_time-start_time}/")