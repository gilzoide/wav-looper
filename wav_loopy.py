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
Wav-loopy, a simple WAV audio file looper: read file -> write file looped X times

The following formats are allowed for X (using input sample size as basis for time):
  Number "1.2": output size is X * input size
  Time in seconds "20s": output size is exactly X seconds
  Adition time in seconds "+10s": output size is input size + X seconds


Usage:
    wav_loopy [-f FADE] INPUT OUTPUT X
    wav_loopy (-h | --help | --version)

Options:
    -h, --help                Show this help.
    --version                 Show program version.
    -f FADE, --fade-out=FADE  Fade out the last <fade> seconds linearly [default: 0]
"""

__version__ = '0.0.1'

from docopt import docopt
from scipy.io import wavfile


def main():
    arguments = docopt(__doc__, version="wav_loopy " + __version__)


if __name__ == '__main__':
    main()

