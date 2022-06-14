import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

print(__file__)
print("\n")
print(dir_path) # the path of the file from dir_path variable is located???

#######################################################################
import os 
import glob 

os.chdir(os.getcwd() + '/Data')
path = os.getcwd() 
files = [file for file in glob.glob(path+'/*')] 
for i in files:
  df = pd.read_csv(files[i])
