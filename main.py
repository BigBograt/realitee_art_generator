from PIL import Image
import os
import json
import random


def start_generation():

    aura_path = "images/aura/"
    primary_path = "images/primary/"
    secondary_path = "images/secondary/"
    wheels_path = "images/wheels/"
    artwork_path = "images/artwork/"
    lights_path = "images/lights/"
    trait1_path = "images/trait1/"
    trait2_path = "images/trait2/"
    trait3_path = "images/trait3/"

    ride_type = "Camper"

    meta = []
    counter = 0
    x = 1

    while x <= 10:
        aura = random.choices(sorted(os.listdir(aura_path)), weights=(1, 500))[0]
        primary = random.choices(sorted(os.listdir(primary_path)), weights=(7, 5, 6, 6, 1, 4, 5, 2, 1, 1, 1, 1, 6, 7, 2, 1, 6, 6, 1, 7, 7, 3, 1, 1, 7, 3))[0]
        secondary = random.choice(sorted(os.listdir(secondary_path)))
        wheels = random.choices(sorted(os.listdir(wheels_path)), weights=(8, 90, 2))[0]
        artwork = random.choice(sorted(os.listdir(artwork_path)))
        lights = random.choices(sorted(os.listdir(lights_path)), weights=(80, 20))[0]
        trait1 = random.choices(sorted(os.listdir(trait1_path)), weights=(6, 4, 2, 80, 6, 2))[0]
        trait2 = random.choices(sorted(os.listdir(trait2_path)), weights=(1, 1, 1, 1, 96))[0]
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
                    'value': ride_type.split('.png')[0]
                },
                {
                    'trait_type': 'Primary color',
                    'value': primary.split('.png')[0]
                },
                {
                    'trait_type': 'Wheels',
                    'value': wheels.split('.png')[0]
                },
                {
                    'trait_type': 'Lights',
                    'value': lights.split('.png')[0]
                }
            ]
        }

        if aura.split('.png')[0].upper() != "NONE":
            output_meta['attributes'].append({
                    'trait_type': 'Aura',
                    'value': aura.split('.png')[0]
                })

        if artwork.split('.png')[0].upper() != "NONE":
            output_meta['attributes'].append({
                    'trait_type': 'Artwork',
                    'value': artwork.split('.png')[0]
                })

        if secondary.split('.png')[0].upper() != "NONE":
            output_meta['attributes'].append({
                    'trait_type': 'Secondary color',
                    'value': secondary.split('.png')[0]
                })

        if trait1.split('.png')[0].upper() != "NONE":
            output_meta['attributes'].append({
                    'trait_type': 'Feature One',
                    'value': trait1.split('.png')[0]
                })

        if trait2.split('.png')[0].upper() != "NONE":
            output_meta['attributes'].append({
                    'trait_type': 'Feature One',
                    'value': trait2.split('.png')[0]
                })

        if trait3.split('.png')[0].upper() != "NONE":
            output_meta['attributes'].append({
                    'trait_type': 'Feature One',
                    'value': trait3.split('.png')[0]
                })

        if temp_item in meta:
            print("Duplicate LFG again")
        else:
            meta.append(temp_item)

            with open("final/" + str(x) + '.json', 'w') as f:
                json.dump(output_meta, f, sort_keys=True, indent=4, ensure_ascii=False)

            # DO NOT AMEND BASE IMAGE
            base_image = Image.open("images/base.png")

            aura_img = Image.open(aura_path + aura)
            primary_img = Image.open(primary_path + primary)
            secondary_img = Image.open(secondary_path + secondary)
            wheels_img = Image.open(wheels_path + wheels)
            artwork_img = Image.open(artwork_path + artwork)
            lights_img = Image.open(lights_path + lights)
            trait1_img = Image.open(trait1_path + trait1)
            trait2_img = Image.open(trait2_path + trait2)
            trait3_img = Image.open(trait3_path + trait3)

            base_image.paste(aura_img, (0, 0), mask=aura_img)
            base_image.paste(primary_img, (0, 0), mask=primary_img)
            base_image.paste(secondary_img, (0, 0), mask=secondary_img)
            base_image.paste(wheels_img, (0, 0), mask=wheels_img)
            base_image.paste(artwork_img, (0, 0), mask=artwork_img)
            base_image.paste(lights_img, (0, 0), mask=lights_img)
            base_image.paste(trait1_img, (0, 0), mask=trait1_img)
            base_image.paste(trait2_img, (0, 0), mask=trait2_img)
            base_image.paste(trait3_img, (0, 0), mask=trait3_img)

            base_image.save('final/' + str(x) + '.png')

            # Do not alter below
            print(x)
            counter += 1
            x += 1

    print('Primary: \n')
    print('Aquamarine: ' + str(str(meta).count('Aquamarine')))
    print('Army Green: ' + str(str(meta).count('Army Green')))
    print('Black: ' + str(str(meta).count('Black')))
    print('Blue: ' + str(str(meta).count('Blue')))
    print('Camo: ' + str(str(meta).count('Camo')))
    print('Cheetah: ' + str(str(meta).count('Cheetah')))
    print('Cream: ' + str(str(meta).count('Cream')))
    print('DMT: ' + str(str(meta).count('DMT')))
    print('Dots: ' + str(str(meta).count('Dots')))
    print('Galaxy: ' + str(str(meta).count('Galaxy')))
    print('Giraffe: ' + str(str(meta).count('Giraffe')))
    print('Gold: ' + str(str(meta).count('Gold')))
    print('Gray: ' + str(str(meta).count('Gray')))
    print('Green: ' + str(str(meta).count('Green')))
    print('Leather: ' + str(str(meta).count('Leather')))
    print('Noise: ' + str(str(meta).count('Noise')))
    print('Orange: ' + str(str(meta).count('Orange')))
    print('Pink: ' + str(str(meta).count('Pink')))
    print('Pilkadot: ' + str(str(meta).count('Pilkadot')))
    print('Purple: ' + str(str(meta).count('Purple')))
    print('Red: ' + str(str(meta).count('Red')))
    print('Rust: ' + str(str(meta).count('Rust')))
    print('Trippy: ' + str(str(meta).count('Trippy')))
    print('Weed: ' + str(str(meta).count('Weed')))
    print('Yellow: ' + str(str(meta).count('Yellow')))
    print('Zombie: ' + str(str(meta).count('Zombie')))


start_generation()
