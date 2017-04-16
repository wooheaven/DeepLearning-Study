# docker run container
```{bash}
$ pwd
/home/rwoo/02_workspace/05_DeepLearning_Workspace/DeepLearning-Study/01_Tensorflow/03_Workspace

$ docker run -it -p 8888:8888 tensorflow/tensorflow
[I 16:09:32.629 NotebookApp] Writing notebook server cookie secret to /root/.local/share/jupyter/runtime/notebook_cookie_secret
[W 16:09:32.649 NotebookApp] WARNING: The notebook server is listening on all IP addresses and not using encryption. This is not recommended.
[I 16:09:32.659 NotebookApp] Serving notebooks from local directory: /notebooks
[I 16:09:32.660 NotebookApp] 0 active kernels 
[I 16:09:32.660 NotebookApp] The Jupyter Notebook is running at: http://[all ip addresses on your system]:8888/?token=6c012464f922cd82a12fac044d7f1bfa5e57084d12126d1f
[I 16:09:32.660 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 16:09:32.660 NotebookApp] 
    
    Copy/paste this URL into your browser when you connect for the first time,
    to login with a token:
        http://localhost:8888/?token=6c012464f922cd82a12fac044d7f1bfa5e57084d12126d33
```
