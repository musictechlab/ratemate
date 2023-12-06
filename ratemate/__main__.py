import argparse
import logging

import coloredlogs

from ratemate import RateMate

logger = logging.getLogger("root")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")

    parser.add_argument("audio_file", help="Audio file path")

    args = parser.parse_args()

    if args.debug:
        coloredlogs.install(
            level="DEBUG",
            fmt="%(asctime)s %(name)s[%(process)d] %(levelname)s %(message)s",
        )
        logger.debug("LOG_LEVEL set to DEBUG")
    else:
        coloredlogs.install(
            level="INFO",
            fmt="%(asctime)s %(name)s[%(process)d] %(levelname)s %(message)s",
        )

    rm = RateMate()

    audio_rate = rm.rate_audio(args.audio_file)

    logger.info(f"Output: {audio_rate}")


if __name__ == "__main__":
    main()
