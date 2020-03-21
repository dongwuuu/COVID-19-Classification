import os
import argparse
# import pandas as pd
from random import shuffle
import cv2


parser = argparse.ArgumentParser(description='utils module')
parser.add_argument('--metadata', type=str, help='path to dataset', default="./data/original_git_data/metadata.csv")
parser.add_argument('--description_path', type=str, help='path to dataset', default="./data/")

def create_data_folder(args):
    meta_df = pd.read_csv(args.metadata)
    covid_patients = meta_df['finding']=='COVID-19'
    PA = meta_df['view']=='PA'
    PA_covid = meta_df[covid_patients & PA]
    # Others = meta_df[~covid_patients & PA]
    covid_files = ["./data/original_git_data/images/" + files for files in PA_covid['filename']]
    print("number of covid:", len(covid_files))

    shuffle(covid_files)

    others = os.listdir("./data/chest_xray/train/PNEUMONIA")
    shuffle(others)
    others = others[:len(covid_files)]
    Others = ["./data/chest_xray/train/PNEUMONIA/" + f for f in others]

    train_covid = covid_files[:int(len(covid_files) * 0.7)]
    val_covid = covid_files[int(len(covid_files) * 0.7):]

    train_other = Others[:int(len(Others) * 0.7)]
    val_other = Others[int(len(Others) * 0.7):]
    print("train covid:", len(train_covid))
    print("val covid:", len(val_covid))
    print("train other:", len(train_other))
    print("val other:", len(val_other))

    for i in train_covid:
        os.system("cp " + i + " ./data/public_dataset/train/positive/" + i.split("/")[-1])
    
    for i in train_other:
        os.system("cp " + i + " ./data/public_dataset/train/negative/" + i.split("/")[-1])
    
    for i in val_other:
        os.system("cp " + i + " ./data/public_dataset/val/negative/" + i.split("/")[-1])
    
    for i in val_covid:
        os.system("cp " + i + " ./data/public_dataset/val/positive/" + i.split("/")[-1])


def file_change(args):
    data_dir = ["./data/public_dataset/train/positive","./data/public_dataset/train/negative","./data/public_dataset/val/positive","./data/public_dataset/val/negative"]
    for cur in data_dir:
        for img_path in os.listdir(cur):
            src = cv2.imread(os.path.join(cur, img_path))
            b,g,r = cv2.split(src)
            des = os.path.join(cur, img_path).replace("public_dataset", "public")
            cv2.imwrite("." + "".join(des.split(".")[:-1]) + ".png", cv2.merge([b, g, r]))
    

if __name__ == "__main__":
    args = parser.parse_args()
    # create_data_folder(args)
    file_change(args)