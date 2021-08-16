"""
The script is used to sort and deduplicate the links at the end of README.

"""

import re

def main():
    with open('./README.md', 'r') as f:
        readme_lines = f.readlines()
    links_anchor = readme_lines.index('<!---Links--->\n') + 1

    links = readme_lines[links_anchor:]
    sorted_links = sorted(set(links), key=lambda x: int(re.findall(r'\[(\d+)\]', x)[0]))

    with open('./new_README.md', 'w') as f:
        for line in readme_lines[:links_anchor] + sorted_links:
            f.write(line)
    
if __name__ == '__main__':
    main()
