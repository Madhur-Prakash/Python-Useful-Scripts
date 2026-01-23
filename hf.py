import argparse
import os
import subprocess
import sys
from pathlib import Path
import shutil


HF = "hf"


def run_cmd(cmd):
    """Run shell command and stream output live"""

    try:
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )

        for line in process.stdout:
            print(line, end="")

        process.wait()

        if process.returncode != 0:
            raise subprocess.CalledProcessError(
                process.returncode, cmd
            )

    except subprocess.CalledProcessError:
        print("❌ Command failed:", " ".join(cmd))
        sys.exit(1)


def get_hf_cache():
    return os.environ.get(
        "HF_HOME",
        str(Path.home() / ".cache" / "huggingface")
    )


# ---------------- Commands ---------------- #


def list_cache(args):
    """List cached models"""
    run_cmd([HF, "cache", "scan"])


def show_size(args):
    """Show cache size"""
    cache = get_hf_cache()

    print(f"📁 Cache Location: {cache}")

    if os.name == "nt":  # Windows
        run_cmd([
            "powershell",
            "-Command",
            f"(Get-ChildItem '{cache}' -Recurse | "
            "Measure-Object -Property Length -Sum).Sum / 1GB"
        ])


def search_models(args):
    """Search models"""
    run_cmd([HF, "search", "models", args.query])


def download_model(args):
    """Download model"""
    cmd = [HF, "download", args.model]

    if args.resume:
        cmd.append("--resume-download")

    run_cmd(cmd)


def delete_model(args):
    """Delete a specific model from cache"""

    cache = get_hf_cache()
    hub_path = Path(cache) / "hub"

    model_cache_name = "models--" + args.model.replace("/", "--")
    model_path = hub_path / model_cache_name

    if not model_path.exists():
        print(f"❌ Model not found: {args.model}")
        sys.exit(1)

    total_size = sum(
        f.stat().st_size
        for f in model_path.rglob("*")
        if f.is_file()
    )

    size_gb = total_size / (1024 ** 3)

    if not args.yes:
        print(f"⚠️  Delete: {args.model}")
        print(f"Size: {size_gb:.2f} GB")

        confirm = input("Type 'yes' to confirm: ")

        if confirm.lower() != "yes":
            print("❌ Cancelled")
            return

    shutil.rmtree(model_path)

    print(f"✅ Deleted {args.model} ({size_gb:.2f} GB freed)")


def delete_interactive(args):
    """Interactive cache deletion"""
    print("🔍 Opening cache manager...")
    run_cmd([HF, "cache", "delete"])


def delete_all(args):
    """Delete entire cache"""

    cache = get_hf_cache()
    hub_path = Path(cache) / "hub"

    if not hub_path.exists():
        print("❌ No cache found")
        return

    total_size = sum(
        f.stat().st_size
        for f in hub_path.rglob("*")
        if f.is_file()
    )

    size_gb = total_size / (1024 ** 3)

    print("⚠️  WARNING: Delete ALL cached models")
    print(f"Size: {size_gb:.2f} GB")

    if not args.yes:
        confirm = input("Type 'yes' to confirm: ")

        if confirm.lower() != "yes":
            print("❌ Cancelled")
            return

    shutil.rmtree(hub_path)
    hub_path.mkdir(parents=True, exist_ok=True)

    print(f"✅ Cache cleared ({size_gb:.2f} GB freed)")


def model_info(args):
    """Show model info"""
    run_cmd([HF, "repo", "info", args.model])


def whoami(args):
    """Show user"""
    run_cmd([HF, "whoami"])


# ---------------- Main ---------------- #


def main():

    parser = argparse.ArgumentParser(
        description="🔥 HF CLI Helper (modern hf tool)"
    )

    sub = parser.add_subparsers(dest="command")

    # list
    sub.add_parser("list", help="List downloaded models")

    # size
    sub.add_parser("size", help="Show HF cache size")

    # search
    s = sub.add_parser("search", help="Search models")
    s.add_argument("query")

    # download
    d = sub.add_parser("download", help="Download model")
    d.add_argument("model")
    d.add_argument("--resume", action="store_true")

    # delete
    dm = sub.add_parser("delete", help="Delete model")
    dm.add_argument("model")
    dm.add_argument("-y", "--yes", action="store_true")

    # delete-interactive
    sub.add_parser("delete-interactive", help="Interactive delete")

    # delete-all
    da = sub.add_parser("delete-all", help="Delete all cache")
    da.add_argument("-y", "--yes", action="store_true")

    # info
    i = sub.add_parser("info", help="Show model info")
    i.add_argument("model")

    # whoami
    sub.add_parser("whoami", help="Show user")

    args = parser.parse_args()

    if args.command == "list":
        list_cache(args)

    elif args.command == "size":
        show_size(args)

    elif args.command == "search":
        search_models(args)

    elif args.command == "download":
        download_model(args)

    elif args.command == "delete":
        delete_model(args)

    elif args.command == "delete-interactive":
        delete_interactive(args)

    elif args.command == "delete-all":
        delete_all(args)

    elif args.command == "info":
        model_info(args)

    elif args.command == "whoami":
        whoami(args)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()