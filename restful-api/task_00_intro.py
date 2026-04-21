#!/usr/bin/python3
"""
Simple templating program to generate personalized invitations.
"""
import os


def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template.
    """
    # Giriş tiplərinin yoxlanılması
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    # Boş girişlərin yoxlanılması
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Hər bir iştirakçı üçün emal prosesi
    for index, attendee in enumerate(attendees, start=1):
        processed_template = template
        
        # Placeholder siyahısı
        placeholders = ["name", "event_title", "event_date", "event_location"]
        
        for key in placeholders:
            value = attendee.get(key)
            # Əgər dəyər yoxdursa və ya None-dırsa "N/A" ilə əvəzlə
            if value is None:
                value = "N/A"
            
            # Şablondakı {key} hissəsini real dəyərlə əvəzləyirik
            processed_template = processed_template.replace("{" + key + "}", str(value))
        
        # Çıxış faylının yaradılması
        filename = "output_{}.txt".format(index)
        
        try:
            with open(filename, 'w') as f:
                f.write(processed_template)
        except Exception as e:
            print("Error writing to file {}: {}".format(filename, e))
