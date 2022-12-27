import asyncio
import os
import time
import uuid

from watchdog.events import FileSystemEventHandler, FileCreatedEvent
from watchdog.observers import Observer

from db import xml_db
from utils.xml_converter import converter
from utils.logger import logger


def get_csv_files_in_input_folder():
    return [os.path.join(dp, f) for dp, dn, filenames in os.walk(CSV_INPUT_PATH) for f in filenames if
            os.path.splitext(f)[1] == '.csv']


def generate_unique_file_name(directory):
    return f"{directory}/{str(uuid.uuid4())}.xml"


def convert_csv_to_xml(in_path, out_path):
    converter(in_path, out_path)


class CSVHandler(FileSystemEventHandler):
    def __init__(self, input_path, output_path):
        self._output_path = output_path
        self._input_path = input_path

        # generate file creation events for existing files
        for file in [os.path.join(dp, f) for dp, dn, filenames in os.walk(input_path) for f in filenames]:
            event = FileCreatedEvent(os.path.join(CSV_INPUT_PATH, file))
            event.event_type = "created"
            self.dispatch(event)

    async def convert_csv(self, csv_path):
        # here we avoid converting the same file again
        # check converted files in the database
        if csv_path in await self.get_converted_files():
            return

        logger(f"new file to convert: '{csv_path}'")

        # we generate a unique file name for the XML file
        xml_path = generate_unique_file_name(self._output_path)

        # we do the conversion
        convert_csv_to_xml(csv_path, xml_path)
        logger(f"new xml file generated: '{xml_path}'")

        # once the conversion is done, we should update the converted_documents tables
        if xml_db.transfer_file_converted(csv_path, os.path.getsize(csv_path), xml_path):
            logger(f"csv imported to the db: {csv_path}")

        # we should store the XML document into the imported_documents table
        if xml_db.transfer_file_imported(xml_path, xml_path):
            logger(f"xml imported to the db: {xml_path}")

    async def get_converted_files(self):
        # you should retrieve from the database the files that were already converted before
        return xml_db.get_files_converted()

    def on_created(self, event):
        if not event.is_directory and event.src_path.endswith(".csv"):
            asyncio.run(self.convert_csv(event.src_path))


if __name__ == "__main__":

    CSV_INPUT_PATH = "/csv"
    XML_OUTPUT_PATH = "/shared/output"

    # create the file observer
    observer = Observer()
    observer.schedule(
        CSVHandler(CSV_INPUT_PATH, XML_OUTPUT_PATH),
        path=CSV_INPUT_PATH,
        recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()
