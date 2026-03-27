import os
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def generate_invitations(template, attendees):
    # --- Type checks ---
    if not isinstance(template, str):
        logging.error("Invalid input: template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        logging.error("Invalid input: attendees must be a list of dictionaries.")
        return

    # --- Empty inputs ---
    if not template.strip():
        logging.error("Template is empty, no output files generated.")
        return
    if not attendees:
        logging.info("No data provided, no output files generated.")
        return

    # --- Process each attendee ---
    for idx, attendee in enumerate(attendees, start=1):
        content = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key) or "N/A"
            content = content.replace(f"{{{key}}}", value)

        filename = f"output_{idx}.txt"
        try:
            with open(filename, "w") as f:
                f.write(content)
            logging.info(f"File '{filename}' generated successfully.")
        except Exception as e:
            logging.error(f"Error writing file '{filename}': {e}")
