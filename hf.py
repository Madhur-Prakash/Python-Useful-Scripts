import argparse
import os
import subprocess
import sys
from pathlib import Path

def run_cmd(cmd):
    """Run shell command"""
    try:
        subprocess.run(cmd, check=True)
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
    run_cmd(["huggingface-cli", "scan-cache"])

def show_size(args):
    cache = get_hf_cache()
    print(f"📁 Cache Location: {cache}")
    if os.name == "nt":  # Windows
        run_cmd(["powershell", "-Command", 
                f"(Get-ChildItem '{cache}' -Recurse | Measure-Object -Property Length -Sum).Sum / 1GB"])

def search_models(args):
    run_cmd(["huggingface-cli", "search", "models", args.query])

def download_model(args):
    cmd = [
        "huggingface-cli",
        "download",
        args.model
    ]
    if args.resume:
        cmd.append("--resume-download")
    run_cmd(cmd)

def delete_model(args):
    """Delete a specific model from cache using Python"""
    import shutil
    
    cache = get_hf_cache()
    hub_path = Path(cache) / "hub"
    
    # Convert model name to cache format (e.g., sentence-transformers/all-MiniLM-L6-v2 -> models--sentence-transformers--all-MiniLM-L6-v2)
    model_cache_name = "models--" + args.model.replace("/", "--")
    model_path = hub_path / model_cache_name
    
    if not model_path.exists():
        print(f"❌ Model not found in cache: {args.model}")
        print(f"   Looking for: {model_path}")
        print("\n💡 Use 'list' command to see cached models")
        sys.exit(1)
    
    # Get size before deletion
    total_size = sum(f.stat().st_size for f in model_path.rglob('*') if f.is_file())
    size_gb = total_size / (1024**3)
    
    if not args.yes:
        print(f"⚠️  About to delete: {args.model}")
        print(f"   Location: {model_path}")
        print(f"   Size: {size_gb:.2f} GB")
        confirm = input("\nAre you sure? Type 'yes' to continue: ")
        if confirm.lower() != 'yes':
            print("❌ Deletion cancelled")
            return
    
    try:
        shutil.rmtree(model_path)
        print(f"✅ Successfully deleted {args.model} ({size_gb:.2f} GB freed)")
    except Exception as e:
        print(f"❌ Error deleting model: {e}")
        sys.exit(1)

def delete_interactive(args):
    """Interactive deletion using huggingface-cli TUI"""
    print("🔍 Opening interactive cache deletion tool...")
    run_cmd(["huggingface-cli", "delete-cache"])

def delete_all(args):
    """Delete entire HF cache"""
    import shutil
    
    cache = get_hf_cache()
    hub_path = Path(cache) / "hub"
    
    if not hub_path.exists():
        print("❌ No cache found")
        return
    
    # Calculate total size
    total_size = sum(f.stat().st_size for f in hub_path.rglob('*') if f.is_file())
    size_gb = total_size / (1024**3)
    
    print(f"⚠️  WARNING: This will delete ALL cached models!")
    print(f"   Location: {hub_path}")
    print(f"   Total size: {size_gb:.2f} GB")
    
    if not args.yes:
        confirm = input("\nAre you sure? Type 'yes' to continue: ")
        if confirm.lower() != 'yes':
            print("❌ Deletion cancelled")
            return
    
    try:
        shutil.rmtree(hub_path)
        hub_path.mkdir(parents=True, exist_ok=True)
        print(f"✅ Successfully deleted all models ({size_gb:.2f} GB freed)")
    except Exception as e:
        print(f"❌ Error deleting cache: {e}")
        sys.exit(1)

def model_info(args):
    run_cmd(["huggingface-cli", "repo", "info", args.model])

def whoami(args):
    run_cmd(["huggingface-cli", "whoami"])

# ---------------- Main ---------------- #

def main():
    parser = argparse.ArgumentParser(
        description="🔥 HF CLI Helper (hf tool)"
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
    d = sub.add_parser("download", help="Download model to default HF cache")
    d.add_argument("model", help="Model name (e.g., meta-llama/Llama-2-7b)")
    d.add_argument("--resume", action="store_true", help="Resume incomplete download")

    # delete (specific model)
    dm = sub.add_parser("delete", help="Delete a specific model from cache")
    dm.add_argument("model", help="Model name (e.g., sentence-transformers/all-MiniLM-L6-v2)")
    dm.add_argument("-y", "--yes", action="store_true", help="Skip confirmation prompt")

    # delete-interactive
    sub.add_parser("delete-interactive", help="Interactive cache deletion (TUI)")

    # delete-all
    da = sub.add_parser("delete-all", help="Delete entire HF cache (all models)")
    da.add_argument("-y", "--yes", action="store_true", help="Skip confirmation prompt")

    # info
    i = sub.add_parser("info", help="Show model information")
    i.add_argument("model", help="Model name")

    # whoami
    sub.add_parser("whoami", help="Show logged-in HuggingFace user")

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