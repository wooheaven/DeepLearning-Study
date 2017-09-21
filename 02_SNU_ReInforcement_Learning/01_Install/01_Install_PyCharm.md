```{text}
# Download PyCharm Community

# UnCompress
$ tar zxf pycharm-community-2017.2.3.tar.gz

# Icon
$ vi ~/pycharm.desktop 
[Desktop Entry]
Name=pycharm
Type=Application
Exec=/home/rwoo/03_Programs/pycharm/pycharm-community-2017.2.3/bin/pycharm.sh
Terminal=false
Icon=/home/rwoo/03_Programs/pycharm/pycharm-community-2017.2.3/bin/pycharm.png
Comment=Integrated Development Environment
NoDisplay=false
Categories=Development;IDE;
Name[en]=pycharm
Name[en_US]=pycharm

$ sudo desktop-file-install ~/pycharm.desktop
```
