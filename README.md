# VAISARAPLOT
## About
This repository Program are made by annalyzing Vaisala radiosonde data.
このリポジトリはVaisalaのラジオゾンデのデータを図示できます。

## Environments
These program are made this environment.
- Python3.8
- Ubuntu20.04 LTS

## Required module (not built in)
- cartopy
- matplotlib
- pandas
- numpy

## Program List
- [vaisalaPlot.py](https://github.com/RyosukeDTomita/vaisalaPlot/blob/master/vaisalaPlot.py): VAISALAの画面ぽい図を作成する。
![VAISALA](https://github.com/RyosukeDTomita/vaisalaPlot/blob/master/samplefig/20210619_2330.png "VAISALA")

### おもちゃ
- [balloonLocation.py](https://github.com/RyosukeDTomita/vaisalaPlot/blob/master/balloonLocation.py): ゾンデのGPS情報を日本地図上に表示する。
![balloonLocation](https://github.com/RyosukeDTomita/vaisalaPlot/blob/master/samplefig/balloon.png "ballonLocation")
- [balloon3d.py](https://github.com/RyosukeDTomita/vaisalaPlot/blob/master/balloon3d.py): ゾンデの位置情報をGPS情報を3次元にプロットする。
![balloon3d](https://github.com/ryosukedtomita/vaisalaplot/blob/master/samplefig/balloon3d.png "balloon3d")
- [balloon3dgif.py](https://github.com/RyosukeDTomita/vaisalaPlot/blob/master/balloon3dgif.py)

![balloongif](https://github.com/ryosukedtomita/vaisalaplot/blob/master/samplefig/balloon.gif "balloon.gif")
- [wind.py](https://github.com/RyosukeDTomita/vaisalaPlot/blob/master/wind.py): [vaisalaPlot.py](https://github.com/RyosukeDTomita/vaisalaPlot/blob/master/vaisalaPlot.py)の風の鉛直プロファイルのみ。

## How to use

```shell
python3 vaisalaPlot.py -h
usage: vaisalaPlot.py [-h] [-i INPUT]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Select input file

python3 vaisalaPlot.py -i ../zonde/mirai_rs41_20210619_2330.txt
```

