#! /usr/bin/python -i
# coding=utf-8

import udkanbun,os
PACKAGE_DIR=os.path.abspath(os.path.dirname(__file__))

def load():
  m=os.path.join(PACKAGE_DIR,"ud-chinese.udpipe")
  return udkanbun.UDKanbun(mecab=False,danku=False,model=m)

