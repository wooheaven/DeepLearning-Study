```{bash}
$ conda create --name p3.5 python=3.5.4
Fetching package metadata .........
Solving package specifications: .

Package plan for installation in environment /home/rwoo/03_Programs/anaconda/anaconda3/envs/p3.5:

The following NEW packages will be INSTALLED:

    certifi:    2016.2.28-py35_0
    openssl:    1.0.2l-0        
    pip:        9.0.1-py35_1    
    python:     3.5.4-0         
    readline:   6.2-2           
    setuptools: 36.4.0-py35_1   
    sqlite:     3.13.0-0        
    tk:         8.5.18-0        
    wheel:      0.29.0-py35_0   
    xz:         5.2.3-0         
    zlib:       1.2.11-0        

Proceed ([y]/n)? y
...

$ source activate p3.5

(p3.5) $ conda install pillow numpy matplotlib h5py tensorflow keras
Fetching package metadata .........
Solving package specifications: .

Package plan for installation in environment /home/rwoo/03_Programs/anaconda/anaconda3/envs/p3.5:

The following NEW packages will be INSTALLED:

    backports:              1.0-py35_0        
    backports.weakref:      1.0rc1-py35_0     
    bleach:                 1.5.0-py35_0      
    cycler:                 0.10.0-py35_0     
    dbus:                   1.10.20-0         
    expat:                  2.1.0-0           
    fontconfig:             2.12.1-3          
    freetype:               2.5.5-2           
    glib:                   2.50.2-1          
    gst-plugins-base:       1.8.0-0           
    gstreamer:              1.8.0-0           
    h5py:                   2.7.0-np113py35_0 
    hdf5:                   1.8.17-2          
    html5lib:               0.9999999-py35_0  
    icu:                    54.1-0            
    jbig:                   2.1-0             
    jpeg:                   9b-0              
    keras:                  2.0.5-py35_0      
    libffi:                 3.2.1-1           
    libgcc:                 5.2.0-0           
    libgfortran:            3.0.0-1           
    libgpuarray:            0.6.9-0           
    libiconv:               1.14-0            
    libpng:                 1.6.30-1          
    libprotobuf:            3.4.0-0           
    libtiff:                4.0.6-3           
    libxcb:                 1.12-1            
    libxml2:                2.9.4-0           
    mako:                   1.0.6-py35_0      
    markdown:               2.6.9-py35_0      
    markupsafe:             1.0-py35_0        
    matplotlib:             2.0.2-np113py35_0 
    mkl:                    2017.0.3-0        
    mkl-service:            1.1.2-py35_3      
    nose:                   1.3.7-py35_1      
    numpy:                  1.13.1-py35_0     
    olefile:                0.44-py35_0       
    pcre:                   8.39-1            
    pillow:                 4.2.1-py35_0      
    protobuf:               3.4.0-py35_0      
    pygpu:                  0.6.9-py35_0      
    pyparsing:              2.2.0-py35_0      
    pyqt:                   5.6.0-py35_2      
    python-dateutil:        2.6.1-py35_0      
    pytz:                   2017.2-py35_0     
    pyyaml:                 3.12-py35_0       
    qt:                     5.6.2-5           
    scipy:                  0.19.1-np113py35_0
    sip:                    4.18-py35_0       
    six:                    1.10.0-py35_0     
    tensorflow:             1.3.0-0           
    tensorflow-base:        1.3.0-py35_0      
    tensorflow-tensorboard: 0.1.5-py35_0      
    theano:                 0.9.0-py35_0      
    werkzeug:               0.12.2-py35_0     
    yaml:                   0.1.6-0           

Proceed ([y]/n)? y
...

(p3.5) $ mkdir ~/.matplotlib
(p3.5) $ vi ~/.matplotlib/matplotlibrc
backend : Agg

```
