"""CLI entrypoint for `python -m actf_project`."""
from .generator import export_all


def main() -> None:
    export_all()
    print("ACTF 3D concept exported to ./output")


if __name__ == "__main__":
    main()
