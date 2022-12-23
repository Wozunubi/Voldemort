import os
from cryptography.fernet import Fernet

TARGET_FOLDER = "./targetFolder"


def encrypt():
    f = open(TARGET_FOLDER + "/key", "at")
    f.close()
    f = open(TARGET_FOLDER + "/key", "rt")
    if f.read() == "":
        f.close()
        key = Fernet.generate_key()
        fernet = Fernet(key)

        for file in os.listdir(TARGET_FOLDER):
            if file != "key":
                f1 = open(TARGET_FOLDER + "/" + file, "rt")
                f2 = open(TARGET_FOLDER + "/" + file + ".tmp", "wb")
                f2.write(fernet.encrypt(f1.read().encode()))
                f1 = open(TARGET_FOLDER + "/" + file, "wb")
                f2 = open(TARGET_FOLDER + "/" + file + ".tmp", "rb")
                f1.write(f2.read())
                f2.close()
                os.remove(TARGET_FOLDER + "/" + file + ".tmp")

        f = open(TARGET_FOLDER + "/key", "wb")
        f.write(key)
        f.close()


def decrypt():
    f = open(TARGET_FOLDER + "/key", "rt")
    if f.read() != "":
        f.close()
        f = open(TARGET_FOLDER + "/key", "rb")
        fernet = Fernet(f.read())
        f.close()

        for file in os.listdir(TARGET_FOLDER ):
            if file != "key":
                f1 = open(TARGET_FOLDER + "/" + file, "rb")
                f2 = open(TARGET_FOLDER + "/" + file + ".tmp", "wt")
                f2.write(fernet.decrypt(f1.read()).decode())
                f1 = open(TARGET_FOLDER + "/" + file, "wt")
                f2 = open(TARGET_FOLDER + "/" + file + ".tmp", "rt")
                f1.write(f2.read())
                f2.close()
                os.remove(TARGET_FOLDER + "/" + file + ".tmp")

        f = open(TARGET_FOLDER + "/key", "wb")
        f.close()


if __name__ == '__main__':
    action = "i"
    while action != "x":
        action = input()
        if action == "en":
            encrypt()
        elif action == "de":
            decrypt()