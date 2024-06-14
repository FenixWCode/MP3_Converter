import os
import time
import mp3_convert

class DirMonitor:
    def __init__(self, dir_path, exten=".mp4"):
        self.dir_path = dir_path
        self.exten = exten

    def list_files(self) -> list:
        files = []
        for file in os.listdir(self.dir_path):
            full_file_path = os.path.join(self.dir_path, file)

            # Check if format is mp4
            file, extension = os.path.splitext(file)
            if extension == self.exten:
                files.append(full_file_path)

        return  files

    def monitor(self):
        files_status = self.list_files()
        while True:
            time.sleep(5)
            current_status = self.list_files()
            new_files = list(set(current_status) - set(files_status))

            for new_file in new_files:
                mp3_convert.convert(new_file)

            files_status = current_status

d1 = DirMonitor("tmp")
d1.list_files()