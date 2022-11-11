import hashlib
import os
import time


def main():
    path = directory_set()
    while True:
        print(f'What would you like to do?\n'
              f'-------\n'
              f'1) - Create new baseline\n'
              f'2) - Begin monitoring files\n'
              f'3) - Change directory\n'
              f'-------')
        user_choice = input('Please enter your choice: ')
        if user_choice == '1':
            base_str = read_hash(path)
            if len(base_str) == 0:      # When there are no files in path, re-prompt for new directory
                print(f'\n{path} directory is empty.\nPlease change the directory'
                      f' to a different path. \n')
                continue
            write_base(path, base_str)
        elif user_choice == '2':
            base_dict = read_base(path)
            if len(base_dict) == 0:         # If dictionary is returned empty, re-prompt user
                continue
            verify(path, base_dict)
        elif user_choice == '3':
            path = directory_set()
        else:
            print('Invalid input, please try again.')


def directory_set():    # Prompt user for Directory. Repeat if non-existent
    while True:
        path = input(r'Please enter the directory you would like to monitor: ')
        if os.path.exists(path):
            return path
        else:
            print('Error: Path is invalid. Please re-enter directory')


def read_hash(path):    # Open every file in directory, hash contents, add to dictionary
    base_str = ''
    for file in os.listdir(path):   # Iterate through each file
        try:
            digest = hashlib.sha256()   # Create object with SHA-256 hash algo
            with open(f'{path}\\{file}', 'rb') as check_file:
                file_content = check_file.read()  # Read contents into string
                digest.update(file_content)      # Add string to digest
                base_str += file + '|' + digest.hexdigest() + '\n'   # append file/hash pair to new string
        except PermissionError:     # Skip attempting to digest subdirectories
            pass

    return base_str


def write_base(path, base_str):     # Writes the baseline file/hash pairs to baseline.txt
    with open(f'{path}\\baseline.txt', 'w') as baseFile:
        baseFile.write(base_str)


def read_base(path):     # Reads baseline.txt, splits line by seperator, adds pairs to dictionary
    base_dict = {}
    try:
        with open(f'{path}\\baseline.txt', 'r') as base_file:
            for line in base_file:
                base_str = line.strip()
                base_list = base_str.split('|')
                base_dict[base_list[0]] = base_list[1]
    except FileNotFoundError:       # Catches error if baseline does not exist. dictionary will return empty
        print('Baseline file not found in directory. Please create new baseline or change your directory.')
    return base_dict


def verify(path, base_dict):
    verify_dict = {}
    base_dict.pop('baseline.txt')    # Remove baseline.txt k/v pair from base dictionary
    while True:
        time.sleep(5)       # Repeat loop every 5 seconds
        verify_str = read_hash(path)     # Hash files in directory
        verify_list = verify_str.splitlines()
        for pair in verify_list:     # Iterate through list, split by seperator, add pairs to dictionary
            verify_pair = pair.split('|')
            verify_dict[verify_pair[0]] = verify_pair[1]
        verify_dict.pop('baseline.txt')      # Remove baseline.txt k/v pair from verify dictionary
        if base_dict == verify_dict:
            print('All good here, folks.')
        else:
            print('ERROR! FILE HAS CHANGED!')


main()
