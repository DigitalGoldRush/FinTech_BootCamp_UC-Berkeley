# Loan Qualifier App 

This user-friendly app allows the user to determine what loans they may qualify for based on their current financial status. The information required to run this program are as follows:
 1. Credit score
 2. Monthly debt
 3. Monthly income
 4. Loan amount requested
 5. Home value 

Qualifying loans can be saved to a CSV file for future reference if prompted.
 
![<img src="http://url/image.png" style=" width:10px ; height:10px "  >](https://m.foolcdn.com/media/affiliates/images/Loan_paperwork_money.width-1200.jpg)

---

## Technology Used

[![Python 3.7.13](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/downloads/release/python-3713/)
[![Python](https://img.shields.io/badge/Python-3.7.13-blue)](https://www.python.org/downloads/release/python-3713/)

[<img alt="Visual Studio Code" src="https://img.shields.io/badge/VisualStudioCode-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white"/> ](https://code.visualstudio.com/)


[<img alt="DjangoREST" src="https://img.shields.io/badge/PyPI-Questionary-ff1709?style=for-the-badge&logoColor=white&color=ff1709&labelColor=gray"/>](https://questionary.readthedocs.io/en/stable/index.html)

[<img alt="DjangoREST" src="https://img.shields.io/badge/PyPI-FIRE-ff1709?style=for-the-badge&logoColor=white&color=ff1709&labelColor=gray"/>](https://pypi.org/project/fire/)

[<img alt="DjangoREST" src="https://img.shields.io/badge/PyPI-TABULATE-ff1709?style=for-the-badge&logoColor=white&color=ff1709&labelColor=gray"/>](https://pypi.org/project/tabulate/)

[<img alt="GitHub" src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white"/>](https://github.com/DigitalGoldRush?tab=repositories)

---

## Installation Guide

### To install questionary, simply run this command in your terminal of choice:
```python
$ pip install questionary
```
### To install fire, simply run this command in your terminal of choice:
```python
$ pip install fire
```
### To install tabulate, simply run this command in your terminal of choice:
```python
$ pip install tabulate
```

---

## [Questionary Usage](https://questionary.readthedocs.io/en/stable/pages/types.html)

### Use questionary to ask a single question
```python
import questionary
question = questionary.text("What's your first name?")
```
### Need to prompt the user to answer it:
```python
answer = question.ask()
```
### You can concatonate creating and asking the question in a single line for simplicity:
```python
import questionary
answer = questionary.text("What's your first name?").ask()
```

## [Fire Usage](https://github.com/google/python-fire/commit/9f9630ac871138c04c8654eb46d66ca0a2f70b7c) 
You can call `Fire` on any Python object:<br>
functions, classes, modules, objects, dictionaries, lists, tuples, etc.

Here is a simple example from the fire-github.

```python
import fire
class Calculator(object):
  """A simple calculator class."""
  def double(self, number):
    return 2 * number
if __name__ == '__main__':
  fire.Fire(Calculator)
```

## [Tabulate Usage](https://pypi.org/project/tabulate/)

### Use tabulate to print small tables with just one function call. The formating is guided by the data itself.
```python
>>> from tabulate import tabulate

>>> table = [["Sun",696000,1989100000],["Earth",6371,5973.6],
...          ["Moon",1737,73.5],["Mars",3390,641.85]]
>>> print(tabulate(table))
-----  ------  -------------
Sun    696000     1.9891e+09
Earth    6371  5973.6
Moon     1737    73.5
Mars     3390   641.85
-----  ------  -------------
```
### Optional argument named `headers` will provide column headers:<br>
```python
>>> print(tabulate(table, headers=["Planet","R (km)", "mass (x 10^29 kg)"]))
Planet      R (km)    mass (x 10^29 kg)
--------  --------  -------------------
Sun         696000           1.9891e+09
Earth         6371        5973.6
Moon          1737          73.5
Mars          3390         641.85
```

---
## Contributors

[![Python](https://img.shields.io/badge/Michael_Dionne-LinkedIn-blue)](https://www.linkedin.com/in/michael-dionne-b2a1b61b/)

---

## License

Copyright (c) 2022 Michael R. Dionne

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE
