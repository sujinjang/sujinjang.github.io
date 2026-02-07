#!/usr/bin/env python3
import re

# Mapping of BibTeX keys to image filenames
image_map = {
    'jang2017tcm': 'tcm_2017.PNG',
    'jang2016motionflow': 'motionflow_2016.PNG',
    'choi2015hand': 'hand_2015.PNG',
    'jang2014gestureanalyzer': 'gestureanalyzer_2014.PNG',
    'gupta2014puppetx': 'puppetx_2014.PNG',
    'jang2012uio': 'uio_2012.PNG',
    'villanueva2023tcm': 'ijhcs_2023.PNG',
    'jang2022dada': 'dada_2022.PNG',
    'jang2023stxd': 'stxd_2023.PNG',
    'chang2024cmda': 'cmda_2024.PNG',
    'chang2024udga': 'udga_2024.PNG',
    'kim2024unveiler': 'unveiler_2024.PNG',
    'oh2025protoocc': 'protoocc_2025.PNG',
    'kim2025vln': 'vln_2025.PNG',
    'ko2025tta': 'tta_2025.PNG',
    'jo2025dimcol': 'dimcol_2025.png',
    'chang2025dg': 'dg_2025.PNG',
    'xu2026moe': 'moe_2026.PNG',
    'peng2026damvla': 'damvla_2026.png',
}

# Read the bib file
with open('_bibliography/publications.bib', 'r') as f:
    content = f.read()

# Add image field to each entry
for key, image in image_map.items():
    # Find the entry and add image field before the tag field
    pattern = rf'(@\w+\{{{key},.*?)(  tag={{[^}}]+}})'
    replacement = rf'\1  image={{{image}}},\n\2'
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)

# Write back
with open('_bibliography/publications.bib', 'w') as f:
    f.write(content)

print("✅ Added image fields to all BibTeX entries")
