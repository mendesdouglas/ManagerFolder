import distutils
from distutils.core import setup
import py2exe.build_exe
import sys,os
import os.path
import tkinter
import _tkinter

distutils.core.setup(
      windows=[
            {'script': 'navegate.py',
             #'icon_resources': [(1, 'moduleicon.ico')]
            }
      ],
      zipfile=None,
      options={'py2exe':{
                         'includes': ['tkinter'],
                         'bundle_files': 3
                        }
      }
  )

# from cx_Freeze import setup, Executable
# import tkinter as tk
# from tkinter import ttk
# import shutil
# import os
# import time
# import datetime
# import sys
# import matplotlib
# base=None
# if sys.platform=='win32':
#        base = "Win32GUI"
#
# setup(name='tk',
#       version='0.1',
#       description='Visualizador de producao',
#       executables=[Executable("managerFolder.py",base=base)],
#       options={"build.exe": {"packages":["tkinter"]}},
#       )
#
#
# # from cx_Freeze import setup, Executable
# # import tkinter as tk
# # from tkinter import ttk
# # import shutil
# # import os
# # import time
# # import datetime
# # import sys
# #
# # base=None
# #
# # if sys.platform=='win32':
# #       base = "Win32GUI"
# #
# #
# #
# # setup(name='tk',
# #       version='00.1',
# #       description='Visualizador de producao',
# #       options={"build.exe":["tkinter"]},
# #       executables=[Executable("managerFolder.py", base=base)]
# #       )
#
#
