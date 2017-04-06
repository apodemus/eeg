#ln -s path/to/repo/eeg `python3 -m site --user-site`/eeg

import site
import subprocess
import inspect
from pathlib import Path

here = inspect.getfile(inspect.currentframe())
here = Path(here)
src = str(here.parent.resolve())
dest = site.getsitepackages()[0]
dest = str(Path(dest) / 'eeg')

subprocess.call(['ln','-s', src, dest])

print(src, dest)

