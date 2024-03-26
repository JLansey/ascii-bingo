# ascii-bingo

A Python script designed to create visually appealing, printable ASCII bingo boards. The script generates boards using predefined sets of words, ensuring unique and balanced content across different themes. While currently themed around Argentine culture, it's designed to be adaptable for a wide range of topics.

## Features

- Generates unique bingo boards with predefined word sets, ensuring a diverse and balanced selection.
- Supports custom themes through external Python modules (for example, `argentina.py` for an Argentine-themed bingo).
- Provides an ASCII art representation for each board, making them ready for printing or digital sharing.
- Allows customization of the central square word to tailor the experience to different events or themes.

## How It Works

The script divides a sorted list of words into sections with similar difficulty, selecting randomly to ensure even difficulty while respecting constraints between words to avoid thematic overlaps. It places a special, optional word in the center of each board, suitable for thematic emphasis or as a free space.

## Installation

1. Clone this repository.
2. Ensure Python 3.6 or higher is installed on your system.
3. (Optional) Modify `argentina.py` or create a new theme file to customize the word sets and constraints according to your needs.

## Usage

To generate bingo boards:

```python
from bingo import print_bingo_sheets

# Generate and print 10 bingo sheets
print_bingo_sheets(10, 'output.txt')
```

For custom themes, replace `argentina` with your module containing `sorted_list`, `constraints`, `center_word`, and `ascii_art_header`.

## Customization

- **Word Sets**: Modify `sorted_list` in the theme file to change the words used on the bingo boards.
- **Constraints**: Adjust `constraints` to ensure certain words are never chosen together.
- **Center Word**: Set `center_word` to define a fixed word for the center of each board, or `None` for a random selection.
- **ASCII Art**: Replace `ascii_art_header` in your theme file to customize the header of each board.

## Contributing

We welcome contributions, especially new themes to enhance the diversity and fun of the bingo boards!

## Example

Below is an example of a bingo board generated by the script:

![Example ASCII Bingo Board](https://github.com/JLansey/ascii-bingo/assets/4146681/5144747b-53db-4dc4-a1e4-f337a1ad7b05)

*An example of a bingo board generated by ascii-bingo, displayed on a tablet.*

## License

This project is licensed under the MIT License - see the LICENSE file for details.
