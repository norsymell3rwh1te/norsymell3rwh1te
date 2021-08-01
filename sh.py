import json, random, time, socket, platform, subprocess
timestr = time.strftime("%Y-%m-%d - %H:%M:%S UTC")
f = open("./build.sh", "w")
f.write(f'''
echo "{timestr}"

 ''')
f.close()
subprocess.call('git add . && \
git commit -am "fix" && \
git push origin main', shell=True)