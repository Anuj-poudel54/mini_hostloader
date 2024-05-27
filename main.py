from watchdog.observers import Observer
import time
from watchers import Watcher
from pathlib import Path
import os


class Main:
    def __init__(self, watcher: Watcher, on_change_command: str, file_with_paths: str | Path | None = None, path_to_watch: str | Path | None = None, recursive_watch: bool = False) -> None:
        self.event_handler = watcher
        self.observers = []
        self.path_to_watch = path_to_watch
        self.file_with_paths = file_with_paths
        self.recursive_watch = recursive_watch
        self.paths = []

        if not on_change_command:
            raise Exception(
                "Please command that should be run after file modification.")
        self.event_handler.add_command(on_change_command)

        if self.file_with_paths and not os.path.isfile(self.file_with_paths):
            raise FileNotFoundError("Path you provided is not a file path.")

        if not self.file_with_paths and not self.path_to_watch:
            raise Exception("Either provide single path or file with path")

        self._read_paths()

    def watch(self) -> Exception | None:
        if not (self.path_to_watch or self.paths):
            raise Exception(
                "Provide path to directory to watch or file containing paths")

        for observer in self.observers:
            observer.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:

            for observer in self.observers:
                observer.stop()

        for observer in self.observers:
            observer.join()

    def _read_path(self, path: Path | str):

        if not os.path.isdir(path):
            raise NotADirectoryError(f"'{path}' is not a directory")

        if len(os.listdir(path)) <= 0:
            return

        observer = Observer()
        observer.schedule(
            self.event_handler, path=self.path_to_watch, recursive=self.recursive_watch)
        self.observers.append(observer)

    def _read_paths(self):

        # prioratize files with paths rather than just one directory
        if self.file_with_paths:

            with open(self.file_with_paths) as f:
                self.paths = list(map(lambda p: p.strip("\n"), f.readlines()))

            for path in self.paths:
                self._read_path(path)

        else:
            self._read_path(self.path_to_watch)


if __name__ == "__main__":
    Main(Watcher(), "echo 'modification detected'",
         path_to_watch="path/to/dir").watch()
