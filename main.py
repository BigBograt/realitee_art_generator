from PIL import Image
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

    # Define image paths for each trait. Folder names do not represent meta values. filenames do.
    aura_path = "images/aura/"
    primary_path = "images/primary/"
    secondary_path = "images/secondary/"
    wheels_path = "images/wheels/"
    sticker_path = "images/stickers/"
    artwork_path = "images/artwork/"
    lights_path = "images/lights/"
    trait1_path = "images/trait1/"
    trait2_path = "images/trait2/"
    trait3_path = "images/trait3/"

    #Define ride type as it will be shown in the metadata
    ride_type = "Camper"

    meta = []
    counter = 0
    x = 1

    while x <= 20:
        aura = random.choice(sorted(os.listdir(aura_path)))
        primary = random.choices(sorted(os.listdir(primary_path)), weights=(30, 3, 2, 15, 3, 2, 8, 20, 10, 5, 2, 4))[0]
        secondary = random.choice(sorted(os.listdir(secondary_path)))
        sticker = random.choices(sorted(os.listdir(sticker_path)), weights=(5, 25, 25, 20, 20, 5))[0]
        wheels = random.choices(sorted(os.listdir(wheels_path)), weights=(8, 90, 2))[0]
        artwork = random.choice(sorted(os.listdir(artwork_path)))
        lights = random.choices(sorted(os.listdir(lights_path)), weights=(80, 20))[0]
        trait1 = random.choices(sorted(os.listdir(trait1_path)), weights=(5, 5, 10, 50, 10, 20))[0]
        trait2 = random.choice(sorted(os.listdir(trait2_path)))
        trait3 = random.choice(sorted(os.listdir(trait3_path)))

        temp_item = {
            'attributes': [
                {
                    'trait_type': 'Ride Type',
                    'value': ride_type
                },
                {
                    'trait_type': 'Aura',
                    'value': aura
                },
                {
                    'trait_type': 'Primary color',
                    'value': primary
                },
                {
                    'trait_type': 'Secondary color',
                    'value': secondary
                },
                {
                    'trait_type': 'Sticker',
                    'value': sticker
                },
                {
                    'trait_type': 'Wheels',
                    'value': wheels
                },
                {
                    'trait_type': 'Artwork',
                    'value': artwork
                },
                {
                    'trait_type': 'Lights',
                    'value': lights
                },
                {
                    'trait_type': 'Feature One',
                    'value': trait1
                },
                {
                    'trait_type': 'Feature two',
                    'value': trait2
                },
                {
                    'trait_type': 'Feature Three',
                    'value': trait3
                }
            ]
        }

        output_meta = {
            'name': 'AR #' + str(x),
            'description': 'AR LFG',
            'image': 'https://storage.googleapis.com/aperides/rides/images/' + str(x) + '.png',
            'attributes': [
                {
                    'trait_type': 'Ride Type',
                    'value': ride_type
                },
                {
                    'trait_type': 'Aura',
                    'value': aura
                },
                {
                    'trait_type': 'Primary Monkey color',
                    'value': primary
                },
                {
                    'trait_type': 'Secondary color',
                    'value': secondary
                },
                {
                    'trait_type': 'Sticker',
                    'value': sticker
                },
                {
                    'trait_type': 'Wheels',
                    'value': wheels
                },
                {
                    'trait_type': 'Artwork',
                    'value': artwork
                },
                {
                    'trait_type': 'Lights',
                    'value': lights
                },
                {
                    'trait_type': 'Feature One',
                    'value': trait1
                },
                {
                    'trait_type': 'Feature two',
                    'value': trait2
                },
                {
                    'trait_type': 'Feature Three',
                    'value': trait3
                }
            ]
        }

        if temp_item in meta:
            print("Duplicate LFG again")
        else:
            meta.append(temp_item)

            with open("final/" + str(x) + '.json', 'w') as f:
                json.dump(output_meta, f, sort_keys=True, indent=4, ensure_ascii=False)

            # DO NOT AMEND BASE IMAGE this is a blank image
            base_image = Image.open("images/base.png")

            aura_img = Image.open(aura_path + aura)
            primary_img = Image.open(primary_path + primary)
            secondary_img = Image.open(secondary_path + secondary)
            sticker_img = Image.open(sticker_path + sticker)
            wheels_img = Image.open(wheels_path + wheels)
            artwork_img = Image.open(artwork_path + artwork)
            lights_img = Image.open(lights_path + lights)
            trait1_img = Image.open(trait1_path + trait1)
            trait2_img = Image.open(trait2_path + trait2)
            trait3_img = Image.open(trait3_path + trait3)

            base_image.paste(aura_img, (0, 0), mask=aura_img)
            base_image.paste(primary_img, (0, 0), mask=primary_img)
            base_image.paste(secondary_img, (0, 0), mask=secondary_img)
            base_image.paste(sticker_img, (0, 0), mask=sticker_img)
            base_image.paste(wheels_img, (0, 0), mask=wheels_img)
            base_image.paste(artwork_img, (0, 0), mask=artwork_img)
            base_image.paste(lights_img, (0, 0), mask=lights_img)
            base_image.paste(trait1_img, (0, 0), mask=trait1_img)
            base_image.paste(trait2_img, (0, 0), mask=trait2_img)
            base_image.paste(trait3_img, (0, 0), mask=trait3_img)

            base_image.save('final/' + str(x) + '.png')

            # Static Image used to show wihout APE ######
            # This section OPENS all images ready to be layered
            base_image = Image.open("images/base.png")

            aura_img = Image.open(aura_path + aura)
            primary_img = Image.open(primary_path + primary)
            secondary_img = Image.open(secondary_path + secondary)
            sticker_img = Image.open(sticker_path + sticker)
            wheels_img = Image.open(wheels_path + wheels)
            artwork_img = Image.open(artwork_path + artwork)
            lights_img = Image.open(lights_path + lights)
            trait1_img = Image.open(trait1_path + trait1)
            trait2_img = Image.open(trait2_path + trait2)
            trait3_img = Image.open(trait3_path + trait3)

            # ---- This image on top of full ride to fill the gap
            back_piece = Image.open("images/backpiece.png")

            # This section LAYERS AND SAVES all imagery.
            base_image.paste(aura_img, (0, 0), mask=aura_img)
            base_image.paste(primary_img, (0, 0), mask=primary_img)
            base_image.paste(secondary_img, (0, 0), mask=secondary_img)
            base_image.paste(sticker_img, (0, 0), mask=sticker_img)
            base_image.paste(wheels_img, (0, 0), mask=wheels_img)
            base_image.paste(artwork_img, (0, 0), mask=artwork_img)
            base_image.paste(lights_img, (0, 0), mask=lights_img)
            base_image.paste(trait1_img, (0, 0), mask=trait1_img)
            base_image.paste(trait2_img, (0, 0), mask=trait2_img)
            base_image.paste(trait3_img, (0, 0), mask=trait3_img)

            # --- This image on top of full ride to fill the gap
            base_image.paste(back_piece, (0, 0), mask=back_piece)

            base_image.save('final/' + str(x) + '_main.png')

            # Do not alter below
            counter += 1
            x += 1


start_generation()