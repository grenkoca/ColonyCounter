# ColonyCounter

A silly lil program that lets a user input an image of a petri dish on a dark background (like a lab table) and it returns a count of how many cell colonies are in the dish. Honestly I wrote this in 15 minutes because I didn't want to count colonies in my biochem lab: this really isn't intended for proper usage.

## Usage

```./count_colonies ./sample_data/IMG_3722.jpg -show_results True```

Additionally you can run this sequentially on as many images as you want. Try running two images at once:

```./count_colonies ./sample_data/IMG_3722.jpg ./sample_data/IMG_3732.jpg```

## Installation

```
pip install -r requirements.txt
chmod +x ./count_colonies
```

Or use conda if you're so inclined.
