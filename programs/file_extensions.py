import os


def get_file_extensions(folder):
    extensions = set()
    for root, _, files in os.walk(folder):
        for file in files:
            _, extension = os.path.splitext(file)
            extensions.add(extension.lower())
    return extensions


if __name__ == "__main__":
    folder_path = r"C:\Users\Xiaomi\Desktop\Картинки"

    unique_extensions = get_file_extensions(folder_path)
    print("Unique file extensions in the folder:")
    for ext in unique_extensions:
        print(ext)