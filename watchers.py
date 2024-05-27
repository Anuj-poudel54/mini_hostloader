from watchdog.events import FileSystemEventHandler
import os


class Watcher(FileSystemEventHandler):

    def add_command(self, command: str):
        self.command = command

    def on_any_event(self, event):
        print(f'Event type: {event.event_type}  path : {event.src_path}')
        print(f"Running '{self.command}'...")
        os.system(self.command)
