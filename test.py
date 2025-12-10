#!/usr/bin/env python3
import os
import shutil
import subprocess

script_dir = os.path.dirname(os.path.abspath(__file__))
test_source = os.path.join(script_dir, 'test_source')
test_destination = os.path.join(script_dir, 'test_destination')

# Clear destination folder
for item in os.listdir(test_destination):
    item_path = os.path.join(test_destination, item)
    if os.path.isdir(item_path):
        shutil.rmtree(item_path)
    else:
        os.remove(item_path)
print(f"Cleared {test_destination}", flush=True)

# Run the main script
subprocess.run(['python3', 'html_ssi.py', test_source, test_destination], cwd=script_dir)
