import os
import csv, json, sys

def clean_file(path):

    data = []
    rootdir = path

    for subdir, dirs, files in os.walk(rootdir):

        for f in files:

            print(os.path.join(subdir, f))

            with open(f) as fp:
                line = fp.readline()
                cnt = 1
                
                while line:
                    row = line.strip()
                    data.append(row)
                    line = fp.readline()
                    cnt += 1

            f = open(f, 'w')

            for (idx, i) in enumerate(data):
                if idx == 0:
                    f.write("[{},".format(i))
                elif idx < len(data)-1:
                    f.write("{},".format(i))
                else:
                    f.write("{}]".format(i))
            f.close()

def json_2_csv(path):

    for subdir, dirs, files in os.walk(rootdir):

        for fi in files:

            print(os.path.join(subdir, fi))
            #sys.setdefaultencoding("UTF-8") 

            fileInput = fi
            fileOutput = fo
            inputFile = open(fileInput)
            outputFile = open(fileOutput, 'w')
            data = json.load(inputFile)
            inputFile.close()
            output = csv.writer(outputFile)
            output.writerow(data[0].keys())
            for row in data:
                output.writerow(row.values())