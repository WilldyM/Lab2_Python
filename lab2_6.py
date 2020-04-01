import argparse
import os
import shutil
import datetime


def crArchive(path):
    if os.path.exists(path + '\Archive') is False:
        os.chdir(path)
        os.mkdir(str('Archive'))


def crSmall(path):
    if os.path.exists(path + '\Small') is False:
        os.chdir(path)
        os.mkdir(str('Small'))

parser = argparse.ArgumentParser(description='Lab6_Reorganize')
parser.add_argument('--source', type=str, help='Путь к файлам')
parser.add_argument('--days', type=int, help='Дата изменения файлов')
parser.add_argument('--size', type=int, help='Максимальный размер файлов')
args = parser.parse_args()

sourceArg = args.source
sourceArg = sourceArg.replace('\\\\', '\\')
print('Source: {}'.format(sourceArg))

daysArg = args.days
difference = datetime.date.today() - datetime.timedelta(days=daysArg)
print('Days: {0}\nDifference: {1}'.format(daysArg,difference))

sizeArg = args.size
print('Size: {}'.format(sizeArg))

if os.path.exists(sourceArg):
    if os.listdir(sourceArg) is not None:
        files = os.listdir(sourceArg)
        files = [os.path.join(sourceArg, file) for file in files]
        files = [file for file in files if os.path.isfile(file) is True]
        print(files)
        print()
        for file in files:
            print(file)
            if difference > datetime.date.fromtimestamp(os.stat(file).st_mtime):
                crArchive(sourceArg)
                shutil.move(file, sourceArg + '\Archive')
            if os.path.exists(file):
                if os.path.getsize(file) < sizeArg:
                    crSmall(sourceArg)
                    shutil.move(file, sourceArg + '\Small')
    else:
        print('Директория пуста!!!')























