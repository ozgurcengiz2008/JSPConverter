from cx_Freeze import setup, Executable

executables = [
    Executable(
        "main_11.py",
        base="Win32GUI",
        # icon="your_icon.ico",
        target_name="JSP_converter.exe"  # Hedef dosya adını burada belirtin
    )
]

options = {
    "build_exe": {
        "include_msvcr": True,
        # "includes": ["your_module"],
        # "excludes": ["unwanted_module"],
        # "packages": ["your_package"],
        "include_files": ["images/loading-6.gif"],
    }
}

setup(
    name="JSP_Converter",
    version="1.0",
    description="Mp3.ogg.wav.mp4 formatlı seslerin birbirine dönüşümünü sağlar. Video dosyalarından sesleri ayıklar ve dönüştürür.",
    executables=executables,
    options=options,
)
