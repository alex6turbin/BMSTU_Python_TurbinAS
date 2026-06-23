import subprocess
import schedule
import shutil
import psutil
import time
import os

def add_user(username):
    subprocess.run(['sudo', 'useradd', username])
    print(f"Пользователь {username} добавлен.")

def remove_user(username):
    subprocess.run(['sudo', 'userdel', username])
    print(f"Пользователь {username} удален.")

def copy_file(src, dst):
    shutil.copy(src, dst)
    print(f"Файл {src} скопирован в {dst}")

def delete_file(filename):
    os.remove(filename)
    print(f"Файл {filename} удален.")

def monitor_resources():
    while True:
        cpu_percent = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory()
        disk = psutil.disk_usage('/')

        print(f"CPU загружен на: {cpu_percent}%")
        print(f"Памяти использовано: {mem.percent}%")
        print(f"Диск заполнен на: {disk.percent}%")
        print("-----------------------------")

        time.sleep(5)

def list_processes():
    for proc in psutil.process_iter(['pid', 'name']):
        print(f"PID: {proc.info['pid']}, Имя: {proc.info['name']}")

def job():
    print("Задача выполнена!")
    '''
        (Запуск задачи каждый день в 3:00)
    '''
    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == "__main__":
    print('Program is ready')
    # add_user('noviy_user')
    # remove_user('noviy_user')
    # copy_file('source.txt', 'destination.txt')
    # delete_file('src-dst/destination.txt')
    # list_processes()

    # Выполнение резервной копии данных:
    # shutil.copytree('/home/user/data', '/home/user/backup/data')
    # print("Копирование завершено")

    # Назначение прав доступа:
    # os.chmod('file.txt', 0o755)
    # print("Права доступа изменены")

    # job()
    # monitor_resources()