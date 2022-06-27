from PIL import Image
import shutil
import os
import json
import random

# dir_list = sorted(os.listdir(sticker_path))
#

# print("Files and directories in '", sticker_path, "' :")
#
# # prints all files
# print(primary_path)


def start_generation():

    primary_path = "images/primary/"
    secondary_path = "images/secondary/"

    sticker_path = "images/stickers/"
    trait_path = "images/traits/"

    meta = []
    counter = 0
    x = 1

    while x <= 20:

        primary = random.choices(os.listdir(primary_path), weights=(10, 20, 30, 40, 50), k=5)
        a = str(meta).count(primary)
        primary_value = primary.split('#')

        if str(a) == primary_value[0]:
            shutil.move(primary_path + primary, "used/" + primary_path + primary)
            primary = random.choice(os.listdir(primary_path))

        secondary = random.choice(os.listdir(secondary_path))
        a = str(meta).count(secondary)
        secondary_value = secondary.split('#')
        if str(a) == secondary_value[0]:
            shutil.move(secondary_path + secondary, "used/" + secondary_path + secondary)
            secondary = random.choice(os.listdir(secondary_path))

        sticker = random.choice(os.listdir(sticker_path))
        b = str(meta).count(sticker)
        sticker_value = sticker.split('#')
        if str(b) == sticker_value[0]:
            shutil.move(sticker_path + sticker, "used/" + sticker_path + sticker)
            sticker = random.choice(os.listdir(sticker_path))

        trait = random.choice(os.listdir(trait_path))
        c = str(meta).count(trait)
        trait_value = trait.split('#')
        if str(c) == trait_value[0]:
            shutil.move(trait_path + trait, "used/" + trait_path + trait)
            trait = random.choice(os.listdir(trait_path))

        temp_item = {
            'attributes': [
                {
                    'trait_type': 'Primary color',
                    'value': primary_value[1]
                },
                {
                    'trait_type': 'Secondary color',
                    'value': secondary_value[1]
                },
                {
                    'trait_type': 'Sticker',
                    'value': sticker_value[1]
                },
                {
                    'trait_type': 'trait1',
                    'value': trait_value[1]
                }
            ]
        }

        output_meta = {
            'name': 'AR #' + str(x),
            'description': 'AR LFG',
            'image': 'https://storage.googleapis.com/aperides/rides/images/' + str(x) + '.png',
            'attributes': [
                {
                    'trait_type': 'Primary Monkey color',
                    'value': primary_value[1]
                },
                {
                    'trait_type': 'Secondary color',
                    'value': secondary_value[1]
                },
                {
                    'trait_type': 'Sticker',
                    'value': sticker_value[1]
                },
                {
                    'trait_type': 'trait1',
                    'value': trait_value[1]
                }
            ]
        }

        if temp_item in meta:
            print("Duplicate LFG again")
        else:
            meta.append(temp_item)

            with open("final/" + str(x) + '.json', 'w') as f:
                json.dump(output_meta, f, sort_keys=True, indent=4, ensure_ascii=False)

            # print(meta)

            img1 = Image.open(primary_path + primary)
            img2 = Image.open(secondary_path + secondary)
            img3 = Image.open("images/traits/" + trait)
            img4 = Image.open("images/stickers/" + sticker)

            img1.paste(img2, (0, 0), mask=img2)
            img1.paste(img3, (0, 0), mask=img3)
            img1.paste(img4, (0, 0), mask=img4)

            img1.save('final/' + str(x) + '.png')

            # Image Back ######
            img1 = Image.open("images/back/primary/" + primary)
            img2 = Image.open(secondary_path + secondary)
            img3 = Image.open("images/traits/" + trait)
            img4 = Image.open("images/stickers/" + sticker)

            img1.paste(img2, (0, 0), mask=img2)
            img1.paste(img3, (0, 0), mask=img3)
            img1.paste(img4, (0, 0), mask=img4)

            img1.save('final/' + str(x+30) + '_main.png')
            # Image Back ######

            # Image No AOR ######
            img1 = Image.open("images/back/primary/" + primary)
            img2 = Image.open(secondary_path + secondary)
            img3 = Image.open("images/traits/" + trait)
            img4 = Image.open("images/stickers/" + sticker)

            img1.paste(img2, (0, 0), mask=img2)
            img1.paste(img3, (0, 0), mask=img3)
            img1.paste(img4, (0, 0), mask=img4)

            img1.save('final/' + str(x) + '_main.png')
            # Image No AOR ######

            counter += 1
            x += 1


start_generation()
