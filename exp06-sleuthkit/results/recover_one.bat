@echo off
REM recover_one.bat - Recover a single file by inode from an image
REM Usage: recover_one.bat "C:\path\to\image.E01" 128 [output_name]
SETLOCAL ENABLEDELAYEDEXPANSION

if "%~2"=="" (
  echo Usage: %~nx0 "C:\path\to\image.E01" INODE [output_name]
  echo Example: %~nx0 "C:\SleuthKitLab\4Dell Latitude CPi.E01" 128 recovered.bin
  goto :eof
)

set "IMG=%~1"
set "INODE=%~2"
set "OUTNAME=%~3"

REM Configure Sleuth Kit path if needed
set "TSK="

if not "%TSK%"=="" (
  set "ICAT=%TSK%\icat.exe"
  set "ISTAT=%TSK%\istat.exe"
) else (
  set "ICAT=icat.exe"
  set "ISTAT=istat.exe"
)

for %%I in ("%IMG%") do (
  set "OUTDIR=%%~dpnI_outputs"
  if not exist "!OUTDIR!" mkdir "!OUTDIR!"
)

if "%OUTNAME%"=="" set "OUTNAME=file_!INODE!.bin"

echo [+] Recovering inode %INODE% from "%IMG%" to "%OUTDIR%\%OUTNAME%"
"%ICAT%" "%IMG%" %INODE% > "!OUTDIR!\%OUTNAME%" 2> "!OUTDIR!\icat_%INODE%_stderr.log"

echo [+] Writing metadata to "!OUTDIR!\metadata_%INODE%.txt"
"%ISTAT%" "%IMG%" %INODE% > "!OUTDIR!\metadata_%INODE%.txt" 2>&1

echo Done.
ENDLOCAL
