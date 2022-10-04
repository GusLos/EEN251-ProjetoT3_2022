# Run first this script to prepare your environment.

try:
    from pip import main as pipmain
except ImportError:
    from pip._internal import main as pipmain


# pipmain(['install', 'nltk'])
# pipmain(['install','pathlib '])

# import pathlib
# import nltk
# path_nltk = pathlib.PurePath('.','nltk')

attempts: int = 0
while attempts <3:
    try:
        # nltk.data.path.append(path_nltk)
        pipmain(['install','selenium'])
        pipmain(['install','SpeechRecognition'])
        pipmain(['install','pyttsx3'])
        pipmain(['install','PyAudio'])
        attempts = 10
    except Exception as  e:
        print(f'Error: {e}')
        print(f'Attempt {attempts + 1} failed, trying again.')
        attempts+=1

# nltk.download('stopwords', download_dir=path_nltk)


