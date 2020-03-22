# docker pull
```
# https://hub.docker.com/layers/tensorflow/tensorflow/latest-gpu-py3-jupyter/images/sha256-901b827b19d14aa0dd79ebbd45f410ee9dbfa209f6a4db71041b5b8ae144fea5?context=explore
ubuntu@ubuntu:~$ docker pull tensorflow/tensorflow:latest-gpu-py3-jupyter
ubuntu@ubuntu:~$ docker run --gpus all -it --rm tensorflow/tensorflow:latest-gpu-py3-jupyter    python -c "import tensorflow as tf; print(tf.__version__)"
2020-03-22 01:30:26.762317: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libnvinfer.so.6
2020-03-22 01:30:26.763871: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libnvinfer_plugin.so.6
2.1.0

ubuntu@ubuntu:~$ docker run --gpus all -it --rm tensorflow/tensorflow:latest-gpu-py3-jupyter python -c "import platform; print(platform.python_version())"
3.6.9

ubuntu@ubuntu:~$ docker run --gpus all -it --rm tensorflow/tensorflow:latest-gpu-py3-jupyter python -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([3, 3])))"
2020-03-22 01:41:32.327232: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libnvinfer.so.6
2020-03-22 01:41:32.328860: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libnvinfer_plugin.so.6
2020-03-22 01:41:32.930490: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcuda.so.1
2020-03-22 01:41:32.939621: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2020-03-22 01:41:32.940409: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1555] Found device 0 with properties: 
pciBusID: 0000:01:00.0 name: GeForce GTX 950M computeCapability: 5.0
coreClock: 1.124GHz coreCount: 5 deviceMemorySize: 1.96GiB deviceMemoryBandwidth: 29.83GiB/s
2020-03-22 01:41:32.940462: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcudart.so.10.1
2020-03-22 01:41:32.940543: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcublas.so.10
2020-03-22 01:41:32.942010: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcufft.so.10
2020-03-22 01:41:32.942476: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcurand.so.10
2020-03-22 01:41:32.944212: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcusolver.so.10
2020-03-22 01:41:32.945320: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcusparse.so.10
2020-03-22 01:41:32.945355: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcudnn.so.7
2020-03-22 01:41:32.945514: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2020-03-22 01:41:32.946114: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2020-03-22 01:41:32.946592: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1697] Adding visible gpu devices: 0
2020-03-22 01:41:32.946935: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
2020-03-22 01:41:32.972409: I tensorflow/core/platform/profile_utils/cpu_utils.cc:94] CPU Frequency: 2592000000 Hz
2020-03-22 01:41:32.973440: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x42c7c00 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2020-03-22 01:41:32.973473: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
2020-03-22 01:41:33.021110: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2020-03-22 01:41:33.021808: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x434dac0 initialized for platform CUDA (this does not guarantee that XLA will be used). Devices:
2020-03-22 01:41:33.021826: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): GeForce GTX 950M, Compute Capability 5.0
2020-03-22 01:41:33.022460: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2020-03-22 01:41:33.022977: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1555] Found device 0 with properties: 
pciBusID: 0000:01:00.0 name: GeForce GTX 950M computeCapability: 5.0
coreClock: 1.124GHz coreCount: 5 deviceMemorySize: 1.96GiB deviceMemoryBandwidth: 29.83GiB/s
2020-03-22 01:41:33.023010: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcudart.so.10.1
2020-03-22 01:41:33.023025: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcublas.so.10
2020-03-22 01:41:33.023043: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcufft.so.10
2020-03-22 01:41:33.023059: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcurand.so.10
2020-03-22 01:41:33.023074: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcusolver.so.10
2020-03-22 01:41:33.023089: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcusparse.so.10
2020-03-22 01:41:33.023113: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcudnn.so.7
2020-03-22 01:41:33.023190: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2020-03-22 01:41:33.023855: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2020-03-22 01:41:33.024473: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1697] Adding visible gpu devices: 0
2020-03-22 01:41:33.024519: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcudart.so.10.1
2020-03-22 01:41:33.299903: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1096] Device interconnect StreamExecutor with strength 1 edge matrix:
2020-03-22 01:41:33.299944: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1102]      0 
2020-03-22 01:41:33.299969: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1115] 0:   N 
2020-03-22 01:41:33.300306: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2020-03-22 01:41:33.300893: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2020-03-22 01:41:33.301523: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1241] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 1142 MB memory) -> physical GPU (device: 0, name: GeForce GTX 950M, pci bus id: 0000:01:00.0, compute capability: 5.0)
tf.Tensor(5.376428, shape=(), dtype=float32)
```

