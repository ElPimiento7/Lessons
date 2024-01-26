import os
import shutil
from datetime import datetime
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def get_modification_date(filepath):
    modification_time = os.path.getmtime(filepath)
    return datetime.utcfromtimestamp(modification_time).year


def organize_photos(source_folder, destination_folder):
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            file_path = os.path.join(root, file)

            # Получаем расширение файла
            _, extension = os.path.splitext(file)
            extension_lower = extension.lower()

            # Список поддерживаемых расширений
            supported_extensions = set(['.arw', '.jpeg', '.raw', '.png', '.mp3', '.mp4', '.jpg', '3gp'])

            # Добавленные расширения
            additional_extensions = ['.tmp', '.lnk', '.css', '.html', '.gal', '.cr2',
                                     '.sfk', '.ppt', '.zip', '.ttf', '.doc', '.pptm', '.cdr',
                                     '.ini', '.rar', '.jpg-large', '.pptx', '.xmp', '.mov',
                                     '.xlsx', '.pdf', '.psd', '.tiff', '.php', '.a']

            if extension_lower in supported_extensions or extension_lower in additional_extensions:
                if extension_lower in ('.arw', '.raw'):
                    extension_folder = "RawImages"
                elif extension_lower in ('.jpeg', '.jpg', '.png'):
                    extension_folder = "JpegImages"
                elif extension_lower in ('.mp3', '.mp4', '3gp'):
                    extension_folder = "MediaFiles"
                elif extension_lower in additional_extensions:
                    extension_folder = f"AdditionalFiles_{extension_lower[1:]}"
                    supported_extensions.add(extension_folder)
                else:
                    logging.warning(f"Unsupported file format for file: {file}")
                    continue
            else:
                logging.warning(f"Unsupported file format for file: {file}")
                continue

            modification_year = get_modification_date(file_path)
            logging.debug(f"Processing file: {file} - Modification year: {modification_year}")

            if modification_year:
                year_folder = os.path.join(destination_folder, str(modification_year), extension_folder)
                os.makedirs(year_folder, exist_ok=True)
                destination_path = os.path.join(year_folder, file)
                shutil.copy(file_path, destination_path)
                logging.info(f"File {file} moved to {destination_path}")
            else:
                logging.warning(f"Could not determine year for file: {file}")


if __name__ == "__main__":
    source_folder = r"C:\Users\Xiaomi\Desktop\Картинки"
    destination_folder = r"C:\Users\Xiaomi\Desktop\Sorted"

    try:
        organize_photos(source_folder, destination_folder)
    except Exception as e:
        logging.error(f"An error occurred: {e}")