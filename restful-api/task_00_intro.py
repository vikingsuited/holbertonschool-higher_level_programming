#!/usr/bin/python3
"""
Simple templating program to generate personalized invitations.
"""
import os


def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template.
    """
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        processed_template = template
        placeholders = ["name", "event_title", "event_date", "event_location"]
        
        for key in placeholders:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            processed_template = processed_template.replace("{" + key + "}", str(value))
        
        filename = "output_{}.txt".format(index)
        try:
            with open(filename, 'w') as f:
                f.write(processed_template)
        except Exception as e:
            print("Error writing to file {}: {}".format(filename, e))
