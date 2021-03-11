@echo off

pyinstaller -F -w -i carlife.ico carlife_main_window.py

set source_path=dist
set dest_path="carlife protocol analysis tool"

echo %source_path%
echo %dest_path%

copy %source_path%\carlife_main_window.exe %dest_path%
copy res\import.png %dest_path%\res\import.png
copy res\filter.png %dest_path%\res\filter.png

cd %dest_path%
del "CarLife PAT.exe"
ren carlife_main_window.exe "CarLife PAT.exe"

pause