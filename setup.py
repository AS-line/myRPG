from cx_Freeze import setup, Executable

setup(
    name = "Main",
    version = "0.2.2",
    description = "Pygame",
    executables = [Executable("Main.pyw")]
)