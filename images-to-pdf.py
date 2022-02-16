# This is a script to easily convert a bunch of images to PDF
# Useful when converting cultured images which I have found scattered around the internet
# Written by Ralph Louis Gopez

import gc
import click
from os import listdir
from os.path import isfile, join
from pathlib import Path
from PIL import Image

# Compiles a single folder of images to a PDF
def compile(directory):
    print(f'Compiling: {directory}')
    base_image = None
    images = []

    paths = listdir(directory)
    paths.sort()

    for index, path in enumerate(paths):
        absolute_path = join(directory, path)

        current_image = Image.open(absolute_path)
        current_image = current_image.convert('RGB')

        if index == 0:
            base_image = current_image

        if isfile(absolute_path) and index > 0:
            images.append( current_image )
        print(f'Adding: {absolute_path}')

    filename = Path(directory).parts[-1] + '.pdf'
    base_image.save(filename, 'PDF', resolution=100.00, save_all=True, append_images=images)
    print(f'Saved as: {filename}')
    
    del base_image
    del images
    gc.collect()

# Compiles multiple PDFs separated by a folders in a root directory
def use_collection_folder(directory):
    titles = listdir(directory)
    titles.sort()

    compileAll = input('Compile all? (y/n) ') == 'y'

    if compileAll:
        for title in titles:
            compile(join(directory, title))
    else:
        for index, title in enumerate(titles):
            print(f'{index} - {title}')
        compile_index = int(input('Input index to compile: '))
        compile(join(directory, titles[compile_index]))

@click.command()
@click.option('--path', type=click.Path(exists=True, file_okay=False), required=True, help="Path of input directory.")
@click.option('--mode', type=click.Choice(['individual', 'collection'], case_sensitive=False), default='individual', help="Mode of compilation.")
def main(mode, path):
    if mode == 'individual':
        compile(path)
    else:
        use_collection_folder(path)

if __name__ == '__main__':
    main()
