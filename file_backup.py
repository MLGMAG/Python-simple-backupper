import os
import datetime
import time
from zipfile import ZipFile
import shutil

current_path = os.getcwd()
files_folder = 'files_to_backup'
backup_folder = 'backups'
file_folder_path = current_path + os.sep + files_folder
backup_folder_path = current_path + os.sep + backup_folder


def get_folders_from_dir(path):
    objects_in_folder = os.listdir(path)
    folders = os.listdir(path)
    for item in objects_in_folder:
        for character in item:
            if character == '.':
                folders.remove(item)
                break
    del objects_in_folder
    return folders


# We need to check folder of those file containing


def on_startup():
    print()
    if files_folder not in get_folders_from_dir(current_path):
        os.mkdir(files_folder + os.sep)
        print('[Logger]: File ("{}") isn\'t exist, I create one'.format(files_folder))
    else:
        print('[Logger]: File ("{}") is exist'.format(files_folder))

    if backup_folder not in get_folders_from_dir(current_path):
        os.mkdir(backup_folder + os.sep)
        print('[Logger]: File ("{}") isn\'t exist, I create one'.format(backup_folder))
    else:
        print('[Logger]: File ("{}") is exist'.format(backup_folder))
    print()
    console_helper()


def console_helper():
    time.sleep(1)
    print('=========================================================================================')
    print('Hello, it\'s Backup Manager v.1.0.0')
    print('=========================================================================================')
    time.sleep(2)
    print('I can backup yours "important" files);\n')
    time.sleep(2)
    print('I can work in 2 ways:')
    time.sleep(1)
    print('First: you can put your files mainly in "{}" folder yourself;'.format(files_folder))
    time.sleep(3)
    print('Second: I can add those files (you just need to enter a path of the file);\n')
    time.sleep(3)


def backup_files():
    time.sleep(1)
    print('[Logger]: Now I\'am in ({}) folder'.format(file_folder_path))
    files_path = []
    files_in_folder = []
    for folder_path, folders_in_path, files in os.walk(file_folder_path):
        for file in files:
            if os.path.getsize(folder_path + os.sep + file) <= 1_048_576:
                files_path.append(folder_path + os.sep + file)
                files_in_folder.append(file)
            else:
                print('File: "{}" is to large (Max is 1MB);'.format(file))
    count_files_in_folder = len(files_in_folder)

    if count_files_in_folder == 0:
        time.sleep(1)
        print('[Logger]: No files to backup\n')
    elif count_files_in_folder >= 200:
        time.sleep(1)
        print('[Logger]: It\'s to many files: {}\n'.format(count_files_in_folder))
    else:
        zip_file_name = (datetime.datetime.now().strftime("%Y%m%d%H%M%S") + '.zip')
        print('[Logger]: Here it is {} files'.format(count_files_in_folder))
        time.sleep(1)
        print('[Logger]: Files in folder:', files_in_folder)
        time.sleep(1)
        print('[Logger]: Start creating of backup and backing up all files')
        backup = ZipFile(zip_file_name, 'w')
        for file in files_path:
            backup.write(file)
        backup.close()
        time.sleep(2)
        print('[Logger]: All files successfully backed up')
        time.sleep(1)
        print('[Logger]: Moving "{}" to ("{}") folder'.format(zip_file_name, backup_folder))
        shutil.move(current_path + os.sep + zip_file_name, backup_folder)
        time.sleep(1.5)
        print('Backup successfully completed!')
        print('You can find your backup in folder ("{}") with name "{}";\n'.format(backup_folder, zip_file_name))
        time.sleep(1)


def add_file():
    # print('Example: D:\\Games\\Nexus Mod Manager\\Skyrim\\Install Info\\InstallLog.xml')
    # file_path = input('Copy file path:')
    # print('[Logger]: I take a file path')
    # print('[Logger]: Staring moving of file')
    # shutil.copyfile(file_path, file_folder_path)
    # print('[Logger]: File successfully moved')
    print('Coming soon ;)')


on_startup()

while True:
    print('Select a number:')
    print('1.Backup all files in folder ("{}");'.format(files_folder))
    print('2.Add a file by path;')
    print('3.Exit;\n')
    choice = input('Enter your choice:')

    if choice == '1':
        backup_files()

    elif choice == '2':
        add_file()

    elif choice == '3':
        print('See you soon)')
        exit(0)

    else:
        print('You enter a wrong number!')
