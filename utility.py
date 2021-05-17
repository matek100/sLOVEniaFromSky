def file_manager(file_name, file_length):
    try:
        f = open(file_name)
    except IOError:
        print(file_name + " does not exists")
        f = open(file_name, "w")
        for i in range(file_length):
            f.write("0\n")
        f.close()

