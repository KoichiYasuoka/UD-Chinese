[![Current PyPI packages](https://badge.fury.io/py/udchinese.svg)](https://pypi.org/project/udchinese/)

# UD-Chinese

Tokenizer, POS-Tagger, and Dependency-Parser for Chinese (简体/繁體/文言文), working on [Universal Dependencies](https://universaldependencies.org/format.html).

## Basic usage

```py
>>> import udchinese
>>> zh=udchinese.load()
>>> s=zh("我把这本书看完了。吾既讀是書也。")
>>> print(s)
```

## Usage via spaCy

If you have already installed [spaCy](https://pypi.org/project/spacy/) 2.1.0 or later, you can use UD-Chinese via spaCy Language pipeline.

```py
>>> import udchinese.spacy
>>> zh=udchinese.spacy.load()
>>> d=zh("我把这本书看完了。吾既讀是書也。")
>>> print(type(d))
<class 'spacy.tokens.doc.Doc'>
>>> print(udkanbun.spacy.to_conllu(d))
```

## Installation for Linux

Binary-wheel is available for Linux, and is installed by default when you use `pip`:
```sh
pip install udchinese
```

## Installation for Cygwin

Make sure to get `gcc-g++` `python37-pip` `python37-devel` packages, and then:
```sh
pip3.7 install udchinese
```
Use `python3.7` command in [Cygwin](https://www.cygwin.com/install.html) instead of `python`.

## Installation for Jupyter Notebook (Google Colaboratory)

```py
!pip install udchinese
```

## Author

Koichi Yasuoka (安岡孝一)

