import json, random, time, socket, platform

timestr = time.strftime("%Y-%m-%d - %H:%M:%S UTC")



f = open("./README.md", "w")

f.write(f'''

 <p align="left"> <img src="https://komarev.com/ghpvc/?username=xtenzq&label=Profile%20views&color=0e75b6&style=flat" alt="xtenzq" /> </p>  


<p align="left">
  <img src="https://img.shields.io/npm/v/readme-md-generator.svg?orange=blue" />
  <a href="https://www.npmjs.com/package/readme-md-generator">
    <img alt="downloads" src="https://img.shields.io/npm/dm/readme-md-generator.svg?color=blue" target="_blank" />
  </a>
  <a href="https://github.com/kefranabg/readme-md-generator/blob/master/LICENSE">
    <img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-yellow.svg" target="_blank" />
  </a>
  <a href="https://codecov.io/gh/kefranabg/readme-md-generator">
    <img src="https://codecov.io/gh/kefranabg/readme-md-generator/branch/master/graph/badge.svg" />
  </a>
  <a href="https://github.com/frinyvonnick/gitmoji-changelog">
    <img src="https://img.shields.io/badge/changelog-gitmoji-brightgreen.svg" alt="gitmoji-changelog">
  </a>
  <a href="https://mobile.twitter.com/_YannBertrand">
    <img alt="Twitter: blackerto" src="https://img.shields.io/twitter/follow/_YannBertrand.svg?style=social" target="_blank" />
  </a>
</p>
### 💻for  Linux or Windows

  * #### Scan Port
  
    * ***for PortScan***
    
      **Usage：**
    
      ![Air_scan_use](https://raw.githubusercontent.com/gegocpebblehelmer/gegocpebblehelmer/main/Linux/Pro_scan.png)

 ```bash

 Host Name : {socket.gethostname()}

 platform  : {platform.platform()}

 Ip Local  : {socket.gethostbyname(socket.gethostname())}

 ```
### Cobalt Strike

  * ***Windows***

       	{socket.gethostbyname(socket.gethostname())} Cobalt Strike PortScanï¼ŒServerScan ã€‚

      * ***for Service and Version Detection***

        Interact:

        ![serverscan_windows](https://github.com/gegocpebblehelmer/gegocpebblehelmer/raw/main/Windows/Air_scan_probes_use.png)

```bash

{timestr}

```

 ''')

f.close()
