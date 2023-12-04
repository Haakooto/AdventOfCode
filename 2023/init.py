import os
import sys
import requests
import re
from datetime import datetime

def get_AOC_title(year, day):
    url = f'https://adventofcode.com/{2023}/day/{day}'
    response = requests.get(url)
    
    if response.status_code == 200:
        content = response.text
        start = content.find('<h2>')
        end = content.find('</h2>', start)
        title = content[start + len('<h2>'): end]
        problem_name = title.split(': ')[1][:-3]
        problem_name = problem_name.strip().replace(' ', '_').lower()
        cleaned = re.sub(r'[^a-zA-Z0-9_]', '', problem_name)
        return cleaned

def get_AOC_input(year, day):
    url = f'https://adventofcode.com/{2023}/day/{day}/input'
    
    cookie = {"cookie": f'session={open("cookie.txt", "r").read()}'}
    response = requests.get(url, headers=cookie)
    
    if response.status_code == 200:
        return response.text
    
def create_folder(year, day):
    problem_name = get_AOC_title(year, day)
    if problem_name:
        folder_name = f"{day:02d}_{problem_name}"
        os.makedirs(folder_name)
        return folder_name
    
def main():
    if len(sys.argv) == 1:
        d = int(datetime.now().strftime("%d"))
    elif len(sys.argv) == 2:
        d = int(sys.argv[1])

    folder_name = create_folder(2023, d)
    if folder_name:
        inp = get_AOC_input(2023, d)
        if inp:
            with open(f"{folder_name}/input.txt", 'w') as f:
                f.write(inp)
        else:
            print("Error: Could not get input")
        with open(f"{folder_name}/test_input.txt", 'w') as f:
            f.write("")
        with open(f"{folder_name}/test_input_2.txt", 'w') as f:
            f.write("")
        with open(f"{folder_name}/solver.py", 'w') as f:
            f.write(open("base_file.py", 'r').read())
        print(f"Created folder {folder_name}")
    else:
        print("Error: Could not create folder")

if __name__ == "__main__":
    main()
    
