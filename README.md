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

* `0.1.1` - added command-line interface for default usage (no phoneme encoding and experimental stuff left out)
* `release 0.1` - initial release of the software, still a lot of `ToDo`s and some more experimental features (see documentation); also exception handling could be improved

# Installation/Setup

It has currently only one external dependency, [num2words](https://pypi.org/project/num2words/). All dependencies are to be found in `requirements.txt` and included in `setup.py` as well, at the moment.

Installation is eays using `pip` and built-in `git` package installation based on `setup.py`:

* `pip install git+https://github.com/repodiac/german_transliterate`

Setup:

- It should install and behave (`import german_transliterate.core`) to your current Python environment as any other `pip` package (in case, create a virtual environment with `virtualenv` or `conda` before).

# Documentation

## Example Usage

In Python code or as library:

```
from german_transliterate.core import GermanTransliterate

text = 'Um 13:15h kaufte Hr. Meier (Mitarbeiter der Firma ABC) 1.000 Luftballons für 250€.'
print('ORIGINAL:', text, '\n')

ops = {'acronym_phoneme', 'accent_peculiarity', 'amount_money', 'date', 'timestamp',
        'weekday', 'month', 'time_of_day', 'ordinal', 'special', 'math_symbol', 'spoken_symbol'}

# use these setting for PHONEMIC ENCODINGS as input (e.g. with TTS)
print('TRANSLITERATION with phonemic encodings:',
      GermanTransliterate(replace={';': ',', ':': ' '}, sep_abbreviation=' -- ').transliterate(text), '\n')

# use none or your own for other purposes than phonemic encoding and do not use 'spoken_symbol' or 'acronym_phoneme'
print('TRANSLITERATION (default):',
      GermanTransliterate(transliterate_ops=list(ops-{'spoken_symbol', 'acronym_phoneme'})).transliterate(text), '\n')
```

**NEW** From command-line (in the shell):

```
python core.py '1, 2, 3 - alles ist dabei'
```

## Input Parameters

There is currently only *one* method to be used: `transliterate('Das ist der Text.')`

It has the following input parameters:

* `transliterate_ops` list of keywords, see below for details
* `replace` dict of "original: replacement" string tuples to be used as additional plain and simple "on-the-fly" replacements with the text, e.g replace={'-' : ' '} replaces all dashes with whitespace; leave `empty` for **normal use** and use `{';': ',', ':': ' '}` with **phonemic encodings**
* `sep_abbreviation` a special separator used for transliteration of abbreviations; this is mostly only useful with phonemic encoding of a text as a next step in a TTS pipeline; leave `empty` for **normal use** and use `' -- '` with **phonemic encodings**
* `make_lowercase` if True, text is made lowercase (leave `empty` by default)
**NOTE**: most of the transliterate operations do **only** work with `make_lowercase=True` - this is due to the various dictionaries operating with lowercase only. Please use `make_lowercase=False` only when `transliterate_ops` aren't overly used, otherwise most of them do not work!

The parameters used for the config parameter `transliterate_ops` are as follows:

* `acronym_phoneme` transliterates abbreviations like `ABC` into a phonemic version `ah beh zee`
* `accent_peculiarity` removes peculiar Unicode encodings and maps them to compatible ASCII-like versions (cleaning op)
* `amount_money` transliterates currency and money symbols like $, €, EUR etc.
* `date` transliterates dates, e.g. 12.10.2019
* `timestamp` transliterates timestamps, e.g. 13h:15m:45s
* `weekday` (*experimental*), transliterates abbreviations for weekdays, for instance `Mo` -- **currently this is rather error-prone (many false-positives)**
* `month` (*experimental*), transliterates abbreviations for months, e.g. `Jan` or `Dez` -- **currently this is rather error-prone (many false-positives)**
* `time_of_day` transliterates time of day, e.g. 13:15h
* `ordinal` transliterates ordinal numbers, e.g. `2.` into `zweite` (tries to find a tradeoff for correct case suffix, i.e. `zweiten` or `zweitem`)
* `special` transliterates edge cases and special terms, e.g. `8 / 10` into `acht von zehn`
* `math_symbol` (*experimental*), transliterates a small selection of math symbols, e.g. `plus`, `minus` etc. (also here applies: can have a lot of false-positives, so use with care)
* `spoken_symbol` allows to transliterate brackets or citation marks into spoken language, e.g. '( text )' into `-- in klammern -- text --` (if `sep_abbreviation` is set to ' -- '), mainly useful for TTS tasks

## Performance

The current state is mainly based on using manual mappings and regular expressions for substitution and expansion of strings (words or terms). Therefore, current performance should be good enough to be used with online inference or "realtime" usage in a text processing pipeline. As further modules or ops are added over time, there might be also rather slow methods doing heavy computations and thus suited mainly for training or offline processing.

# Issues and Comments

Please open issues on github for bugs or feature requests. You can also reach out to me via email.
