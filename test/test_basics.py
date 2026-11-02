import pathlib
import py_compile

ROOT = pathlib.Path(__file__).resolve().parent.parent


def test_all_python_files_compile():
    files = [p for p in ROOT.rglob("*.py") if "tests" not in p.parts]
    assert files, "no Python source files found"
    for path in files:
        py_compile.compile(str(path), doraise=True)
