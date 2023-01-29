import sys

def printTitle():
    title = '''
     _____ __ ____  __   ______         
    / ___// //_/ / / /  / ____/__  ____ 
    \__ \/ ,< / / / /  / / __/ _ \/ __ \\
   ___/ / /| / /_/ /  / /_/ /  __/ / / /
  /____/_/ |_\____/   \____/\___/_/ /_/ 
                                        
    '''
    print(title)
    return

def encodeValue(dictionary, value):
    return dictionary[value] + "-"

def storeListing(sku_code):
    with open("listings.txt", "a+") as f:
        f.write(sku_code + '\n')
        f.close()

def saveListingInDB(sku_code):
    with open("database.txt", "a+") as f:
        f.write(sku_code + '\n')
        f.close()

def addListingID(sku_code):
    all_listings = []
    with open("listings.txt", "r+") as f:
        all_listings = f.readlines()
        f.close()
    return all_listings.count(sku_code + '\n') - 1

def encodeListing(listing_data, input_data):
    sku_code = ""
    if (len(listing_data) == len(input_data)):
        for i in range(len(listing_data)):
            sku_code += encodeValue(listing_data[i], input_data[i])
    else:
        print("\n[X] Error: inconsistent data.")

    storeListing(sku_code)
    sku_code += str(addListingID(sku_code))
    return sku_code

def launchMenu(listing_data):
    printTitle()
    input_data = []
    for i in range(len(listing_data)):
        value_label = listing_data[i]["Label"]
        print("\nListing's " + value_label + ":\n")
        for j in range(len(listing_data)):
            print(str(j+1) + ") " + list(listing_data[i].keys())[j+1])
        opt = input("\nChoose an option [1-" + str(j+1) + "]:\n > ")
        try:
            opt = int(opt)
        except:
            opt = j+2
        if (opt <= (j+1) and opt > 0):
            input_data.append(list(listing_data[i].keys())[opt])
        else:
            print("[X] Error: Not a valid option")
            key_pressed = input("[i] Press Q to quit or the ENTER key to retry...\n")
            if (key_pressed == 'q' or key_pressed == 'Q'):
                sys.exit()
            else:
                launchMenu(listing_data)

    sku_code = encodeListing(listing_data, input_data)
    saveListingInDB(sku_code)
    print('\n' + str(input_data) + " --> " + sku_code)
    return

product = {
            "Label":"product",
            "Painting":"P",
            "Custom Painting":"CP",
            "Photo":"PH"}
material = {
            "Label":"material",
            "Canvas":"C",
            "Framed Print":"FP",
            "Poster":"P"}
size = {
            "Label":"size",
            "Small":"S",
            "Medium":"M",
            "Large":"L"
}


listing_data = [product, material, size]
launchMenu(listing_data)