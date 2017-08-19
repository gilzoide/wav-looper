wav-loopy
=========
A simple WAV audio file looper: read file -> write file looped by X.

The following formats are allowed for X (using input sample size as basis for time):

* Number "1.2": output size is ``X * input size``
* Time in seconds "20.0s": output size is exactly ``X`` seconds
* Adition time in seconds "+10.0s": output size is ``input size + X`` seconds

*wav-loopy* also may fade out the last seconds of a track.


Usage
-----
::

    wav-loopy [-f FADE] [-o OUTPUT] INPUT X
    wav-loopy (-h | --help | --version)

Installing
----------
Using pip_::

    $ pip install wav-loopy

Or from the source code::

    $ python setup.py install

.. _pip: https://pypi.python.org/pypi/pip/)
