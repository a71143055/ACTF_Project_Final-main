"""Top-level runner for the ACTF CAD generator.

This file is kept as a small script that delegates to the
`actf_project` package implementation. Running this file will
produce the same behavior as before but the project code is now
organized as an importable package under `src/actf_project`.
"""

from actf_project.generator import export_all


if __name__ == "__main__":
    export_all()
    print("ACTF 3D concept exported to ./output")
