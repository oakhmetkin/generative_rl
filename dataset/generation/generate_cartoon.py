from cartoon import cartoonify
from os import listdir, system


ORIG_IMAGES_PATH = 'dataset/data/orig'
SAVE_PATH = 'dataset/data/cartoon'


if __name__ == '__main__':
    images = listdir(ORIG_IMAGES_PATH)
    L = len(images)

    for i, img in enumerate(images):
        if i % 10 == 0:
            system('cls') # clear console output
            print(f'Progress: {(i / L * 100):.2f}% ({i + 1}/{L})')
        cartoonify(f'{ORIG_IMAGES_PATH}/{img}', f'{SAVE_PATH}/{img}')

    system('cls') # clear console output
    print(f'Progress: 100.00% ({L} images cartoonified)')
