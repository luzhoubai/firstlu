

from setuptools import setup

setup(
    name='sayhello',
    version='1.0',
    packages=['sayhello','writedoc'],
    py_modules=[''],
    url='',
    license='',
    author='luzho',
    author_email='luzhoubai@qq.com',
    description='say hello to world',
    entry_points={
        'console_scripts': [  # 命令的入口
            'sayhello=sayhello.main:printhello',
            'readtext=sayhello.main:read1txt',
            'writedocx=writedoc.wr:w'
        ]
    }
)
