import os
for root, dirs, files in os.walk(r"C:\users\win10\desktop\githubClone\Vocaba\formatters\listening"):
    print("root:", root)
    print("dirs:", dirs)
    print("files:", files)