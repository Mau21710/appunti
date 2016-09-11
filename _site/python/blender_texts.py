# This stub runs a python script relative to the currently open
# blend file, useful when editing scripts externally.

import bpy
import os



# Use your own script name here:
filename = "/home/maurizio/GitBook/Library/maoz75/gli-appunti/python/funBlender.py"
filename = "/home/maurizio/GitBook/Library/maoz75/gli-appunti/python/funTTS.py"
filename = "/home/maurizio/GitBook/Library/maoz75/gli-appunti/python/funAsciidoc.py"

#filepath = os.path.join(os.path.dirname(bpy.data.filepath), filename)
filepath = str(filename)
global_namespace = {"__file__": filepath, "__name__": "__main__"}
with open(filepath, 'rb') as file:
    exec(compile(file.read(), filepath, 'exec'), global_namespace)


    
exec(compile(open(filename).read(), filename, 'exec'))