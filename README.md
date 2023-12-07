# Ratemate

Ratemate is an automated proof of concept tool designed for the analysis of audio tracks. 
It proficiently extracts lyrics from the provided audio and subsequently conducts evaluations based on the PEGI (Pan European Game Information) scale.

## Prerequisites

1. You have to create a new secret API key here: https://platform.openai.com/api-keys
2. You need to have minumum $5 USD credits to use GPT API: https://platform.openai.com/account/billing/overview 

## Installation

To install Ratemate, use the following commands:

```bash
poetry install
```

After installation, make sure to provide your OpenAPI API key in the `.env` file.

## Running

Activate the virtual environment:

```bash
poetry shell
```

Run Ratemate on a specific audio track (replace `someaudio.mp3` with the actual filename):

```bash
python ratemate someaudio.mp3
```

For debugging purposes, you can enable debugging mode:

```bash
python ratemate someaudio.mp3 --debug
```

## Example output
<div align="center" width="100px">
 <picture>
   <img alt="Ratemate" src="https://github.com/bravelab/ratemate/blob/main/ratemate-example.png">
 </picture>
</div>


## License

MIT License

Copyright (c) 2023 Brave Sp. z o.

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
SOFTWARE.

<div align="center">
  Bravelab. Digital Commerce Solution For The Music Industry<br>
  <a href="https://www.bravelab.io/">Website</a>
  <span> | </span>
  <a href="https://linkedin.com/company/bravelab.io">LinkdedIn</a><span> | </span>
  <a href="mailto:office@bravelab.io">Let's talk</a><br>
  Crafted by https://www.bravelab.io
</div>


