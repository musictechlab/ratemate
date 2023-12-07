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


<div align="center">
  Bravelab. Digital Commerce Solution For The Music Industry<br>
  <a href="https://www.bravelab.io/">Website</a>
  <span> | </span>
  <a href="https://linkedin.com/company/bravelab.io">LinkdedIn</a>
</div>
