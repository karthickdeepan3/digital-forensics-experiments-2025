Sleuth Kit Easy Method (Single Image)
=====================================

When is ONE image enough?
-------------------------
- If you have a *standalone* image (e.g., .img, .dd, .raw, or a single .E01 file that is NOT part of a split set), then one file is enough.
- If your evidence is a *split* Expert Witness (EWF) image (e.g., 4Dell Latitude CPi.E01, 4Dell Latitude CPi.E02, ...), you MUST keep **all parts in the same folder**. TSK will read the first part (.E01) but still needs the rest present.

Quick start
-----------
1) Install Sleuth Kit on Windows (or ensure fsstat/mmls/fls/icat/istat are in PATH).
2) Put your image file(s) in a folder, e.g. C:\SleuthKitLab\
3) Run:
   tsk_easy_run.bat "C:\SleuthKitLab\your_image.E01"
4) Open the generated outputs in the *_outputs folder.
5) To recover a file by inode (from filelist.txt), run:
   recover_one.bat "C:\SleuthKitLab\your_image.E01" 128 recovered.bin

Tip: If your .E01 is part of a split set, keep .E01 and .E02 (and more, if any) together.
