# Ratemate

Ratemate is an automated tool designed for the analysis of audio tracks. It proficiently extracts lyrics from the provided audio and subsequently conducts evaluations based on the PEGI (Pan European Game Information) scale.

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