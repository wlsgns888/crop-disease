import json
import numpy as np
import pandas as pd
import os, copy
import cv2
import seaborn as sns
import matplotlib.pyplot as plt

def load_json(json_path):
    with open(json_path, "r") as json_file:
        data = json.load(json_file)
        return data

def draw_bbox(img, annotations):
    bbox_img = copy.deepcopy(img)

    bbox_list = annotations['bbox']
    part_list = annotations['part']

    for bbox in bbox_list:
        x1 = int(bbox['x'] + 0.5)
        y1 = int(bbox['y'] + 0.5)
        x2 = int(bbox['x'] + bbox['w'] + 0.5)
        y2 = int(bbox['y'] + bbox['h'] + 0.5)
        cv2.rectangle(bbox_img, (x1,y1), (x2,y2), (0,255,0))

    for bbox in part_list:
        x1 = int(bbox['x'] + 0.5)
        y1 = int(bbox['y'] + 0.5)
        x2 = int(bbox['x'] + bbox['w'] + 0.5)
        y2 = int(bbox['y'] + bbox['h'] + 0.5)
        cv2.rectangle(bbox_img, (x1,y1), (x2,y2), (0,0,255))

    return bbox_img

if __name__ == '__main__':
    data_dir = r'C:\Users\talee\Desktop\dacon\crop_disearse\sample\sample_data'
    data_folder_list = os.listdir(data_dir)

    print('cnt data :', len(data_folder_list))

    annot_df = pd.DataFrame(columns=['area', 'disease', 'grow', 'risk', 'crop'])
    skip_cnt = 10
    for idx, data_folder in enumerate(data_folder_list):
        data_folder_dir = os.path.join(data_dir, data_folder)
        img_path = os.path.join(data_folder_dir, f'{data_folder}.jpg')
        json_path = os.path.join(data_folder_dir, f'{data_folder}.json')
        csv_path = os.path.join(data_folder_dir, f'{data_folder}.csv')

        json_data = load_json(json_path)
        annot = json_data['annotations']
        annot_df.loc[idx] = [annot['area'], annot['disease'], annot['grow'], annot['risk'], annot['crop']]

        if idx % skip_cnt == 0:
            img = cv2.imread(img_path)
            bbox_img = draw_bbox(img, json_data['annotations'])
            cv2.imshow('img', img)
            cv2.imshow('bbox_img', bbox_img)
            cv2.waitKey(1)

        

    plt.figure()
    sns.countplot(x="area", data=annot_df)

    plt.figure()
    sns.countplot(x="disease", data=annot_df)
    
    plt.figure()
    sns.countplot(x="grow", data=annot_df)

    plt.figure()
    sns.countplot(x="risk", data=annot_df)

    plt.figure()
    sns.countplot(x="crop", data=annot_df)

    plt.show()
    a= 1

            




    