import os

directory_path = "E:\\Загрузки"

directory_content = os.listdir(directory_path)
for filename in directory_content:
    if filename.endswith(".torrent"):
        os.remove(os.path.join(directory_path, filename))

