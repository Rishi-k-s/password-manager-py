from secretsKey.encrypt import Encrypt
from secretsKey.decrypt import Decrypt


def main():
    # key = Encrypt.getMainKey()
    # print(key)
    #test
    encryptor = Encrypt()
    decryptor = Decrypt()
    # Name Username Password
    encPass = encryptor.encryptString("abc","qwe","1234")

    print(decryptor.decryptString(encPass))


if __name__ == "__main__":
    main()