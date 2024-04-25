from pathlib import Path

class DirectoryManager:

    @staticmethod
    def get_directory_folders(directory):
        folders = Path(directory).iterdir()
        return [
            folder.name for folder in folders
        ]
