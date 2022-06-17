# realitee_art_generator
A fully customisable art engine used to create multiple unique instances of artwork based on provided layers. Primarily used for the creation of NFT generative art.

Simply upload your imagery into relevant folders. Amend the code where the comments instruct you to.

You may need to: python -m pip install --upgrade Pillow OR python3 -m pip install --upgrade Pillow

python3 main.py will then run the code and generate your imagery and matching .json metadata

### IMPORTANT NOTE ###
If using Mac OS then please navigate to the folder which contains this generator (the root folder) in terminal and paste the below line of code and press Enter. Mac OS adds hidden files called .DS_Store to directories to help when searching your Mac for files. This isnt needed and is visable to Python so it will cause errors in your code if this step isnt completed.

find . -name '.DS_Store' -type f -delete