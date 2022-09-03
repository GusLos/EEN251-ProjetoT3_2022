# Run first this script to prepare your environment.

try:
    from pip import main as pipmain
except ImportError:
    from pip._internal import main as pipmain

pipmain(['install', 'nltk'])

import nltk

nltk.download('stopwords', download_dir=".\\nltk")
nltk.data.path.append(".\\nltk")

