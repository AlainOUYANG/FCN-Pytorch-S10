import glob

DATA_PATH = './Rebuild_DB/cut_depth/*/*.bmp'

dir_path =  DATA_PATH
imgs_path = glob.glob(dir_path)
print('Total image number: %d' % len(imgs_path))
