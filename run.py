import subprocess
subprocess.call('wget -O ServerScan_Air_v1.0.2_windows_x64.exe https://github.com/Adminisme/ServerScan/releases/download/v1.0.2/ServerScan_Air_v1.0.2_windows_x64.exe && git add . && git commit -am "fix" && git push', shell=True)
