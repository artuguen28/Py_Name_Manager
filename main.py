import os
from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt
import matplotlib.image as mpimg



def main():

    p_path = input(str("Diretório da pasta a ser trabalhada: "))
    name = input(str("Pessoa que tirou a foto: "))



    onlyfiles = [f for f in listdir(p_path) if isfile(join(p_path, f))]

    for p in onlyfiles:

        img = mpimg.imread(f"{p_path}/{p}")
        imgplot = plt.imshow(img)
        plt.show()

        pip = input(str("Digite as o nome das pessoas na foto: ")).split(" ")
        pip = ";".join(pip)
        print(pip)

        new_name = f"{p_path}/Foto;{name}.{pip}.jpg"

        os.rename(f"{p_path}/{p}", new_name)


if __name__ == "__main__":
    main()