# docker run [tensorflow] container, configure jupyter notebook
```
ubuntu@ubuntu:~/02_Documents/04_DeepLearning_WorkSpace$ docker run --gpus all -it -p 8888:8888 -v `pwd`/DeepLearning-Study:/tf/DeepLearning-Study --name tensorflow tensorflow/tensorflow:latest-gpu-py3-jupyter

________                               _______________                
___  __/__________________________________  ____/__  /________      __
__  /  _  _ \_  __ \_  ___/  __ \_  ___/_  /_   __  /_  __ \_ | /| / /
_  /   /  __/  / / /(__  )/ /_/ /  /   _  __/   _  / / /_/ /_ |/ |/ / 
/_/    \___//_/ /_//____/ \____//_/    /_/      /_/  \____/____/|__/


WARNING: You are running this container as root, which can cause new files in
mounted volumes to be created as the root user on your host machine.

To avoid this, run the container by specifying your user's userid:

$ docker run -u $(id -u):$(id -g) args...

[I 07:28:33.829 NotebookApp] Writing notebook server cookie secret to /root/.local/share/jupyter/runtime/notebook_cookie_secret
jupyter_http_over_ws extension initialized. Listening on /http_over_websocket
[I 07:28:34.023 NotebookApp] Serving notebooks from local directory: /tf
[I 07:28:34.024 NotebookApp] The Jupyter Notebook is running at:
[I 07:28:34.024 NotebookApp] http://517c57d416ea:8888/?token=342f318ad82ba2a6bf9f3066b2b66985ecf9aad759c8df6b
[I 07:28:34.024 NotebookApp]  or http://127.0.0.1:8888/?token=342f318ad82ba2a6bf9f3066b2b66985ecf9aad759c8df6b
[I 07:28:34.024 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 07:28:34.029 NotebookApp] 
    
    To access the notebook, open this file in a browser:
        file:///root/.local/share/jupyter/runtime/nbserver-1-open.html
    Or copy and paste one of these URLs:
        http://517c57d416ea:8888/?token=342f318ad82ba2a6bf9f3066b2b66985ecf9aad759c8df6b
     or http://127.0.0.1:8888/?token=342f318ad82ba2a6bf9f3066b2b66985ecf9aad759c8df6b
[I 07:28:40.380 NotebookApp] 302 GET /?token=342f318ad82ba2a6bf9f3066b2b66985ecf9aad759c8df6b (172.17.0.1) 0.66ms

# new terminal
ubuntu@ubuntu:~/Documents/04_DeepLearning_WorkSpace$ docker exec -it tensorflow bash

________                               _______________                
___  __/__________________________________  ____/__  /________      __
__  /  _  _ \_  __ \_  ___/  __ \_  ___/_  /_   __  /_  __ \_ | /| / /
_  /   /  __/  / / /(__  )/ /_/ /  /   _  __/   _  / / /_/ /_ |/ |/ / 
/_/    \___//_/ /_//____/ \____//_/    /_/      /_/  \____/____/|__/


WARNING: You are running this container as root, which can cause new files in
mounted volumes to be created as the root user on your host machine.

To avoid this, run the container by specifying your user's userid:

$ docker run -u $(id -u):$(id -g) args...

root@517c57d416ea:/tf# ps -ef
UID        PID  PPID  C STIME TTY          TIME CMD
root         1     0  0 07:28 pts/0    00:00:00 /usr/bin/python3 /usr/local/bin/jupyter-notebook --notebook-dir=/tf --ip 0.0.0.0 --no-browser --allow-root
root        12     0  6 07:30 pts/1    00:00:00 bash
root        21    12  0 07:30 pts/1    00:00:00 ps -ef

root@517c57d416ea:/tf# ll
total 16
drwxrwxrwx 1 root root 4096 Mar 22 07:28 ./
drwxr-xr-x 1 root root 4096 Mar 22 07:28 ../
drwxrwxr-x 8 1000 1000 4096 Mar 21 06:24 DeepLearning-Study/
drwxrwxrwx 1 root root 4096 Jan 11 18:48 tensorflow-tutorials/

root@517c57d416ea:/tf# cd ~/.jupyter/
root@517c57d416ea:~/.jupyter# ll
total 12
drwxr-xr-x 2 root root 4096 Jan 11 18:48 ./
drwx------ 1 root root 4096 Mar 22 07:28 ../
-rw-r--r-- 1 root root   96 Jan 11 18:48 jupyter_notebook_config.json

root@517c57d416ea:~/.jupyter# cat jupyter_notebook_config.json 
{
  "NotebookApp": {
    "nbserver_extensions": {
      "jupyter_http_over_ws": true
    }
  }
}

root@517c57d416ea:~/.jupyter# jupyter notebook password
Enter password: 
Verify password: 
[NotebookPasswordApp] Wrote hashed password to /root/.jupyter/jupyter_notebook_config.json

root@517c57d416ea:~/.jupyter# cat jupyter_notebook_config.json 
{
  "NotebookApp": {
    "nbserver_extensions": {
      "jupyter_http_over_ws": true
    },
    "password": "sha1:ff9dc0022d26:1ef40445afdacac32d8aee1fd32d5ad92f18ced0"
  }
}

root@517c57d416ea:~/.jupyter# sed -i 's/sha1:ff9dc0022d26:1ef40445afdacac32d8aee1fd32d5ad92f18ced0//' jupyter_notebook_config.json 
root@517c57d416ea:~/.jupyter# cat jupyter_notebook_config.json 
{
  "NotebookApp": {
    "nbserver_extensions": {
      "jupyter_http_over_ws": true
    },
    "password": ""
  }
}

root@517c57d416ea:~/.jupyter# exit
exit

ubuntu@ubuntu:~/Documents/04_DeepLearning_WorkSpace$ docker ps
CONTAINER ID        IMAGE                                          COMMAND                  CREATED             STATUS                 PORTS                                                             NAMES
517c57d416ea        tensorflow/tensorflow:latest-gpu-py3-jupyter   "bash -c 'source /et…"   5 minutes ago       Up 5 minutes           0.0.0.0:8888->8888/tcp                                            tensorflow
```

# restart [tensorflow] container
```
# previous terminal
^C[I 07:36:20.453 NotebookApp] interrupted
Serving notebooks from local directory: /tf
0 active kernels
The Jupyter Notebook is running at:
http://517c57d416ea:8888/?token=342f318ad82ba2a6bf9f3066b2b66985ecf9aad759c8df6b
 or http://127.0.0.1:8888/?token=342f318ad82ba2a6bf9f3066b2b66985ecf9aad759c8df6b
Shutdown this notebook server (y/[n])? y
[C 07:36:22.118 NotebookApp] Shutdown confirmed
[I 07:36:22.119 NotebookApp] Shutting down 0 kernels

ubuntu@ubuntu:~/02_Documents/04_DeepLearning_WorkSpace$ docker start tensorflow 
tensorflow

# open http://127.0.0.1:8888 without password for tensorflow
```