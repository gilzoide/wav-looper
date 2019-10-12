from setuptools import setup
from codecs import open

with open('README.rst', encoding='utf-8') as readme:
    long_description = readme.read()

setup(name='wav-loopy',
      version='0.1.0',
      description="A simple WAV audio file looper: read file -> write file looped by X",
      long_description=long_description,

      url="https://github.com/gilzoide/wav-loopy",
      author='gilzoide',
      author_email='gilzoide@gmail.com',

      license='GPLv3',
      classifiers=['Development Status :: 3 - Alpha',
                   'Environment :: Console',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 3'
      ],
      keywords="audio wav loop",
      install_requires=['numpy', 'scipy', 'docopt'],

      py_modules=['wav_loopy'],
      entry_points={
          'console_scripts': ['wav-loopy = wav_loopy:main']
      })

