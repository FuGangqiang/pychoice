import os
from setuptools import setup


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    long_description = f.read()


setup(
    name='pychoice',
    version='0.1.0',
    description='An utility adds code readability to your application and/or API, Code is documentation!',
    long_description=long_description,
    url='https://github.com/FuGangqiang/pychoice',
    author='FuGangqiang',
    author_email='fu_gangqiang@qq.com',
    keywords='choice',
    license='MIT',

    py_modules=['pychoice'],

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Documentation',
        'License :: OSI Approved :: MIT License',
    ],
)
