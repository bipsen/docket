import os
import socket
import logging
from pyairtable import Table
from pyairtable.formulas import match


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class Docket:
    def __init__(self, airtable_name):
        airtable_api_key = os.environ["AIRTABLE_API_KEY"]
        airtable_base_id = os.environ["AIRTABLE_WEBSCRAPING_BASE_ID"]
        self.table = Table(airtable_api_key, airtable_base_id, airtable_name)

    def get_jobs(self):
        while True:
            # Check if already in progress with this computer
            record = self.table.first(
                formula=match(
                    {"Progress": "In progress", "Worker": socket.gethostname()}
                )
            )

            # If not, get first empty record
            if not record:
                record = self.table.first(sort=["Id"], formula="Progress=''")

            # If not, harvesting is finished
            if not record:
                logging.info(f"Finished harvesting")
                break

            target = record["fields"]["Id"]
            self.table.update(
                record["id"],
                {"Progress": "In progress", "Worker": socket.gethostname()},
            )
            logging.info(f"Now harvesting {target}")
            yield target
            self.table.update(record["id"], {"Progress": "Done"})
