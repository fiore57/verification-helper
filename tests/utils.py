import contextlib
import os
import pathlib
import tempfile
from typing import *


@contextlib.contextmanager
def load_files(files: Dict[str, bytes]) -> Iterator[pathlib.Path]:
    with tempfile.TemporaryDirectory() as tempdir_:
        tempdir = pathlib.Path(tempdir_).resolve()
        for relpath, data in files.items():
            assert '/' not in relpath and '\\' not in relpath  # we should use pathlib
            path = tempdir / relpath
            path.parent.mkdir(parents=True, exist_ok=True)
            with open(str(path), "wb") as fh:
                fh.write(data)
        yield tempdir


@contextlib.contextmanager
def chdir(path: pathlib.Path) -> Iterator[None]:
    cwd = os.getcwd()
    try:
        os.chdir(str(path))
        yield
    finally:
        os.chdir(cwd)
