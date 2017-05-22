from __future__ import print_function
import os
import sys
from utils import *
'''
fuck the grayscale images among the RGB images which causes broadcasting error in main_bird.py
all those bad images:
/home/hadoop/Downloads/CUB_200_2011/CUB_200_2011/images/025.Pelagic_Cormorant/Pelagic_Cormorant_0022_23802.jpg
/home/hadoop/Downloads/CUB_200_2011/CUB_200_2011/images/066.Western_Gull/Western_Gull_0002_54825.jpg
/home/hadoop/Downloads/CUB_200_2011/CUB_200_2011/images/009.Brewer_Blackbird/Brewer_Blackbird_0028_2682.jpg
/home/hadoop/Downloads/CUB_200_2011/CUB_200_2011/images/063.Ivory_Gull/Ivory_Gull_0040_49180.jpg
/home/hadoop/Downloads/CUB_200_2011/CUB_200_2011/images/063.Ivory_Gull/Ivory_Gull_0085_49456.jpg
/home/hadoop/Downloads/CUB_200_2011/CUB_200_2011/images/108.White_necked_Raven/White_Necked_Raven_0070_102645.jpg
/home/hadoop/Downloads/CUB_200_2011/CUB_200_2011/images/087.Mallard/Mallard_0130_76836.jpg
/home/hadoop/Downloads/CUB_200_2011/CUB_200_2011/images/093.Clark_Nutcracker/Clark_Nutcracker_0020_85099.jpg
'''

dataset_name = "CUB_200_2011"

def get_data_files(image_dir):
	# cur_dir = os.getcwd()
	# image_dir = os.path.join(cur_dir,"data/CUB_200_2011")

	result = []
	for dirpath, dirnames, files in os.walk(image_dir):
		for file in files:
			
			file_path = os.path.join(dirpath,file)
			file_format = file_path.split(".")[-1]
			if file_format == 'jpg':
				img = imread(file_path, is_grayscale = False)
				if len(img.shape) != 3:
					print(file_path)
				else:
					result.append(file_path)

	# print(len(result)) 11788
	# print(result[:10])
	return result


if __name__ == '__main__':
	cur_dir = os.getcwd()
	image_dir = os.path.join(cur_dir,"data",dataset_name)
	all_files = get_data_files(image_dir)
	print(all_files[:10])