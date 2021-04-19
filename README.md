# PlayVideoInConsole

Script for playing videofiles in console
![Example](https://github.com/Roqvie/PlayVideoInConsole/blob/main/examples/image.png?raw=true)
![Example](https://github.com/Roqvie/PlayVideoInConsole/blob/main/examples/image2.png?raw=true)
## Install
```sh
git clone https://github.com/Roqvie/PlayVideoInConsole.git
cd PlayVideoInConsole
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```
## Usage

Playing video with grayscale-based frames processing:
```sh
python play.py examples/rick.mp4 --shape 160 45 --image-type grayscale
```
Playing video with treshold-based frames processing:
```sh
python play.py examples/badapple.mp4 --symbols .# --shape 160 45 --image-type treshold --treshold 127
```
Help:
```sh
python play.py --help
```

