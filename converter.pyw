import os
import re
import sys
from io import TextIOWrapper
from tkinter import Tk, filedialog, messagebox

# HH:MM:SS
# not foolproof, but catches some bad time inputs
pattern = re.compile('[0-9]{2}:[0-5][0-9]:[0-5][0-9]')

GUI = None
if 'PROMPT' in os.environ:
    GUI = False
else:
    GUI = True



#   FORMAT:
# CHAPTER{#}=HH:MM:SS.mmm
# CHAPTER{#}NAME={NAME}

def convert(f: TextIOWrapper) -> None:
    path, ext = os.path.splitext(f.name)
    savepath = f'{path}_(1){ext}'

    out = None
    try:
        out = open(savepath, 'x')
    except FileExistsError:
        f.close()
        error(f'Error: "{savepath}" already exists.')

    for i, line in enumerate(f):
        i +=  1
        time, chapter = line.split(' ', 1)

        # make sure time is properly formatted
        if not pattern.match(time):
            time = f'00:{time}'
            if not pattern.match(time):
                f.close()
                out.close()
                error('Error: Invalid time or format. Check output file(s).')

        line1 = f'CHAPTER{i:02d}\t={time}.000'
        line2 = f'CHAPTER{i:02d}NAME\t={chapter}'
        out.write(f'{line1}\n')
        out.write(f'{line2}\n')
    f.close()
    out.close()
            
            
def error(message: str) -> None:
    if GUI:
        messagebox.showerror('Chapter Converter', message)
        sys.exit()
    else:
        sys.exit(message)



if __name__ == '__main__':
    Tk().withdraw()
    files = filedialog.askopenfiles()
    for f in files:
        convert(f)
