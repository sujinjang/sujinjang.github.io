#!/usr/bin/env python3
"""
Helper script to add a new publication to the BibTeX file
"""

import sys

def get_input(prompt, default=None):
    """Get input with optional default value"""
    if default:
        prompt = f"{prompt} [{default}]"
    value = input(f"{prompt}: ").strip()
    return value if value else default

def main():
    print("=== Add New Publication ===\n")
    
    # Basic info
    key = get_input("BibTeX key (e.g., jang2026paper)")
    title = get_input("Title")
    authors = get_input("Authors (separate with 'and')")
    year = get_input("Year")
    
    # Type
    print("\nType: 1=Conference, 2=Journal, 3=Preprint")
    type_choice = get_input("Choose type", "1")
    type_map = {"1": "conference", "2": "journal", "3": "preprint"}
    pub_type = type_map.get(type_choice, "conference")
    
    # Entry type
    entry_type = "inproceedings" if pub_type == "conference" else "article"
    
    # Tag
    tag = get_input("Tag (e.g., C14, J3, P5)")
    
    # Optional fields
    venue = get_input("Venue (e.g., CVPR, NeurIPS)", "")
    acceptance = get_input("Acceptance rate (e.g., 25%)", "")
    pdf = get_input("PDF URL", "")
    code = get_input("Code URL", "")
    website = get_input("Project website", "")
    
    # Build BibTeX entry
    bibtex = f"""
@{entry_type}{{{key},
  title={{{title}}},
  author={{{authors}}},
"""
    
    if pub_type == "conference":
        bibtex += f"  booktitle={{{get_input('Conference name', '')}}},\n"
    elif pub_type == "journal":
        bibtex += f"  journal={{{get_input('Journal name', '')}}},\n"
    
    bibtex += f"  year={{{year}}},\n"
    bibtex += f"  type={{{pub_type}}},\n"
    
    if venue:
        bibtex += f"  venue={{{venue}}},\n"
    if acceptance:
        bibtex += f"  acceptance={{{acceptance}}},\n"
    if pdf:
        bibtex += f"  pdf={{{pdf}}},\n"
    if code:
        bibtex += f"  code={{{code}}},\n"
    if website:
        bibtex += f"  website={{{website}}},\n"
    
    bibtex += f"  tag={{{tag}}}\n"
    bibtex += "}\n"
    
    print("\n=== Generated BibTeX Entry ===")
    print(bibtex)
    
    # Ask to append
    if get_input("\nAppend to _bibliography/publications.bib? (y/n)", "y").lower() == "y":
        with open("_bibliography/publications.bib", "a") as f:
            f.write(bibtex)
        print("✅ Added to publications.bib")
        print(f"\n📝 Don't forget to add teaser image: assets/teaser/{key}.png")
    else:
        print("\nEntry not added. Copy the above BibTeX manually if needed.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nCancelled.")
        sys.exit(0)
