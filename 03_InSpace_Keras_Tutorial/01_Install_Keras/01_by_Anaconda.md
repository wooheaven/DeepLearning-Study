```{zsh}
conda info --envs
# conda environments:
#
python3.5                /Users/rwoo/anaconda/envs/python3.5
root                  *  /Users/rwoo/anaconda

conda create --name p2.7 python=2.7.12
Fetching package metadata .........
Solving package specifications: .

Package plan for installation in environment /Users/rwoo/anaconda/envs/p2.7:

The following NEW packages will be INSTALLED:

    certifi:    2016.2.28-py27_0
    openssl:    1.0.2l-0
    pip:        9.0.1-py27_1
    python:     2.7.12-1
    readline:   6.2-2
    setuptools: 36.4.0-py27_0
    sqlite:     3.13.0-0
    tk:         8.5.18-0
    wheel:      0.29.0-py27_0
    zlib:       1.2.11-0

Proceed ([y]/n)? y

#
# To activate this environment, use:
# > source activate p2.7
#
# To deactivate this environment, use:
# > source deactivate p2.7
#

source activate p2.7
(p2.7)

conda install ipython jupyter numpy scipy scikit-learn matplotlib pandas pydot h5py pil graphviz theano tensorflow
Fetching package metadata .........
Solving package specifications: .

Package plan for installation in environment /Users/rwoo/anaconda/envs/p2.7:

The following NEW packages will be INSTALLED:

    appnope:            0.1.0-py27_0
    backports:          1.0-py27_0
    backports_abc:      0.5-py27_0
    bleach:             1.5.0-py27_0
    configparser:       3.5.0-py27_0
    cycler:             0.10.0-py27_0
    decorator:          4.1.2-py27_0
    entrypoints:        0.2.3-py27_0
    enum34:             1.1.6-py27_0
    freetype:           2.5.5-2
    funcsigs:           1.0.2-py27_0
    functools32:        3.2.3.2-py27_0
    get_terminal_size:  1.0.0-py27_0
    graphviz:           2.38.0-3
    h5py:               2.7.0-np112py27_0
    hdf5:               1.8.17-2
    html5lib:           0.9999999-py27_0
    icu:                54.1-0
    ipykernel:          4.6.1-py27_0
    ipython:            5.3.0-py27_0
    ipython_genutils:   0.2.0-py27_0
    ipywidgets:         6.0.0-py27_0
    jbig:               2.1-0
    jinja2:             2.9.6-py27_0
    jpeg:               8d-2
    jsonschema:         2.6.0-py27_0
    jupyter:            1.0.0-py27_3
    jupyter_client:     5.1.0-py27_0
    jupyter_console:    5.2.0-py27_0
    jupyter_core:       4.3.0-py27_0
    lcms:               1.19-0
    libgpuarray:        0.6.9-0
    libpng:             1.6.30-1
    libprotobuf:        3.2.0-0
    libtiff:            4.0.6-2
    mako:               1.0.6-py27_0
    markupsafe:         1.0-py27_0
    matplotlib:         2.0.2-np112py27_0
    mistune:            0.7.4-py27_0
    mkl:                2017.0.3-0
    mkl-service:        1.1.2-py27_3
    mock:               2.0.0-py27_0
    nbconvert:          5.2.1-py27_0
    nbformat:           4.4.0-py27_0
    nose:               1.3.7-py27_1
    notebook:           5.0.0-py27_0
    numpy:              1.12.1-py27_0
    pandas:             0.20.3-py27_0
    pandocfilters:      1.4.2-py27_0
    path.py:            10.3.1-py27_0
    pathlib2:           2.3.0-py27_0
    pbr:                1.10.0-py27_0
    pexpect:            4.2.1-py27_0
    pickleshare:        0.7.4-py27_0
    pil:                1.1.7-py27_2
    prompt_toolkit:     1.0.15-py27_0
    protobuf:           3.2.0-py27_0
    ptyprocess:         0.5.2-py27_0
    pydot:              1.0.28-py27_0
    pygments:           2.2.0-py27_0
    pygpu:              0.6.9-py27_0
    pyparsing:          1.5.6-py27_0
    pyqt:               5.6.0-py27_2
    python-dateutil:    2.6.1-py27_0
    pytz:               2017.2-py27_0
    pyzmq:              16.0.2-py27_0
    qt:                 5.6.2-2
    qtconsole:          4.3.1-py27_0
    scandir:            1.5-py27_0
    scikit-learn:       0.19.0-np112py27_0
    scipy:              0.19.1-np112py27_0
    simplegeneric:      0.8.1-py27_1
    singledispatch:     3.4.0.3-py27_0
    sip:                4.18-py27_0
    six:                1.10.0-py27_0
    ssl_match_hostname: 3.5.0.1-py27_0
    subprocess32:       3.2.7-py27_0
    tensorflow:         1.1.0-np112py27_0
    terminado:          0.6-py27_0
    testpath:           0.3.1-py27_0
    theano:             0.9.0-py27_0
    tornado:            4.5.2-py27_0
    traitlets:          4.3.2-py27_0
    wcwidth:            0.1.7-py27_0
    werkzeug:           0.12.2-py27_0
    widgetsnbextension: 3.0.2-py27_0
    xz:                 5.2.3-0

Proceed ([y]/n)? y

conda install -c conda-forge keras
Fetching package metadata ...........
Solving package specifications: .

Package plan for installation in environment /Users/rwoo/anaconda/envs/p2.7:

The following NEW packages will be INSTALLED:

    keras:      2.0.6-py27_0      conda-forge
    pyyaml:     3.12-py27_1       conda-forge
    yaml:       0.1.6-0           conda-forge

The following packages will be SUPERSEDED by a higher-priority channel:

    tensorflow: 1.1.0-np112py27_0             --> 1.0.0-py27_0 conda-forge

Proceed ([y]/n)? y

conda list
# packages in environment at /Users/rwoo/anaconda/envs/p2.7:
#
appnope                   0.1.0                    py27_0
backports                 1.0                      py27_0
backports_abc             0.5                      py27_0
bleach                    1.5.0                    py27_0
certifi                   2016.2.28                py27_0
configparser              3.5.0                    py27_0
cycler                    0.10.0                   py27_0
decorator                 4.1.2                    py27_0
entrypoints               0.2.3                    py27_0
enum34                    1.1.6                    py27_0
freetype                  2.5.5                         2
funcsigs                  1.0.2                    py27_0
functools32               3.2.3.2                  py27_0
get_terminal_size         1.0.0                    py27_0
graphviz                  2.38.0                        3
h5py                      2.7.0               np112py27_0
hdf5                      1.8.17                        2
html5lib                  0.9999999                py27_0
icu                       54.1                          0
ipykernel                 4.6.1                    py27_0
ipython                   5.3.0                    py27_0
ipython_genutils          0.2.0                    py27_0
ipywidgets                6.0.0                    py27_0
jbig                      2.1                           0
jinja2                    2.9.6                    py27_0
jpeg                      8d                            2
jsonschema                2.6.0                    py27_0
jupyter                   1.0.0                    py27_3
jupyter_client            5.1.0                    py27_0
jupyter_console           5.2.0                    py27_0
jupyter_core              4.3.0                    py27_0
keras                     2.0.6                    py27_0    conda-forge
lcms                      1.19                          0
libgpuarray               0.6.9                         0
libpng                    1.6.30                        1
libprotobuf               3.2.0                         0
libtiff                   4.0.6                         2
mako                      1.0.6                    py27_0
markupsafe                1.0                      py27_0
matplotlib                2.0.2               np112py27_0
mistune                   0.7.4                    py27_0
mkl                       2017.0.3                      0
mkl-service               1.1.2                    py27_3
mock                      2.0.0                    py27_0
nbconvert                 5.2.1                    py27_0
nbformat                  4.4.0                    py27_0
nose                      1.3.7                    py27_1
notebook                  5.0.0                    py27_0
numpy                     1.12.1                   py27_0
openssl                   1.0.2l                        0
pandas                    0.20.3                   py27_0
pandocfilters             1.4.2                    py27_0
path.py                   10.3.1                   py27_0
pathlib2                  2.3.0                    py27_0
pbr                       1.10.0                   py27_0
pexpect                   4.2.1                    py27_0
pickleshare               0.7.4                    py27_0
pil                       1.1.7                    py27_2
pip                       9.0.1                    py27_1
prompt_toolkit            1.0.15                   py27_0
protobuf                  3.2.0                    py27_0
ptyprocess                0.5.2                    py27_0
pydot                     1.0.28                   py27_0
pygments                  2.2.0                    py27_0
pygpu                     0.6.9                    py27_0
pyparsing                 1.5.6                    py27_0
pyqt                      5.6.0                    py27_2
python                    2.7.12                        1
python-dateutil           2.6.1                    py27_0
pytz                      2017.2                   py27_0
pyyaml                    3.12                     py27_1    conda-forge
pyzmq                     16.0.2                   py27_0
qt                        5.6.2                         2
qtconsole                 4.3.1                    py27_0
readline                  6.2                           2
scandir                   1.5                      py27_0
scikit-learn              0.19.0              np112py27_0
scipy                     0.19.1              np112py27_0
setuptools                36.4.0                   py27_0
simplegeneric             0.8.1                    py27_1
singledispatch            3.4.0.3                  py27_0
sip                       4.18                     py27_0
six                       1.10.0                   py27_0
sqlite                    3.13.0                        0
ssl_match_hostname        3.5.0.1                  py27_0
subprocess32              3.2.7                    py27_0
tensorflow                1.0.0                    py27_0    conda-forge
terminado                 0.6                      py27_0
testpath                  0.3.1                    py27_0
theano                    0.9.0                    py27_0
tk                        8.5.18                        0
tornado                   4.5.2                    py27_0
traitlets                 4.3.2                    py27_0
wcwidth                   0.1.7                    py27_0
werkzeug                  0.12.2                   py27_0
wheel                     0.29.0                   py27_0
widgetsnbextension        3.0.2                    py27_0
xz                        5.2.3                         0
yaml                      0.1.6                         0    conda-forge
zlib                      1.2.11                        0
```
