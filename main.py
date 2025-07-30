import fitz  # PyMuPDF
import argparse
import time
import logging

from pathlib import Path


def compress_pdf(input_path: Path, output_path, scale, orientation, dry_run):
    pass


def parse_args():
    parser = argparse.ArgumentParser(description="Tool to compress an image-based PDF with scaling and orientation fix")
    parser.add_argument("input_path", type=Path, help="Path to input PDF")
    parser.add_argument("output_path", type=Path, help="Path to output PDF (must be different from input_path)")
    parser.add_argument("--scale", type=float, default=0.5, help="Scale factor for images (default: 0.5)")
    parser.add_argument("--orientation", choices=["portrait", "landscape"], help="Force page orientation")

    args = parser.parse_args()

    # Validation checks
    if not args.input_path.exists():
        raise FileNotFoundError(f"Input file ({args.input_path}) does not exist")
    if args.output_path.exists():
        logging.warning(f"Output file ({args.output_path}) already exists and will be overwritten!")

        SECONDS_DELAY = 15
        logging.warning(f"You have {SECONDS_DELAY} seconds to abort with Ctrl+C...")
        try:
            time.sleep(SECONDS_DELAY)
        except KeyboardInterrupt:
            logging.info("\nOperation cancelled by user. No files were changed")
            exit(0)
        logging.warning(f"Operation proceeding. Output file ({args.output_path}) will be overwritten!")
    if args.input_path.resolve() == args.output_path.resolve():
        raise IOError(f"The input and output paths cannot resolve to the same path!")
    for fpath in [args.input_path, args.output_path]:
        if not fpath.suffix.lower() == ".pdf":
            raise ValueError(f"Supplied path: {fpath} must end with [.pdf, .PDF]")

    return args


if __name__ == "__main__":
    _args = parse_args()

    logging.basicConfig(level=logging.INFO)
    compress_pdf(**vars(_args))
