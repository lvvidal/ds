def clean_file(path):

    filepath = '/home/airflow/gcs/data/2009_file.json'
    data = []
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        
        while line:
            row = line.strip()
            data.append(row)
            line = fp.readline()
            cnt += 1

    f = open('/home/airflow/gcs/data/2009.json', 'w')
    for (idx, i) in enumerate(data):
        if idx == 0:
            f.write("[{},".format(i))
        elif idx < len(data)-1:
            f.write("{},".format(i))
        else:
            f.write("{}]".format(i))
    f.close()