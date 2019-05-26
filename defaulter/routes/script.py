# my_name = 'Carlos'
# my_age = 18 # not a lie
# my_height = 172 # cm
# my_weight = 71 # kg
# my_eyes = 'Brown'
# my_teeth = 'White'
# my_hair = 'Black'
    
# # print ("Let's talk about %s." % my_name)
# # # print ("He's %d centimeters tall." % my_height)
# # # print ("He's %d kilograms heavy." % my_weight)
# # # print ("Actually that's not too heavy.")
# # # print ("He's got %s eyes and %s hair." % (my_eyes, my_hair))
# # # print ("His teeth are usually %s depending on the coffee." % my_teeth)

# # this line is tricky, try to get it exactly right
# print ("If I add %d, %d, and %d I get %d. I don't know what that means but, whatever." % (
#     my_age, my_height, my_weight, my_age + my_height + my_weight))

import pandas as pd
import numpy as np
import sys
import seaborn as sns
import json

def writetoJSONFile(path, filename, data):
	filePathNameWExt = './' + path + '/' + filename	 + '.json'
	with open(filePathNameWExt, 'w') as fp:
			json.dump(data, fp)




path = './routes'
filename= 'output'
datas = {}



df = pd.read_csv('./routes/{file}'.format(file=sys.argv[1]), na_values=['#NAME?'])

data = df[sys.argv[2]]
quartiles = np.percentile(data, [25, 50, 75])
data_min, data_max = data.min(), data.max()


datas['Minimum'] = str(data_min)		
datas['Quartile1'] = str(quartiles[0])
datas['Median'] = str(quartiles[1])
datas['Quartile3'] = str(quartiles[2])
datas['Maximum'] = str(data_max)

writetoJSONFile(path, filename, datas)
		
print('Min: %.3f' % data_min + '   Max: %.3f' % data_max + '   Q1: %.3f' % quartiles[0] + '   Median : %.3f' % quartiles[1] + 'Q3: %.3f' % quartiles[2] + '   Max: %.3f' % data_max)

type_count = df['employment'].value_counts()

# print(sns.barplot(type_count.index, type_count.values, alpha=0.9))