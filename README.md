
# SKUGen

An easy-to-use S.K.U. (Stock Keeping Unit) codes generator, made in Python.

This is a CLI script that allows you to config your own product details and associated values.

## Setup a product
Inside the file `product_info.json` you can set your product data following the given example's structure

## How to use it
Just execute the script by `python3 generator.py` from the file's folder. Remember to use python3 and not older versions for an optimal experience. No additional libraries are needed.

## Files hierarchy
#### `product_info.json`
 - Contains all the product info
 #### `listings.txt`
 - Contains the list of all the generated products and how many times they've been added
 #### `database.txt`
 - Contains the actual active products with their unique code

## Contributions & Updates
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## To do
In the future i will add the ability to remove deprecated SKU codes from the database 
(at the moment you're already perfectly able to remove them, you just have to do it manually from `database.txt` which is "ok" but not optimal)