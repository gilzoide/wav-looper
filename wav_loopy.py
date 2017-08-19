#!/usr/bin/env python

# Copyright 2017 Gil Barbosa Reis <gilzoide@gmail.com>
#
# Wav-loopy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Wav-loopy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Wav-loopy.  If not, see <http://www.gnu.org/licenses/>.

"""
Wav-loopy is a simple WAV audio file looper: read file -> write file looped by X.

The following formats are allowed for X (using input sample size as basis for time):
  Number "1.2": output size is X * input size
  Time in seconds "20.0s": output size is exactly X seconds
  Adition time in seconds "+10.0s": output size is input size + X seconds


Usage:
    wav-loopy [-f FADE] [-o OUTPUT] INPUT X
    wav-loopy (-h | --help | --version)

Options:
    -h, --help                  Show this help.
    --version                   Show program version.
    -o OUTPUT, --output=OUTPUT  Looped WAV file output name. [default: loopyed.wav]
    -f FADE, --fade-out=FADE    Fade out the last <fade> seconds linearly. [default: 0]
"""

__version__ = '0.1.0'

from docopt import docopt
from scipy.io import wavfile
import numpy as np

import re
from math import ceil

class WavLooper:
    '''WAV manipulation controller'''
    def __init__(self, filename):
        self.sample_rate, self.wav = wavfile.read(filename)

    def input_size(self):
        '''Get the input WAV file size in samples'''
        return self.wav.shape[0]

    def sec2sample(self, s):
        '''Transforms from time in seconds to number of samples'''
        return int(self.sample_rate * s)

    def find_output_size(self, X):
        '''Find the number of samples of the output'''
        try:
            m = re.match(r"(\+?)(.+)s$", X)
            if not m:
                return int(float(X) * self.input_size())
            else:
                seconds = float(m.group(2))
                total = self.sec2sample(seconds)
                if m.group(1) == '+':
                    total += self.input_size()
                return total
        except ValueError:
            raise ValueError("Invalid format for loop factor {!r}".format(X))

    def loop(self, output_filename, X, fade):
        '''Loop the input file and write it to output'''
        output_size = self.find_output_size(X)
        output = np.tile(self.wav, [ceil(output_size / self.input_size()), 1])[:output_size]
        if fade:
            fade_num_samples = self.sec2sample(fade)
            step = 1.0 / fade_num_samples
            for i in range(fade_num_samples, 0, -1):
                output[-i] = np.multiply(output[-i], i * step, casting='unsafe')
        wavfile.write(output_filename, self.sample_rate, output)


def main():
    arguments = docopt(__doc__, version="wav-loopy " + __version__)
    looper = WavLooper(arguments['INPUT'])
    looper.loop(arguments['--output'], arguments['X'], float(arguments['--fade-out']))


if __name__ == '__main__':
    main()

