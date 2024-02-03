
# this is for making the swf section of the file-z list.

import os

def generate_html_links(directory_path):
    # Get a list of SWF files in the specified directory
    swf_files = [file for file in os.listdir(directory_path) if file.endswith(".swf")]

    # Check if there are any SWF files in the directory
    if not swf_files:
        print("No SWF files found in the specified directory.")
        return ""

    # Sort the list of SWF files
    swf_files.sort()

    # Identify and remove duplicates
    unique_swf_files = list(set(swf_files))
    duplicates = [duplicate for duplicate in set(swf_files) - set(unique_swf_files)]

    # Create HTML content with comments for removed duplicates and formatted links
    html_content = "<!-- List generated for SWF files. Just copy and paste into the appropriate SWF section. -->\n"
    
    if duplicates:
        html_content += "<!-- Duplicates Removed: -->\n"
        for duplicate in duplicates:
            html_content += f'<!-- {duplicate} -->\n'

    for swf_file in unique_swf_files:
        swf_url = f"https://raw.githubusercontent.com/MegaTheLEGEND/swf-storage/master/{swf_file}"
        html_content += f'<a href="./gfiles/flash/index.html?swf={swf_url}">{swf_file.replace(".swf", "")}</a>\n'

    return html_content

# Get the script's directory
script_directory = os.path.dirname(os.path.abspath(__file__))

# Set the directory path to the parent directory
directory_path = os.path.abspath(os.path.join(script_directory, '../'))

# Write HTML content to a file in the script's directory
html_file_path = os.path.join(script_directory, "swf_links.html")
with open(html_file_path, "w") as html_file:
    html_file.write(generate_html_links(directory_path))

print(f"HTML links generated successfully. Check '{html_file_path}'.")
