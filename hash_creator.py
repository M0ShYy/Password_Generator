import hashlib

file ="pass.txt"
with open(file, mode='r') as file:
    # reading the CSV file
    data = file.readlines()
    print(len(data))
    for i in range(0, len(data)):

        passwd = data[i]
        hash_sha256 = hashlib.sha256(passwd.encode('utf-8')).hexdigest()
        hash_md5 = hashlib.md5(passwd.encode('utf-8')).hexdigest()

        print('\n\nligne:', i + 1)
        print('password:',passwd)
        print("sha256", hash_sha256)
        print("md5:", hash_md5)
        md5_data = passwd[:-1] + "," + hash_md5 + "\n"
        sha256_data = passwd[:-1] + "," + hash_sha256 + "\n"

        with open("MD5.csv", 'a') as f_object:
            f_object.writelines(md5_data)
            f_object.close()

        with open("sha256.csv", 'a') as f_object:
            f_object.writelines(sha256_data)
            f_object.close()

