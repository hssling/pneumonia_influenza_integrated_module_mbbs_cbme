@echo off
cd /d "d:\AI Book and Content Writer\book_automation_mcp"

REM Initialize/overwrite the Kannada master file with UTF-8 encoding
powershell -NoLogo -NoProfile -Command "$css = @"<style>`r`n/* Kannada Font Styling */`r`n* {`r`n  font-family: 'Nirmala UI', 'Noto Sans Kannada', 'Tunga', 'Kedage', 'Mukta Malar', sans-serif !important;`r`n}`r`n</style>`r`n`r`n"@; Set-Content -Encoding UTF8 'export\book\community_medicine_kannada.md' $css"

REM Append front matter and outline (UTF-8)
powershell -NoLogo -NoProfile -Command "Get-Content 'drafts_kn\00_frontmatter_kn.md' | Add-Content -Encoding UTF8 'export\book\community_medicine_kannada.md'"
powershell -NoLogo -NoProfile -Command "Get-Content 'drafts_kn\outline_kn.md' | Add-Content -Encoding UTF8 'export\book\community_medicine_kannada.md'"

REM Append all chapter*.md in name order
powershell -NoLogo -NoProfile -Command "$ErrorActionPreference='Stop'; Get-ChildItem 'drafts_kn\chapter*.md' | Sort-Object Name | ForEach-Object { Get-Content $_.FullName | Add-Content -Encoding UTF8 'export\book\community_medicine_kannada.md' }"

REM Append appendices
powershell -NoLogo -NoProfile -Command "Get-Content 'drafts_kn\appendix_glossary_kn.md' | Add-Content -Encoding UTF8 'export\book\community_medicine_kannada.md'"
powershell -NoLogo -NoProfile -Command "Get-Content 'drafts_kn\appendix_abbreviations_kn.md' | Add-Content -Encoding UTF8 'export\book\community_medicine_kannada.md'"
powershell -NoLogo -NoProfile -Command "Get-Content 'drafts_kn\appendix_viva_osce_kn.md' | Add-Content -Encoding UTF8 'export\book\community_medicine_kannada.md'"
powershell -NoLogo -NoProfile -Command "Get-Content 'drafts_kn\appendix_mcq_bank_kn.md' | Add-Content -Encoding UTF8 'export\book\community_medicine_kannada.md'"

echo Kannada book assembled at export\book\community_medicine_kannada.md
