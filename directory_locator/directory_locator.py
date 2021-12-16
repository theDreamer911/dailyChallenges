import argparse
import os

class DirectoryFinder:
    def __init__(self):
        self.path = ''


    @staticmethod
    def get_args():
        parser = argparse.ArgumentParser(description="Scann all files in a directory")
        parser.add_argument("path", help="Path to directory")

        return parser.parse_args()

    def scan_path(self):
        with os.scandir(self.path) as iter_path:
            for entry in iter_path:
                print(entry.name)

    def main(self):
        args = self.get_args()
        self.path = args.path

        self.scan_path()


if __name__ == "__main__":
    finder = DirectoryFinder()
    finder.main()