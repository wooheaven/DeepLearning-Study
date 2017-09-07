```{bash}
$ docker pull tensorflow/tensorflow

$ docker images
REPOSITORY              TAG                 IMAGE ID            CREATED             SIZE
tensorflow/tensorflow   latest              2c520a260ba9        44 hours ago        1.13 GB

$ docker run -it --name tensorflow -p 6006:6006 -p 8888:8888 -v `pwd`/../03_Workspce:/notebook/Workspace tensorflow/tensorflow bash

root@c0120fbe6669:~# cd ~/.jupyter/

root@85ac9f78a27f:~/.jupyter# ipython
Python 2.7.12 (default, Nov 19 2016, 06:48:10) 
Type "copyright", "credits" or "license" for more information.

IPython 5.4.1 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: from IPython.lib import passwd

In [2]: passwd()
Enter password: deep
Verify password: deep
Out[2]: 'sha1:b6bd23676386:f4a6b18f7ce88383b71029640a0f7981b518e94c'

In [3]:                                                                                                                                                                                                     
Do you really want to exit ([y]/n)? y

root@85ac9f78a27f:~/.jupyter# cp jupyter_notebook_config.py jupyter_notebook_config.bak
root@85ac9f78a27f:~/.jupyter# head -17 jupyter_notebook_config.bak > jupyter_notebook_config.py 
root@85ac9f78a27f:~/.jupyter# cat >> jupyter_notebook_config.py << EOF
> c = get_config()
> c.NotebookApp.ip = '0.0.0.0'
> c.NotebookApp.port = 8888
> c.NotebookApp.open_browser = False
> c.MultiKernelManager.default_kernel_name = 'python2'
> c.NotebookApp.password = 'sha1:b6bd23676386:f4a6b18f7ce88383b71029640a0f7981b518e94c'
> c.NotebookApp.notebook_dir = '/notebook/'
> c.NotebookApp.allow_root = True
> EOF

root@4b5a7de303ed:~/.jupyter# jupyter notebook
[I 16:47:38.251 NotebookApp] Writing notebook server cookie secret to /root/.local/share/jupyter/runtime/notebook_cookie_secret
[I 16:47:38.292 NotebookApp] Serving notebooks from local directory: /notebook
[I 16:47:38.292 NotebookApp] 0 active kernels 
[I 16:47:38.292 NotebookApp] The Jupyter Notebook is running at: http://0.0.0.0:8888/
[I 16:47:38.293 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
```
