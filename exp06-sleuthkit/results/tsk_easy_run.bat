@echo off
REM tsk_easy_run.bat - Generate basic forensic outputs with Sleuth Kit
REM Usage: tsk_easy_run.bat "C:\path\to\image.E01"
SETLOCAL ENABLEDELAYEDEXPANSION

if "%~1"=="" (
  echo Usage: %~nx0 "C:\path\to\image.E01"
  echo Example: %~nx0 "C:\SleuthKitLab\4Dell Latitude CPi.E01"
  goto :eof
)

set "IMG=%~1"

REM ---- Configure Sleuth Kit install path if needed ----
REM If Sleuth Kit is not in PATH, set the next line to your install.
REM Example: set "TSK=C:\SleuthKit\bin"
set "TSK="

if not "%TSK%"=="" (
  set "FSSTAT=%TSK%\fsstat.exe"
  set "MMLS=%TSK%\mmls.exe"
  set "FLS=%TSK%\fls.exe"
  set "ISTAT=%TSK%\istat.exe"
) else (
  set "FSSTAT=fsstat.exe"
  set "MMLS=mmls.exe"
  set "FLS=fls.exe"
  set "ISTAT=istat.exe"
)

REM ---- Output folder next to the image ----
for %%I in ("%IMG%") do set "OUT=%%~dpnI_outputs"
if not exist "%OUT%" mkdir "%OUT%"

echo [+] Writing outputs to "%OUT%"
echo.

echo [1/3] File system info ...
"%FSSTAT%" "%IMG%" > "%OUT%\fsinfo.txt" 2>&1

echo [2/3] Partition table ...
"%MMLS%" "%IMG%" > "%OUT%\partitions.txt" 2>&1

echo [3/3] Recursive file listing (incl. deleted) ...
"%FLS%" -r "%IMG%" > "%OUT%\filelist.txt" 2>&1

echo.
echo Done. Open the following files:
echo   - "%OUT%\fsinfo.txt"
echo   - "%OUT%\partitions.txt"
echo   - "%OUT%\filelist.txt"
echo.
echo To recover a file later:
echo   recover_one.bat "%%IMG%%" INODE_NUMBER  > saves the file in the same folder.
echo.

ENDLOCAL
