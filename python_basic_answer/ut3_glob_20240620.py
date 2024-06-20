import glob

files = glob.glob("ut3_files/**/report*.txt",recursive=True)

for f in files:
    print(f)










