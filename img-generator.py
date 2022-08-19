import os
# import pprint
import cv2
from random import choices
import numpy as np

takenMaps = {}
possible_maps = ['samambaia02.png', 'samambaia03.png',
                 'varjao01.png', 'varjao02.png', 'varjao03.png']
idx = 10


def chooseRandomMaps() -> list:
    return choices(possible_maps, k=4)


def load_imgs(path, maps) -> list:
    maps_choosed = ()
    imgs = []

    for map in maps:
        img = cv2.imread(os.path.join(path, map))
        if img is not None:
            maps_choosed += (map,)
            imgs.append(img)

    if takenMaps.get(map) is None:
        takenMaps[map] = 1
        return np.array_split(imgs, 2)
    return []


def concat_vh(list_2d):
    # return final image
    return cv2.vconcat([cv2.hconcat(list_h) for list_h in list_2d])


def getMap(name, odd):
    map = cv2.imread(os.path.join('./maps/mapas', name))


name_idx = 0
while (idx > 0):
    imgs = load_imgs('./maps/mapas', chooseRandomMaps())
    if len(imgs) > 0:
        img = concat_vh(imgs)
        cv2.imwrite('./nft-images/' + str(name_idx) + '.jpg', img)
        name_idx += 1
    idx -= 1
