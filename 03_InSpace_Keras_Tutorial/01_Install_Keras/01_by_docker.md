```{bash}
docker pull tensorflow/tensorflow:latest-py3
docker images

docker run -it -p 8888:8888 -p 6006:6006 -e PASSWORD=keras -v `pwd`/../:/notebooks/ --name keras tensorflow/tensorflow:latest-py3

Ctl + P + Q

docker exec -it keras /bin/bash
apt-get update
apt install graphviz
pip install pydot
pip install graphviz
pip install theano
pip install keras
exit

docker attach keras
```
