from setuptools import setup

setup(
   name='german_transliterate',
   version='0.1.2',
   author='repodiac',
   author_email='spamornot@gmx.net',
   packages=['german_transliterate'],
   url='http://github.com/repodiac/german_transliterate',
   license='CC-BY-4.0 License',
   description='german_transliterate can clean and transliterate (i.e. normalize) German text including abbreviations, numbers, timestamps etc.',
   long_description=open('README.md').read(),
   install_requires=[
       "num2words",
   ],
)
