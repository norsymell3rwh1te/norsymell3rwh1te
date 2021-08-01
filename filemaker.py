import json, random, time, socket, platform

timestr = time.strftime("%Y-%m-%d - %H:%M:%S UTC")



f = open("./README.md", "w")

f.write(f'''

 <p align="left"> <img src="https://komarev.com/ghpvc/?username=xtenzq&label=Profile%20views&color=0e75b6&style=flat" alt="xtenzq" /> </p>  


<p align="center">
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
  <a href="https://twitter.com/FranckAbgrall">
    <img alt="Twitter: FranckAbgrall" src="https://img.shields.io/twitter/follow/FranckAbgrall.svg?style=social" target="_blank" />
  </a>
</p>
## Code Contributors

This project exists thanks to all the people who contribute. [[Contribute](CONTRIBUTING.md)].
<a href="https://github.com/kefranabg/readme-md-generator/graphs/contributors"><img src="https://opencollective.com/readme-md-generator/contributors.svg?width=890&button=false" /></a>

### 💻for  Linux or Windows
  
    * ***for PortScan***
    
      **Usage**
    
      ![Air_scan_use](https://github.com/gegocpebblehelmer/gegocpebblehelmer/raw/main/Linux/Pro_scan.png)

 ```bash

 Host Name : {socket.gethostname()}

 platform  : {platform.platform()}

 Ip Local  : {socket.gethostbyname(socket.gethostname())}

 ```
### ðŸŽ®for Cobalt Strike

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
