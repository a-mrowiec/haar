import glob
import os.path

with open('positives-info.txt', 'w') as outfile:
    for fname in glob.iglob('positives/**/info.txt', recursive=True):
        with open(fname) as infile:
            absolute_dir = os.path.dirname(fname)
            for line in infile:
                outfile.write(os.path.join(absolute_dir, line))

with open('bg.txt', 'w') as outfile:
    for fname in glob.iglob('bg-*.txt', recursive=True):
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
