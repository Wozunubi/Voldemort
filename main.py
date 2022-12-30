import os
from cryptography.fernet import Fernet

TARGET_FOLDER = "./targetFolder"
KEY_LOCATION = "./targetFolder/key"


def encrypt(fernet, folder):
    for file in os.listdir(folder):
        if os.path.isdir(os.path.join(folder, file)):
            encrypt(fernet, os.path.join(folder, file))
        elif file != "key":
            f1 = open(folder + "/" + file, "rt")
            f2 = open(folder + "/" + file + ".tmp", "wb")
            f2.write(fernet.encrypt(f1.read().encode()))
            f1 = open(folder + "/" + file, "wb")
            f2 = open(folder + "/" + file + ".tmp", "rb")
            f1.write(f2.read())
            f2.close()
            os.remove(folder + "/" + file + ".tmp")


def decrypt(fernet, folder):
    for file in os.listdir(folder):
        if os.path.isdir(os.path.join(folder, file)):
            decrypt(fernet, os.path.join(folder, file))
        elif file != "key":
            f1 = open(folder + "/" + file, "rb")
            f2 = open(folder + "/" + file + ".tmp", "wt")
            f2.write(fernet.decrypt(f1.read()).decode())
            f1 = open(folder + "/" + file, "wt")
            f2 = open(folder + "/" + file + ".tmp", "rt")
            f1.write(f2.read())
            f2.close()
            os.remove(folder + "/" + file + ".tmp")


if __name__ == '__main__':
    action = "i"
    while action != "x":
        action = input()
        if action == "en":
            f = open(KEY_LOCATION, "at")
            f.close()
            f = open(KEY_LOCATION, "rt")

            if f.read() == "":
                f.close()
                key = Fernet.generate_key()
                fernet = Fernet(key)

                encrypt(fernet, TARGET_FOLDER)

                f = open(KEY_LOCATION, "wb")
                f.write(key)

            f.close()
        elif action == "de":
            f = open(KEY_LOCATION, "rt")

            if f.read() != "":
                f.close()
                f = open(KEY_LOCATION, "rb")
                fernet = Fernet(f.read())
                f.close()

                decrypt(fernet, TARGET_FOLDER)

                f = open(KEY_LOCATION, "wb")

            f.close()