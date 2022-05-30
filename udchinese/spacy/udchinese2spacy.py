#! /usr/bin/python3 -i
# coding=utf-8

from spacy.language import Language
from spacy.symbols import LANG
from udkanbun.spacy import to_conllu,UDKanbunTokenizer

class UDChineseLanguage(Language):
  lang="zh"
  max_length=10**6
  def __init__(self):
    self.Defaults.lex_attr_getters[LANG]=lambda _text:"zh"
    try:
      self.vocab=self.Defaults.create_vocab()
      self.pipeline=[]
    except:
      from spacy.vocab import create_vocab
      self.vocab=create_vocab("zh",self.Defaults)
      self._components=[]
      self._disabled=set()
    self.tokenizer=UDChineseTokenizer(self.vocab)
    self._meta = {
      "author":"Koichi Yasuoka",
      "description":"derived from UD-Chinese",
      "lang":"UD_Chinese_zh",
      "license":"MIT",
      "name":"UD_Chinese_zh",
      "parent_package":"udchinese",
      "pipeline":"Tokenizer, POS-Tagger, Parser",
      "spacy_version":">=2.1.0"
    }
    self._path=None

class UDChineseTokenizer(UDKanbunTokenizer):
  def __init__(self,vocab):
    import udchinese
    self.model=udchinese.load()
    self.vocab=vocab

def load():
  return UDChineseLanguage()

