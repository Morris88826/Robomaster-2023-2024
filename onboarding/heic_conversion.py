import glob
import os
def heic_to_jpg(jpg_path):
    if not os.path.exists(jpg_path):
        os.mkdir(jpg_path)
    for heic_file in glob.glob('./heic/*.HEIC'):
        out_path = os.path.join(jpg_path, os.path.basename(heic_file).split('.')[0] + '.jpg')
        os.system(f"heif-convert {heic_file} {out_path}")

if __name__ == "__main__":
    heic_to_jpg('./jpg')