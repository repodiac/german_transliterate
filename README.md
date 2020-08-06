# german_transliterate

**german_transliterate** is a Python module to clean and transliterate (i.e. normalize) German text including abbreviations, numbers, timestamps etc. It can be used to clean messy text (e.g. map peculiar Unicode encodings to ASCII) or replace common abbreviations in text in combination with various text mining tasks.

However, it is particularly useful for Text-To-Speech (TTS) preprocessing (both in training and inference) and has features to support phonemic encoding of the results (e.g. with [espeak-ng](https://en.wikipedia.org/wiki/ESpeak#eSpeak_NG)) afterwards as next step in the processing pipeline.

Is has been successfully applied to preprocessing with [Mozilla TTS](https://github.com/mozilla/TTS) in combination with `espeak-ng` phonemes as input data to both training and inference pipeline.

## License and Attribution

This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

To provide **attribution or cite this work** please use the following text snippet:
```
german_transliterate, Copyright 2020 by repodiac, see https://github.com/repodiac for updates and further information
```

## Version History

* `release 0.1` - initial release of the software, still a lot of `ToDo`s and some more experimental features (see documentation); also exception handling could be improved

# Installation/Setup

It has currently only one external dependency, [num2words](https://pypi.org/project/num2words/). All dependencies are to be found in `requirements.txt` and included in `setup.py` as well, at the moment.

Installation is currently done via **local** package installation:

* go to the directory where you cloned this repo (via `git clone https://github.com/repodiac/german_transliterate`)
* type `pip install -e .`

It should install to your current Python environment as any other `pip` package (in case, create a virtual environment with `virtualenv` before).

# Documentation

Example usage:

```
from german_transliterate.german_transliterate import GermanTransliterate

text = 'Um 13:15h kaufte Hr. Meier 1.000 Luftballons für 250€.'
print('ORIGINAL:', text)
# use these setting for PHONEMIC ENCODINGS, leave all parameters empty otherwise
print('TRANSLITERATION:', GermanTransliterate(replace={';': ',', ':': ' '}, sep_abbreviation=' -- ').transliterate(text))
```

The parameters used for the config parameter `transliterate_ops` are as follows:
* ... to be completed

# Issues and Comments

Please open issues for bugs or feature requests. You can also reach out to me via github.
