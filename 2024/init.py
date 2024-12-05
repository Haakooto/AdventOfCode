import os
import sys
import requests
import re
from datetime import datetime
import shutil

def get_AOC_title(year, day):
    url = f'https://adventofcode.com/{year}/day/{day}'
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
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    
    cookie = {"cookie": f'session={open("cookie.txt", "r").read()}'}
    response = requests.get(url, headers=cookie)
    
    if response.status_code == 200:
        return response.text
    
def create_folder(year, day):
    problem_name = get_AOC_title(year, day)
    if problem_name:
        folder_name = f"{day:02d}_{problem_name}"
        if not os.path.exists(folder_name):
            shutil.copytree("./00_base_day", folder_name, symlinks=False, ignore=None, ignore_dangling_symlinks=False, dirs_exist_ok=False)
            print(f"Created folder {folder_name}")
        return folder_name
    
def main():
    year = 2024
    if len(sys.argv) == 1:
        d = int(datetime.now().strftime("%d"))
    elif len(sys.argv) == 2:
        d = int(sys.argv[1])

    folder_name = create_folder(year, d)
    if folder_name:
        inp = get_AOC_input(year, d)
        if inp:
            with open(f"{folder_name}/input.txt", 'w') as f:
                f.write(inp)
        else:
            print("Error: Could not get input")
        with open(f"{folder_name}/test_input.txt", 'w') as f:
            f.write("")
        with open(f"{folder_name}/test_input_2.txt", 'w') as f:
            f.write("")
    else:
        print("Error: Could not create folder")

if __name__ == "__main__":
    main()
    
