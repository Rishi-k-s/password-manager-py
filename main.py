from secretsKey.secret import Encrypt


def main():
    # key = Encrypt.getMainKey()
    # print(key)
    encryptor = Encrypt()
    print(encryptor.encryptString("abc","qwe","123"))


if __name__ == "__main__":
    main()