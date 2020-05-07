[![Current PyPI packages](https://badge.fury.io/py/udchinese.svg)](https://pypi.org/project/udchinese/)

# UD-Chinese

Tokenizer, POS-Tagger, and Dependency-Parser for Chinese ([简体](https://github.com/universaldependencies/UD_Chinese-GSDSimp)/[繁體](https://github.com/universaldependencies/UD_Chinese-GSD)/[文言文](https://github.com/universaldependencies/UD_Classical_Chinese-Kyoto)), working on [Universal Dependencies](https://universaldependencies.org/format.html).

## Basic usage

```py
>>> import udchinese
>>> zh=udchinese.load()
>>> s=zh("我把这本书看完了。吾既讀是書也。")
>>> print(s)
# newdoc
# newpar
# sent_id = 1
# text = 我把这本书看完了。
1	我	我	PRON	n,代名詞,人称,止格	Person=1|PronType=Prs	6	nsubj	_	SpaceAfter=No
2	把	把	ADP	BB	_	5	case	_	SpaceAfter=No
3	这	這	DET	DT	_	4	det	_	SpaceAfter=No
4	本	本	NOUN	n,名詞,描写,形質	_	5	clf	_	SpaceAfter=No
5	书	書	NOUN	n,名詞,主体,書物	_	6	obl:patient	_	SpaceAfter=No
6	看	看	VERB	v,動詞,行為,動作	_	0	root	_	SpaceAfter=No
7	完	完	VERB	v,動詞,変化,性質	_	6	mark	_	SpaceAfter=No
8	了	了	PART	UH	_	6	discourse	_	SpaceAfter=No
9	。	。	PUNCT	s,記号,句点,*	_	6	punct	_	SpacesAfter=\n

# sent_id = 2
# text = 吾既讀是書也。
1	吾	吾	PRON	n,代名詞,人称,起格	Person=1|PronType=Prs	3	nsubj	_	SpaceAfter=No
2	既	既	ADV	v,副詞,時相,完了	AdvType=Tim|Aspect=Perf	3	advmod	_	SpaceAfter=No
3	讀	讀	VERB	v,動詞,行為,動作	_	0	root	_	SpaceAfter=No
4	是	是	PRON	n,代名詞,指示,*	PronType=Dem	5	det	_	SpaceAfter=No
5	書	書	NOUN	n,名詞,主体,書物	_	3	obj	_	SpaceAfter=No
6	也	也	PART	p,助詞,句末,*	_	3	discourse:sp	_	SpaceAfter=No
7	。	。	PUNCT	s,記号,句点,*	_	3	punct	_	SpacesAfter=\n
```

## Usage via spaCy

If you have already installed [spaCy](https://pypi.org/project/spacy/) 2.1.0 or later, you can use UD-Chinese via spaCy Language pipeline.

```py
>>> import udchinese.spacy
>>> zh=udchinese.spacy.load()
>>> d=zh("我把这本书看完了。吾既讀是書也。")
>>> print(type(d))
<class 'spacy.tokens.doc.Doc'>
>>> print(udchinese.spacy.to_conllu(d))
# text = 我把这本书看完了。
1	我	我	PRON	n,代名詞,人称,止格	_	6	nsubj	_	SpaceAfter=No
2	把	把	ADP	BB	_	5	case	_	SpaceAfter=No
3	这	這	DET	DT	_	4	det	_	SpaceAfter=No
4	本	本	NOUN	n,名詞,描写,形質	_	5	clf	_	SpaceAfter=No
5	书	書	NOUN	n,名詞,主体,書物	_	6	obl:patient	_	SpaceAfter=No
6	看	看	VERB	v,動詞,行為,動作	_	0	root	_	SpaceAfter=No
7	完	完	VERB	v,動詞,変化,性質	_	6	mark	_	SpaceAfter=No
8	了	了	PART	UH	_	6	discourse	_	SpaceAfter=No
9	。	。	PUNCT	s,記号,句点,*	_	6	punct	_	_

# text = 吾既讀是書也。
1	吾	吾	PRON	n,代名詞,人称,起格	_	3	nsubj	_	SpaceAfter=No
2	既	既	ADV	v,副詞,時相,完了	_	3	advmod	_	SpaceAfter=No
3	讀	讀	VERB	v,動詞,行為,動作	_	0	root	_	SpaceAfter=No
4	是	是	PRON	n,代名詞,指示,*	_	5	det	_	SpaceAfter=No
5	書	書	NOUN	n,名詞,主体,書物	_	3	obj	_	SpaceAfter=No
6	也	也	PART	p,助詞,句末,*	_	3	discourse:sp	_	SpaceAfter=No
7	。	。	PUNCT	s,記号,句点,*	_	3	punct	_	_
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

