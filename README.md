# ytchapters2json

ytchapters2json is a Python command-line tool that converts YouTube chapter timestamps to a `chapters.json` file in the `application/json+chapters` format for Podcasting 2.0.

<!-- jooray-links:start -->
### More from me

**Related projects**

- [video-slide-extractor](https://github.com/jooray/video-slide-extractor): extract slide keyframes from videos
- [video-summarizer](https://github.com/jooray/video-summarizer): summarize video transcripts with the Venice API
- [mindvalley-dl](https://github.com/jooray/mindvalley-dl): example of scraping media from the web

**Full project showcase:** [all my projects](https://juraj.bednar.io/showcase/).

I write about building things on [my blog](https://juraj.bednar.io/en/blog-en/). I also wrote a cypherpunk novel, [Tamers of Entropy](https://tamersofentropy.net/), and there is a [trailer](https://tamersofentropy.net/#trailer).
<!-- jooray-links:end -->

## Features

- Converts chapters from a text file or stdin.
- Supports specifying an image URL per chapter using `;` in the input file.
- Allows specifying a default image URL with `--image` for chapters without an image.
- Generates a `chapters.json` file compatible with Podcasting 2.0.

## Installation

Ensure you have Python 3 installed.

Clone the repository or download the `ytchapters2json` script.

```bash
git clone https://github.com/jooray/ytchapters2json.git
cd ytchapters2json
```

## Usage

```bash
./ytchapters2json [options] <input_file> <output_file>
```

### Positional Arguments

- `input_file`: Input file containing chapters in the format `hh:mm:ss Title` (use `-` for stdin).
- `output_file`: Output JSON file.

### Optional Arguments

- `--image`: Default image URL to apply to chapters without a specified image.

### Example

```bash
./ytchapters2json --image "https://example.com/default_image.jpg" chapters.txt chapters.json
```

### Help

```bash
./ytchapters2json --help
```

## Input Format

The input file should contain chapters in the following format:

```
hh:mm:ss Chapter Title [;Image URL]
```

- Use `;` to separate the chapter title and an optional image URL.

### Example Input

```
00:00:00 Introduction
00:05:30 Topic 1 ; https://example.com/image1.jpg
00:15:45 Topic 2
```

In this example:

- The first chapter has the title "Introduction" and no image URL.
- The second chapter has the title "Topic 1" and the image URL `https://example.com/image1.jpg`.
- The third chapter has the title "Topic 2" and no image URL.

## Output

The script generates a `chapters.json` file in the `application/json+chapters` format.

### Example Output

```json
{
  "version": "1.2.0",
  "chapters": [
    {
      "startTime": 0,
      "title": "Introduction",
      "image": "https://example.com/default_image.jpg"
    },
    {
      "startTime": 330,
      "title": "Topic 1",
      "image": "https://example.com/image1.jpg"
    },
    {
      "startTime": 945,
      "title": "Topic 2",
      "image": "https://example.com/default_image.jpg"
    }
  ]
}
```

In this example, the `--image` option was used with the value `https://example.com/default_image.jpg`.

## License

This project is licensed under the MIT License.
