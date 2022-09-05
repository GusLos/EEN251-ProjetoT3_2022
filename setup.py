# Run first this script to prepare your environment.

try:
    from pip import main as pipmain
except ImportError:
    from pip._internal import main as pipmain


pipmain(['install', 'nltk'])
pipmain(['install','pathlib '])

import pathlib
import nltk

path_nltk = pathlib.PurePath('.','nltk')

nltk.download('stopwords', download_dir=path_nltk)
nltk.data.path.append(path_nltk)

