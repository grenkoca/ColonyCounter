# ColonyCounter

A silly lil program that lets a user input an image of a petri dish on a dark background (like a lab table) and it returns a count of how many cell colonies are in the dish. Honestly I wrote this in 15 minutes because I didn't want to count colonies in my biochem lab: this really isn't intended for proper usage.

## Usage

```./count_colonies ./sample_data/IMG_3722.jpg -show_results True```

Additionally you can run this sequentially on as many images as you want. Try running two images at once:

```./count_colonies ./sample_data/IMG_3722.jpg ./sample_data/IMG_3732.jpg```

Finally, you can also opt to save the intermediate images used in counting colonies. Namely, the binary plate detection mask and the annotated colonies.

```./count_colonies ./sample_data/IMG_3722.jpg ./sample_data/IMG_3732.jpg --save_imgs ./testrun```

## Installation

```
pip install -r requirements.txt
chmod +x ./count_colonies
```

Or use conda if you're so inclined.

## Example output

```
❯ ./count_colonies sample_data/IMG_3722.jpg sample_data/IMG_3732.jpg --save_imgs ./testrun
sample_data/IMG_3722.jpg : 3284 colonies 
sample_data/IMG_3732.jpg : 2326 colonies 
```

# Future improvements

None of these are particularly hard, but I just need to get to them. If you want to contribute, please do!

- [ ] Output additional CSV file to summarize 
- [ ] Improve colony detection (size/shape/intensity variability, etc.)
- [ ] Implement pen removal
