#! /usr/bin/python -i
# coding=utf-8

import setuptools
URL="https://github.com/KoichiYasuoka/UD-Chinese"

setuptools.setup(
  name="udchinese",
  version="0.1.0",
  description="Tokenizer POS-tagger and Dependency-parser for Chinese (简体/繁體/文言文)",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url=URL,
  author="Koichi Yasuoka",
  author_email="yasuoka@kanji.zinbun.kyoto-u.ac.jp",
  license="MIT",
  keywords="udpipe nlp",
  packages=setuptools.find_packages(),
  install_requires=["udkanbun>=2.0.5"],
  python_requires=">=3.6",
  package_data={
    "udchinese":["./ud-chinese.udpipe"],
  },
  classifiers=[
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
    "Topic :: Text Processing :: Linguistic",
    "Natural Language :: Chinese",
  ],
  project_urls={
    "Source":URL,
    "Tracker":URL+"/issues",
  }
)
