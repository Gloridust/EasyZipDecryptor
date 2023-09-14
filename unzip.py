# 导入所需的模块
import rarfile
import zipfile
import py7zr

# 定义一个函数，用于进行字典攻击
def dictionary_attack(file_path, dictionary_path):
    # 打开并读取字典文件，将每个密码存储在一个列表中
    with open(dictionary_path, "r", encoding="utf8") as f:
        passwords = f.read().split("\n")

    # 根据文件类型选择适当的破解方法
    if file_path.endswith(".zip"):
        zip_crack(file_path, passwords)
    elif file_path.endswith(".rar"):
        rar_crack(file_path, passwords)
    elif file_path.endswith(".7z"):
        seven_zip_crack(file_path, passwords)
    else:
        print("不支持的压缩包格式")

# 定义一个函数，用于破解 ZIP 压缩包
def zip_crack(file_path, passwords):
    print("正在破解 zip 压缩包...")
    zip_file = zipfile.ZipFile(file_path)
    for password in passwords:
        try:
            # 尝试使用密码解压缩文件
            zip_file.extractall(pwd=password.encode("utf8"))
            print("破解成功，密码是：" + password)
            return
        except:
            pass
    print("破解失败")

# 定义一个函数，用于破解 RAR 压缩包
def rar_crack(file_path, passwords):
    print("正在破解 rar 压缩包...")
    rar_file = rarfile.RarFile(file_path)
    for password in passwords:
        try:
            # 尝试使用密码解压缩文件
            rar_file.extractall(pwd=password.encode("utf8"))
            print("破解成功，密码是：" + password)
            return
        except:
            pass
    print("破解失败")

# 定义一个函数，用于破解 7z 压缩包
def seven_zip_crack(file_path, passwords):
    print("正在破解 7z 压缩包...")
    for password in passwords:
        try:
            # 尝试使用密码解压缩文件
            with py7zr.SevenZipFile(file_path, password=password) as archive:
                archive.extractall()
            print("破解成功，密码是：" + password)
            return
        except:
            pass
    print("破解失败")

# 主程序入口
if __name__ == "__main__":
    print("本软件只支持 7z, zip, rar 格式的压缩包")
    dictionary_path = input("请输入字典位置：")
    file_path = input("请输入要破解的压缩包位置：")
    dictionary_attack(file_path, dictionary_path)
