# answer_college_supplemental

# For my Caltech Supplemental Nine Essay

[![PyPI - Version](https://img.shields.io/pypi/v/answer-college-supplemental.svg)](https://pypi.org/project/answer-college-supplemental)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/answer-college-supplemental.svg)](https://pypi.org/project/answer-college-supplemental)

---

## Table of Contents

- [Internals](#internals")
- [Installation](#installation)
- [License](#license)

## Internals

- First, I created a Flask app as the backend and hosted it on Vercel. Since I use Google Gemini to create the essay response, I need to keep the Google Gemini API Key safe and secure, which isn't possible if I were to include it in the Python package.
- Second, I created the CLI tool using the built-in Argparse module to create the flag arguments. Then, I used requests to send a response to my Flask app, which calls Google Gemini. I send the Google Gemini response back to the CLI tool, which saves it to the output file.

## Installation

```console
pip install answer-college-supplemental
```

## License

`answer-college-supplemental` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
