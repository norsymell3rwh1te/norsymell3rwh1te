import json, random, time, socket, platform
timestr = time.strftime("%Y-%m-%d - %H:%M:%S UTC")
f = open("./build.sh", "w")
f.write(f'''
echo "{timestr}"

 ''')
f.close()