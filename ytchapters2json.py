#!/usr/bin/env python3

import sys
import argparse
import json
import re

def parse_timestamp(timestamp_str):
    """Convert hh:mm:ss to seconds"""
    parts = timestamp_str.strip().split(':')
    if len(parts) != 3:
        raise ValueError(f"Invalid timestamp format: {timestamp_str}")
    hours, minutes, seconds = parts
    total_seconds = int(hours) * 3600 + int(minutes) * 60 + int(seconds)
    return total_seconds

def main():
    if len(sys.argv) == 1:
        print("No arguments specified. Use --help for usage information.")
        sys.exit(1)

    parser = argparse.ArgumentParser(description='Convert YouTube chapters to chapters.json for Podcasting 2.0')
    parser.add_argument('input_file', help='Input file containing chapters (use "-" for stdin)')
    parser.add_argument('output_file', help='Output JSON file')
    parser.add_argument('--image', help='Default image URL to apply to chapters without specified image', default=None)
    args = parser.parse_args()

    # Read input
    if args.input_file == '-':
        input_lines = sys.stdin.readlines()
    else:
        with open(args.input_file, 'r', encoding='utf-8') as f:
            input_lines = f.readlines()

    chapters = []
    for line in input_lines:
        line = line.strip()
        if not line:
            continue
        # Adjust regex to capture optional image URL after ';'
        match = re.match(r'(\d{2}:\d{2}:\d{2})\s+(.*)', line)
        if not match:
            print(f"Skipping invalid line: {line}", file=sys.stderr)
            continue
        timestamp_str, rest = match.groups()
        # Now split rest into title and optional image
        if ';' in rest:
            title_part, image_part = rest.split(';', 1)
            title = title_part.strip()
            image_url = image_part.strip()
        else:
            title = rest.strip()
            image_url = None
        try:
            start_time = parse_timestamp(timestamp_str)
        except ValueError as e:
            print(f"Skipping line due to error: {line}", file=sys.stderr)
            continue
        chapter = {
            "startTime": start_time,
            "title": title
        }
        if image_url:
            chapter["image"] = image_url
        elif args.image:
            chapter["image"] = args.image
        chapters.append(chapter)

    output_data = {
        "version": "1.2.0",
        "chapters": chapters
    }

    with open(args.output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    main()
