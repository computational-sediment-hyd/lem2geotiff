# lem2geotiff
python script to translate lem file to geotiff file

## lem2geotiff.translate

    """
    translate lem file to geotiff file

    Parameters
    ----------
    filepath : str
        a full path of a lem file
    valm1111 : float, default 60000
        value of the flag -1111 outside the data creation area
    valm9999 : float, default 50000
        value of the flag -9999 for the sea and land and water sections
    dtype : type, default np.uint16
        data type of a geotiff file
    """

## Usage

### Exmaple 1

```python
import lem2geotiff as l2g

l2g.translate('lem/****.lem')
```

### Exmaple 2

```python
import lem2geotiff as l2g
import glob

for ff in glob.glob( 'lem/*.lem'):
    l2g.translate(ff
```

## Environment

### Anaconda

Creating virtual environment:lem

```sh
conda create -y -n lem python=3.7
conda activate lem 
conda install -y -c conda-forge rioxarray
conda install -y -c conda-forge gdal
conda install -y -c conda-forge jupyter
```

### Google Colaboratory  

install rioxarray and activate work directory

```sh
!pip install rioxarray
```

```python
from google.colab import drive
drive.mount('/content/drive')
```

```sh
%cd "/content/drive/My Drive/*"
```

## Licence

[MIT](/LICENSE)

## Author

[computational-sediment-hyd](https://github.com/computational-sediment-hyd)

## SNS(in Japanese)

<a href="https://computational-sediment-hyd.hatenablog.jp/"><img src="github/logo/hatenablog-logotype.svg" width=25.0%><a href="https://twitter.com/CSHforF"><img src="github/logo/Twitter_Social_Icon_Rounded_Square_Color.svg" width=6%>

