# docker run container
```{bash}
$ pwd
/home/rwoo/02_workspace/05_DeepLearning_Workspace/DeepLearning-Study/01_Tensorflow

$ docker run -it -p 6006:6006 -p 8888:8888 --name tensorflow \
-v /home/rwoo/02_workspace/01_DeepLearning_Workspace/DeepLearning-Study/01_Tensorflow/03_Workspace:/notebooks/03_Workspace tensorflow/tensorflow /bin/bash

root@0f3fc3ad17ad:/notebooks# ll
total 420
drwxr-xr-x  3 root root   4096 Apr 17 15:33 ./
drwxr-xr-x 48 root root   4096 Apr 17 15:33 ../
drwxrwxr-x  2 1000 1000   4096 Apr 16 16:09 03_Workspace/
-rw-r--r--  1 root root  25231 Apr 14 19:36 1_hello_tensorflow.ipynb
-rw-r--r--  1 root root 164559 Apr 14 19:36 2_getting_started.ipynb
-rw-r--r--  1 root root 209796 Apr 14 19:36 3_mnist_from_scratch.ipynb
-rw-r--r--  1 root root    333 Apr 14 19:36 BUILD
-rw-r--r--  1 root root    586 Apr 14 19:36 LICENSE

root@0f3fc3ad17ad:/notebooks# cd ..

root@0f3fc3ad17ad:/# ll
total 80
drwxr-xr-x  48 root root 4096 Apr 17 15:33 ./
drwxr-xr-x  48 root root 4096 Apr 17 15:33 ../
-rwxr-xr-x   1 root root    0 Apr 17 15:33 .dockerenv*
drwxr-xr-x   2 root root 4096 Apr 14 19:37 bin/
drwxr-xr-x   2 root root 4096 Apr 12  2016 boot/
drwxr-xr-x   5 root root  360 Apr 17 15:33 dev/
drwxr-xr-x  63 root root 4096 Apr 17 15:33 etc/
drwxr-xr-x   2 root root 4096 Apr 12  2016 home/
drwxr-xr-x  10 root root 4096 Apr 14 19:37 lib/
drwxr-xr-x   2 root root 4096 Apr 10 18:11 lib64/
drwxr-xr-x   2 root root 4096 Apr 10 18:10 media/
drwxr-xr-x   2 root root 4096 Apr 10 18:10 mnt/
drwxr-xr-x   3 root root 4096 Apr 17 15:33 notebooks/
drwxr-xr-x   2 root root 4096 Apr 10 18:10 opt/
dr-xr-xr-x 235 root root    0 Apr 17 15:33 proc/
drwx------   4 root root 4096 Apr 14 19:39 root/
drwxr-xr-x   6 root root 4096 Apr 14 19:37 run/
-rwxr-xr-x   1 root root  733 Apr 14 19:36 run_jupyter.sh*
drwxr-xr-x   2 root root 4096 Apr 12 21:06 sbin/
drwxr-xr-x   2 root root 4096 Apr 10 18:10 srv/
dr-xr-xr-x  13 root root    0 Apr 17 15:33 sys/
drwxrwxrwt   3 root root 4096 Apr 14 19:38 tmp/
drwxr-xr-x  21 root root 4096 Apr 12 21:06 usr/
drwxr-xr-x  16 root root 4096 Apr 12 21:06 var/

root@0f3fc3ad17ad:/# ./run_jupyter.sh --allow-root --notebook-dir=/notebooks/
[W 15:45:09.919 NotebookApp] WARNING: The notebook server is listening on all IP addresses and not using encryption. This is not recommended.
[I 15:45:09.929 NotebookApp] Serving notebooks from local directory: /notebooks
[I 15:45:09.929 NotebookApp] 0 active kernels 
[I 15:45:09.929 NotebookApp] The Jupyter Notebook is running at: http://[all ip addresses on your system]:8888/?token=81d9fc47e698835cbf7c29e8946559c41916a81a557a36c3
[I 15:45:09.929 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 15:45:09.930 NotebookApp] 
    
    Copy/paste this URL into your browser when you connect for the first time,
    to login with a token:
        http://localhost:8888/?token=81d9fc47e698835cbf7c29e8946559c41916a81a557a36c3
```

# docker start tensorflow
```{bash}
$ docker start tensorflow 
tensorflow

$ docker ps 
CONTAINER ID        IMAGE                   COMMAND             CREATED             STATUS              PORTS                                            NAMES
0f3fc3ad17ad        tensorflow/tensorflow   "/bin/bash"         2 weeks ago         Up 6 seconds        0.0.0.0:6006->6006/tcp, 0.0.0.0:8888->8888/tcp   tensorflow

$ docker exec -it tensorflow /bin/bash

root@0f3fc3ad17ad:/notebooks# 
```
