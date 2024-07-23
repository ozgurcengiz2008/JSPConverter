from cx_Freeze import setup, Executable
import sys
import os

# Increase recursion limit to avoid recursion errors
sys.setrecursionlimit(5000)

# include necessary packages and modules
includes = ["os", "sys", "PyQt5.QtCore", "PyQt5.QtGui", "PyQt5.QtWidgets", "mutagen", "pydub", "vlc"]
excludes = ["tkinter", "unittest"]

# include additional files
data_files = [
    ("", ["main2_form_tr.qm", "main2_form_en.qm"]),
    ("images", ["images/loading-6.gif"]),
    # Uncomment and correct if necessary
    # ("indirilen_video_ses_dosyalari", ["indirilen_video_ses_dosyalari"])  # Ensure the path and files are correct
]

# Setup configuration
setup(
    name="MusicConverter",
    version="1.0.1",
    description="A music converter application",
    options={
        "build_exe": {
            "includes": includes,
            "excludes": excludes,
            "include_files": data_files,
            "build_exe": "dist",
        }
    },
    executables=[Executable("jspconverterv1.0.1.py", base="Win32GUI", icon="icons/jsproductionicon.ico")]
)
