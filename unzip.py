import rarfile
import zipfile
import py7zr

def dictionary_attack(file_path, dictionary_path):
    with open(dictionary_path, "r", encoding="utf8") as f:
        passwords = f.read().split("\n")

    if file_path.endswith(".zip"):
        zip_crack(file_path, passwords)
    elif file_path.endswith(".rar"):
        rar_crack(file_path, passwords)
    elif file_path.endswith(".7z"):
        seven_zip_crack(file_path, passwords)
    else:
        print("不支持的压缩包格式")

def zip_crack(file_path, passwords):
    print("正在破解 zip 压缩包...")
    zip_file = zipfile.ZipFile(file_path)
    for password in passwords:
        try:
            zip_file.extractall(pwd=password.encode("utf8"))
            print("破解成功，密码是：" + password)
            return
        except:
            pass
    print("破解失败")

def rar_crack(file_path, passwords):
    print("正在破解 rar 压缩包...")
    rar_file = rarfile.RarFile(file_path)
    for password in passwords:
        try:
            rar_file.extractall(pwd=password.encode("utf8"))
            print("破解成功，密码是：" + password)
            return
        except:
            pass
    print("破解失败")

def seven_zip_crack(file_path, passwords):
    print("正在破解 7z 压缩包...")
    for password in passwords:
        try:
            with py7zr.SevenZipFile(file_path, password=password) as archive:
                archive.extractall()
            print("破解成功，密码是：" + password)
            return
        except:
            pass
    print("破解失败")

if __name__ == "__main__":
    print("本软件只支持 7z, zip, rar 格式的压缩包")
    dictionary_path = input("请输入字典位置：")
    file_path = input("请输入要破解的压缩包位置：")
    dictionary_attack(file_path, dictionary_path)
