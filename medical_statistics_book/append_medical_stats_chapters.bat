@echo off
cd /d "d:\AI Book and Content Writer\book_automation_mcp"

powershell -Command "Get-Content 'medical_statistics_frontmatter.md' | Set-Content 'export\book\medical_statistics_book.md'"

powershell -Command "Get-Content 'medical_statistics_chapter1.md' | Add-Content 'export\book\medical_statistics_book.md'"
powershell -Command "Get-Content 'medical_statistics_chapter2.md' | Add-Content 'export\book\medical_statistics_book.md'"
powershell -Command "Get-Content 'medical_statistics_chapter3.md' | Add-Content 'export\book\medical_statistics_book.md'"
powershell -Command "Get-Content 'medical_statistics_chapter4.md' | Add-Content 'export\book\medical_statistics_book.md'"
powershell -Command "Get-Content 'medical_statistics_chapter5.md' | Add-Content 'export\book\medical_statistics_book.md'"
powershell -Command "Get-Content 'medical_statistics_chapter6.md' | Add-Content 'export\book\medical_statistics_book.md'"
powershell -Command "Get-Content 'medical_statistics_chapter7.md' | Add-Content 'export\book\medical_statistics_book.md'"
powershell -Command "Get-Content 'medical_statistics_chapter8.md' | Add-Content 'export\book\medical_statistics_book.md'"
powershell -Command "Get-Content 'medical_statistics_chapter9.md' | Add-Content 'export\book\medical_statistics_book.md'"
powershell -Command "Get-Content 'medical_statistics_chapter10.md' | Add-Content 'export\book\medical_statistics_book.md'"
powershell -Command "Get-Content 'medical_statistics_chapter11.md' | Add-Content 'export\book\medical_statistics_book.md'"
powershell -Command "Get-Content 'medical_statistics_chapter12.md' | Add-Content 'export\book\medical_statistics_book.md'"
powershell -Command "Get-Content 'medical_statistics_chapter13.md' | Add-Content 'export\book\medical_statistics_book.md'"
powershell -Command "Get-Content 'medical_statistics_chapter14.md' | Add-Content 'export\book\medical_statistics_book.md'"
powershell -Command "Get-Content 'medical_statistics_chapter15.md' | Add-Content 'export\book\medical_statistics_book.md'"
powershell -Command "Get-Content 'medical_statistics_chapter16.md' | Add-Content 'export\book\medical_statistics_book.md'"
powershell -Command "Get-Content 'medical_statistics_chapter17.md' | Add-Content 'export\book\medical_statistics_book.md'"
powershell -Command "Get-Content 'medical_statistics_chapter18.md' | Add-Content 'export\book\medical_statistics_book.md'"

powershell -Command "Get-Content 'medical_statistics_appendix_glossary.md' | Add-Content 'export\book\medical_statistics_book.md'"
powershell -Command "Get-Content 'medical_statistics_appendix_tables.md' | Add-Content 'export\book\medical_statistics_book.md'"
powershell -Command "Get-Content 'medical_statistics_appendix_resources.md' | Add-Content 'export\book\medical_statistics_book.md'"

powershell -Command "Get-Content 'medical_statistics_companion_website.md' | Add-Content 'export\book\medical_statistics_book.md'"
powershell -Command "Get-Content 'medical_statistics_backmatter.md' | Add-Content 'export\book\medical_statistics_book.md'"

echo All medical statistics book files appended successfully!
