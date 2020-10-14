#!/usr/bin/env python3
# scanjson.py -- Scan JSON from Legiscan API
# By Tony Pearson, IBM, 2020
#
import base64
import codecs
import json
import sys

charForm = "{} for {} on {} from position {} to {}. Using '?' in-place of it!"


def get_parms(argv):
    display_help = False
    filename = ''
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if filename == '--help' or filename == '-h':
            display_help = True
        if not filename.endswith('.json'):
            display_help = True
    else:
        display_help = True

    if display_help:
        print('Syntax:')
        print(sys.argv[0], 'input_file.json')
        print(' ')

    return display_help, filename


def custom_character_handler(exception):
    print(charForm.format(exception.reason,
            exception.object[exception.start:exception.end],
            exception.encoding,
            exception.start,
            exception.end ))
    return ("?", exception.end)


if __name__ == "__main__":
    # Check proper input syntax
    codecs.register_error("custom_character_handler", custom_character_handler)

    display_help, jsonname = get_parms(sys.argv)
    state = jsonname[:2].upper()

    if not display_help:
        print('Congratulations')
        with open(jsonname, "r") as jsonfile:
            data = json.load(jsonfile)
            for entry in data:
                bill = data[entry]
                key = "{}-{}.txt".format(state, bill['number'])
                print('KEY: ', key)
                print('TITLE: ', bill['title'])
                print('SUMMARY: ', bill['description'])
                mimedata = bill['bill_text'].encode('utf-8')
                msg_bytes = base64.b64decode(mimedata)
                billtext = msg_bytes.decode('utf-8', 'custom_character_handler')
                print(len(billtext), billtext[:500])
                break
print('Done.')
        

