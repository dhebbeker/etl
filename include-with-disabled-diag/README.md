The diagnostics performed by the IAR AVR compiler can not be instructed to ignore third party files.

As a workaround, wrapper files are used which disable some diagnostics before including the third 
party header files. At the end, the diagnostic levels are restored.

`updateWrapperFiles.py` allows to update the header files with those of `../include` directory.

In order to use those wrappers, add this directory instead of `../include` to you include paths.