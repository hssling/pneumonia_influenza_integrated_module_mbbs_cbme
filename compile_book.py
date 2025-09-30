#!/usr/bin/env python3
"""
compile_book.py - Simple Python script to compile the nutrition textbook
Author: AI Assistant for Dr. Siddalingaiah H S
"""

import os
import shutil
import glob
from pathlib import Path

def main():
    print("=" * 50)
    print("COMPILING CBME NUTRITION TEXTBOOK")
    print("=" * 50)

    # Set up directories
    base_dir = "nutrition-cbme-textbook"
    if not os.path.exists(base_dir):
        print(f"Error: Directory '{base_dir}' not found!")
        return

    os.chdir(base_dir)
    print(f"Working in directory: {os.getcwd()}")

    # Create export directories
    compiled_dir = "export/compiled"
    published_dir = "export/published"
    os.makedirs(compiled_dir, exist_ok=True)
    os.makedirs(published_dir, exist_ok=True)

    print("\n= COMBINING FRONT MATTER + ALL CHAPTERS + BACK MATTER =")

    # Start with front matter
    output_file = os.path.join(compiled_dir, "complete_nutrition_textbook.md")
    shutil.copy("front_matter.md", output_file)
    print("✓ Added front matter")

    # Add all chapters in order
    for chapter_num in range(1, 43):  # 1 to 42
        chapter_marker = f"\n{'='*50}\n# Chapter {chapter_num}\n{'='*50}\n\n"

        with open(output_file, 'a', encoding='utf-8') as outfile:
            outfile.write(chapter_marker)

        # Find chapter file
        chapter_pattern = f"drafts/chapter{chapter_num}_*.md"
        chapter_files = glob.glob(chapter_pattern)

        if chapter_files:
            chapter_file = chapter_files[0]
            with open(chapter_file, 'r', encoding='utf-8') as infile:
                content = infile.read()
                with open(output_file, 'a', encoding='utf-8') as outfile:
                    outfile.write(content)
            print(f"✓ Added Chapter {chapter_num}: {os.path.basename(chapter_file)}")
        else:
            print(f"⚠  Chapter {chapter_num} not found")

    # Add back matter
    if os.path.exists("back_matter.md"):
        with open("back_matter.md", 'r', encoding='utf-8') as infile:
            back_content = infile.read()
            with open(output_file, 'a', encoding='utf-8') as outfile:
                outfile.write(f"\n{back_content}")
        print("✓ Added back matter")

    print("\n= CHECKING FOR FORMAT CONVERSION =")

    # Check if pandoc is available
    import subprocess
    pandoc_available = False
    try:
        result = subprocess.run(["pandoc", "--version"],
                              capture_output=True, text=True, check=False)
        if result.returncode == 0:
            pandoc_available = True
            print("✓ Pandoc found! Generating multiple formats...")
        else:
            print("• Pandoc not found - only Markdown format available")
    except (FileNotFoundError, OSError):
        print("• Pandoc not found - only Markdown format available")
        print("  Install from: https://pandoc.org/installing.html")

    if pandoc_available:
        print("\nGenerating formats...")

        # PDF (requires LaTeX distribution)
        print("Creating PDF... (requires LaTeX installation)")
        pdf_result = subprocess.run([
            "pandoc", output_file,
            "-o", os.path.join(published_dir, "nutrition_cbme_complete.pdf"),
            "--pdf-engine=pdflatex", "--variable", "fontsize=12pt",
            "--variable", "geometry:margin=1in"
        ], capture_output=True, text=True)

        if pdf_result.returncode == 0:
            print("✓ PDF created successfully")
        else:
            print("• PDF creation failed (LaTeX distribution required)")

        # DOCX
        print("Creating DOCX...")
        docx_result = subprocess.run([
            "pandoc", output_file,
            "-o", os.path.join(published_dir, "nutrition_cbme_complete.docx")
        ], capture_output=False)

        if docx_result.returncode == 0:
            print("✓ DOCX created successfully")

        # HTML
        print("Creating HTML...")
        html_result = subprocess.run([
            "pandoc", output_file,
            "-o", os.path.join(published_dir, "nutrition_cbme_complete.html"),
            "--self-contained", "--toc", "--toc-depth=3"
        ], capture_output=False)

        if html_result.returncode == 0:
            print("✓ HTML created successfully")

        # EPUB
        print("Creating EPUB...")
        epub_result = subprocess.run([
            "pandoc", output_file,
            "-o", os.path.join(published_dir, "nutrition_cbme_complete.epub"),
            "--toc", "--toc-depth=3", "--epub-title",
            "Comprehensive Clinical Nutrition Textbook (CBME)"
        ], capture_output=False)

        if epub_result.returncode == 0:
            print("✓ EPUB created successfully")

        # LaTeX
        print("Creating LaTeX...")
        latex_result = subprocess.run([
            "pandoc", output_file,
            "-o", os.path.join(published_dir, "nutrition_cbme_complete.tex"),
            "--latex-engine=pdflatex"
        ], capture_output=False)

        if latex_result.returncode == 0:
            print("✓ LaTeX created successfully")

    print("\n= CREATING BOOK METADATA =")

    # Create metadata file
    metadata_content = """Book Title: Comprehensive Clinical Nutrition Textbook (CBME Compliant)
Author: Dr. Siddalingaiah H S
Email: hssling@yahoo.com
Phone: +91-8941087719
Affiliation: Indian Medical Council Representative
Edition: 2.0.0
Publication Date: 2025
ISBN: [Assigned upon commercial publication]
Total Chapters: 42
Units: 7
Compliance: CBME, NMC India
Target Audience: MBBS, MD, Nutrition Specialists
"""

    metadata_file = os.path.join(compiled_dir, "book_metadata.txt")
    with open(metadata_file, 'w', encoding='utf-8') as f:
        f.write(metadata_content)
    print("✓ Created book metadata")

    print("\n" + "=" * 50)
    print("COMPILATION COMPLETED SUCCESSFULLY!")
    print("=" * 50)

    print("\n📚 COMPILED BOOK LOCATION:")
    print("=" * 30)
    print(f"Markdown: {Path.cwd()}/{compiled_dir}/complete_nutrition_textbook.md")

    if pandoc_available:
        published_files = os.listdir(published_dir)
        for file in published_files:
            file_path = f"{Path.cwd()}/{published_dir}/{file}"
            file_type = file.split('.')[-1].upper()
            print(f"{file_type:>8}: {file_path}")

    print(f"Metadata: {Path.cwd()}/{compiled_dir}/book_metadata.txt")

    # Return to parent directory
    os.chdir("..")

    print("\n" + "=" * 50)
    print("NEXT: Push all compiled files to GitHub!")
    print("Run: git add . && git commit -m 'Add compiled book formats' && git push")
    print("=" * 50)

if __name__ == "__main__":
    main()
