# Lungs X-ray Chest Classification(COVID-19 or Other pneumonia)

    This project uses a convolutional neural network to build a classifier to determine whether a patient's pneumonia is due to neocoronavirus or other types of pneumonia. The data set is described below.

## Dataset

* [Kaggle Dataset](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia)
  
    The dataset is organized into 3 folders (train, test, val) and contains subfolders for each image category (Pneumonia/Normal). There are 5,863 X-Ray images (JPEG) and 2 categories (Pneumonia/Normal). Chest X-ray images (anterior-posterior) were selected from retrospective cohorts of pediatric patients of one to five years old from Guangzhou Women and Children’s Medical Center, Guangzhou. All chest X-ray imaging was performed as part of patients’ routine clinical care.

* [Github Dataset](https://github.com/ieee8023/covid-chestxray-dataset)
  
  This project extract images from publications.

## Details

### Datasets description

|       |COVID-19   |Others   |
|-------|-----------|---------|
|train  |48         |48       |
|val    |21         |21       |

### Lab environment

* Hygon C86 7185 CPU
* Pre-Wukong DCU
* 128GB RAM

### Result

|           |ACC    |AUC    |SEN    |F1     |
|-----------|-------|-------|-------|-------|
|train      |0.9167 |1.0000 |0.8333 |0.9230 |
|val        |0.9286 |0.9955 |0.8571 |0.9091 |

### ROC

  <img src="./result/data-resnet50_public.pth.png" width="400"/>
