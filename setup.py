#!/usr/bin/env python
# -*- coding:utf-8 -*-


from distutils.core import setup
from pinyin import __version__ as version

setup(
            name='pinyin',
            version=version,
            description='Simplified or Traditional Chinese -> pinyin,With Python',
            author='Qingfeng Xia',
            author_email='qingfeng dot xia@gmail.com',
            url='http://github.com/qingfengxia/pinyin.py',
            py_modules=['pinyin'],
            license='MIT License',
            platforms=['any'],
            classifiers=[
                'Development Status :: 4 - Beta',
                'Intended Audience :: Developers',
                'License :: OSI Approved :: MIT License',
                'Programming Language :: Python',
                'Topic :: Software Development',
                'Topic :: Software Development :: Libraries',
                'Topic :: Software Development :: Libraries :: Python Modules'
                ]
                    
    )
