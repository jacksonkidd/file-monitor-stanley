File Integrity Monitoring Program

This simple program monitors a specified directory for any changes made to the files within it. It uses the SHA-256 hash algorithm to generate a unique checksum for each file, and compares these values to a previously created baseline of file and checksum pairs. If any changes have been made to the files in the directory since the baseline was created, the program will alert the user to the change.

Usage

    1. Open a terminal window and run the program by entering python file_monitor.py.
    2. When prompted, enter the directory that you would like to monitor.
    3. Choose one of the following options:

    ~ Create new baseline - This option will create a new baseline of file and checksum pairs for the specified directory.
    ~ Begin monitoring files - This option will begin monitoring the specified directory for any changes to the files within it, and will alert the user if any changes are detected.
    ~ Change directory - This option allows the user to change the directory being monitored.

    If you choose to create a new baseline, the program will generate a file named baseline.txt in the specified directory, containing the file and checksum pairs for all files in the directory.
    If you choose to monitor the files, the program will continuously monitor the specified directory for any changes to the files within it, and will alert the user if any changes are detected.
