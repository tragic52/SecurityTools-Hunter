# 本程序使用默认的安装密码尝试登录网站，以此检查此类的工具站

import requests
import concurrent.futures
import time
import os
import argparse

banner= """
 ______     __  __     ______     ______     __  __    
/\  ___\   /\ \_\ \   /\  ___\   /\  ___\   /\ \/ /    
\ \ \____  \ \  __ \  \ \  __\   \ \ \____  \ \  _"-.  
 \ \_____\  \ \_\ \_\  \ \_____\  \ \_____\  \ \_\ \_\ 
  \/_____/   \/_/\/_/   \/_____/   \/_____/   \/_/\/_/ 

  Code by Adil
"""
print(banner)

#禁用requests的安全警告，不开启则会出现很多https报警,对结果无影响
requests.packages.urllib3.disable_warnings()

# 获取脚本所在的路径
script_path = os.path.dirname(os.path.abspath(__file__))

# 设置当前工作目录为脚本所在的路径
os.chdir(script_path)

# 检查Vshell的默认账密
def check_vshell_login(host):
    url = f"http://{host}/login/verify"

    data = {
        'username': 'admin',
        'password': 'qwe123qwe'
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Authorization': 'Basic YWRtaW46cXdlMTIzcXdl',
        'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest'
    }
    try:
        req = requests.post(url, headers=headers, data=data).json()
        if (req["status"] == 1):
            with open("vshell_default_login.txt","a+",encoding="utf-8") as f:
                f.write(f"{host}\n")

    except:
        with open("Vshell_ErrorConnection.log",mode="a+",encoding="utf-8") as f:
            f.write(f"{host}\n")

# 检查SuperShell默认账密
def check_supershell_login(host):
    data = {
        "username": "tdragon6",
        "password": "tdragon6"
    }
    try:
        req = requests.post(f"http://{host}/supershell/login/auth",json=data).json()
        if (req["result"] == "success"):
            with open("supershell_default_login.txt","a+",encoding="utf-8") as f:
                f.write(f"{host}\n")

    except:
        with open("SuperShell_ErrorConnection.log",mode="a+",encoding="utf-8") as f:
            f.write(f"{host}\n")

# 检查Nessus的默认账密
def check_nessus_login(host):
    url = f"https://{host}/session"

    data = {
        'username': 'admin',
        'password': 'Admin@tenable123'
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
        'Content-Type': 'application/json',
    }
    req = requests.post(url, headers=headers, json=data,verify=False).json()
    try:
        if (req["token"] != ""):
            with open("nessus_default_login.txt","a+",encoding="utf-8") as f:
                f.write(f"{host}\n")

    except:
        with open("Nessus_ErrorConnection.log",mode="a+",encoding="utf-8") as f:
            f.write(f"{host}\n")

# 检查ARL的默认账密
def check_arl_login(host):
    url = f"https://{host}/api/user/login"

    data = {
        'username': 'admin',
        'password': 'arlpass'
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
        'Content-Type': 'application/json',
    }
    try:
        req = requests.post(url, headers=headers, json=data,verify=False).json()
        if (req["code"] == 200):
            with open("arl_default_login.txt","a+",encoding="utf-8") as f:
                f.write(f"{host}\n")
    except:
        with open("ARL_ErrorConnection.log",mode="a+",encoding="utf-8") as f:
            f.write(f"{host}\n")

# 检查NPS的默认密码
def check_nps_login(host):
    url = f"http://{host}/login/verify"

    headers = {
        "X-Requested-With": "XMLHttpRequest",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Accept": "*/*",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
        "Connection": "keep-alive"
    }

    data = {
        "username": "admin",
        "password": "123"
    }
    try:
        response = requests.post(url, headers=headers, data=data).json()

        if response['status'] == 1:
            with open ("nps_default_login.txt",mode="a+",encoding="utf-8") as f:
                f.write(f"{host}\n")
    except:
        with open("NPS_ErrorConnection.log",mode="a+",encoding="utf-8") as f:
            f.write(f"{host}\n")


# 程序主函数，用以启动检查
def main():
    # 获取开始时间
    start_time = time.time()

    # 计数器
    count = 0

    # 参数解析
    parser = argparse.ArgumentParser()

    parser.add_argument("-f",
                        "--file",
                        help="Target File; Example:host.txt"
    )
    parser.add_argument("-p",
                        "--payload",
                        help="Target payload; Example:nessus、supershell、vshell、arl、nps")
    
    args = parser.parse_args()

    if args.payload == "nessus":
        payload = check_nessus_login
    elif args.payload == "supershell":
        payload = check_supershell_login
    elif args.payload == "vshell":
        payload = check_vshell_login
    elif args.payload == "arl":
        payload = check_arl_login
    elif args.payload == "nps":
        payload = check_nps_login
    else:
        print("请输入正确的payload!!!\n目前仅支持检查nessus、supershell、vshell、arl、nps")
        exit()
    
    print("检查程序正在启动~~~~~")
    
    with open(args.file,"r",encoding="utf-8") as f:
        # 创建一个线程池，设置最大工作线程为30
        with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
            # 创建一个数组，用于保存每个执行任务的对象
            to_do = []

            #读取文本中的url参数，提交给执行器执行
            for host in f.read().splitlines():
                # 执行函数，返回执行对象
                future = executor.submit(payload, f"{host}")

                # 将每个执行对象都添加到任务对象数组中
                to_do.append(future)
            
            # 遍历任务对象数据，返回执行器已完成的任务
            for future in concurrent.futures.as_completed(to_do):
                count += 1
                print(f"已完成检查{count}条对象")
    
    # 获取结束时间
    end_time = time.time()

    # 计算执行时间
    execution_time = end_time - start_time
    print(f"本次程序执行时间为：{execution_time}")

if __name__=="__main__":
    main()
