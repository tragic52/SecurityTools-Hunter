# SecurityTools-Hunter

用于狩猎公网上暴露的安全工具


## 一、简介

- 本程序用于批量化检查公网上他人部署的安全工具登录账户检查，使用默认的安装账户以及常用的账户进行登录尝试，若登录成功则会输出该目标主机`HOST`于文本中。
- 默认账户如下：

| 项目       | 介绍                                    | 默认账密/常用账密 |
| ---------- | --------------------------------------- | ----------------- |
| SuperShell | 一款优秀的C2工具，自带免杀效果          | tdragon6/tdragon6 |
| Vshell     | 一款优秀的C2工具，便于快速上线          | admin/qwe123qwe   |
| Nessus     | 全球大量使用的商业化扫描器(Tenable)     | admin/admin       |
| ARL        | 斗象开源扫描器项目，针对WEB扫描效果不错 | admin/arlpass     |
| NPS        | 流量代理工具                            | admin/123         |

## 二、使用

- 示例：
  - 检查Vshell：` python SafetyToolsCapture.py -f HostList.txt -p vshell`

![image-20240107192133623](https://s2.loli.net/2024/01/07/rgqR3sbm94UxnJN.png)

- 帮助：
  - -f：指定Host地址(格式：IP:Port)
  - -p：指定Payload(当前仅支持SuperShell、Vshell、Nessus、ARL)

![image-20240107192339038](https://s2.loli.net/2024/01/07/iSuPOfzwvnENDae.png)

## 三、资产收集

- FOFA
  - supershell：`app="Supershell-远控平台"`
  - vshell：`app="Vshell-RAT"`
  - nessus：`app="tenable-Nessus"`
  - arl：`app="资产灯塔系统"`
  - nps:`app="nps"`
