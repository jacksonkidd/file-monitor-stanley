import os, hashlib, time


def main():
    path = directory_set()
    while True:
        print(f'What would you like to do?\n'
              f'-------\n'
              f'1) - Create new baseline\n'
              f'2) - Begin monitoring files\n'
              f'3) - Change directory\n'
              f'-------')
        userChoice = input('Please enter your choice: ')
        if userChoice == '1':
            baseStr = read_hash(path)
            write_base(path, baseStr)
        elif userChoice == '2':
            baseDict = read_base(path)
            verify(path, baseDict)
        elif userChoice == '3':
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
    baseStr = ''
    for file in os.listdir(path):   # Iterate through each file
        digest = hashlib.sha256()   # Create object with SHA-256 hash algo
        with open(f'{path}\\{file}', 'rb') as checkFile:
            fileContent = checkFile.read()  # Read contents into string
            digest.update(fileContent)      # Add string to digest
            baseStr += file + '|' + digest.hexdigest() + '\n'   # append file/hash pair to new string
    return baseStr


def write_base(path, baseStr):     # Writes the baseline file/hash pairs to baseline.txt
    with open (f'{path}\\baseline.txt', 'w') as baseFile:
        baseFile.write(baseStr)


def read_base(path):     # Reads baseline.txt, splits line by seperator, adds pairs to dictionary
    baseDict = {}
    with open (f'{path}\\baseline.txt', 'r') as baseFile:
        for line in baseFile:
            baseStr = line.strip()
            baseList = baseStr.split('|')
            baseDict[baseList[0]] = baseList[1]
        return baseDict


def verify(path, baseDict):
    verifyDict = {}
    baseDict.pop('baseline.txt')    # Remove baseline.txt k/v pair from base dictionary
    while True:
        time.sleep(5)       # Repeat loop every 5 seconds
        verifyStr = read_hash(path)     # Hash files in directory
        verifyList = verifyStr.splitlines()
        for pair in verifyList:     # Iterate through list, split by seperator, add pairs to dictionary
            verifyPair = pair.split('|')
            verifyDict[verifyPair[0]] = verifyPair[1]
        verifyDict.pop('baseline.txt')      # Remove baseline.txt k/v pair from verify dictionary
        if baseDict == verifyDict:
            print('All good here, folks.')
        else:
            print('ERROR! FILE HAS CHANGED!')

main()
