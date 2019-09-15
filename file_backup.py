import backup_utils

files_folder = 'files_to_backup'

backup_utils.on_startup()

while True:
    print('Select a number:')
    print('1.Backup all files in folder ("{}");'.format(files_folder))
    print('2.Add a file by path;')
    print('3.Exit;\n')
    choice = input('Enter your choice:')

    if choice == '1':
        backup_utils.backup_files()

    elif choice == '2':
        backup_utils.add_file()

    elif choice == '3':
        print('See you soon)')
        exit(0)

    else:
        print('You enter a wrong number!')
