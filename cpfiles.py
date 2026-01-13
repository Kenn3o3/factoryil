#!/usr/bin/env python3
import sys
import os


def choose_fence(text: str) -> str:
    """
    Choose a Markdown code fence (sequence of backticks) that doesn't appear in the text.
    Starts with ``` and adds more backticks if needed.
    """
    backticks = 3
    while "`" * backticks in text:
        backticks += 1
        # Safety cap (extremely unlikely to be needed)
        if backticks > 12:
            break
    return "`" * backticks


def read_file_text(path: str) -> str:
    """
    Read file as text trying a few encodings. Returns the decoded text.
    Raises the original exception if all attempts fail.
    """
    encodings_to_try = ["utf-8", "utf-8-sig", "utf-16", "latin-1"]
    last_err = None
    for enc in encodings_to_try:
        try:
            with open(path, "r", encoding=enc, errors="strict") as f:
                return f.read()
        except Exception as e:
            last_err = e
    # Fallback: read as binary and replace errors to avoid crashing on odd files
    try:
        with open(path, "rb") as f:
            return f.read().decode("utf-8", errors="replace")
    except Exception:
        if last_err:
            raise last_err
        raise


def normalize_path(p: str, base_dir: str) -> str:
    """
    Resolve path relative to base_dir (the directory of the list file) and return absolute, normalized path.
    """
    if not os.path.isabs(p):
        p = os.path.join(base_dir, p)
    return os.path.abspath(os.path.normpath(p))


def collect_entries_and_ignores(list_path: str):
    """
    Parse the list file into inclusion entries and ignore entries.
    Returns (entries, ignore_files, ignore_dirs), where entries are the raw lines (resolved to absolute paths),
    ignore_files is a set of absolute file paths, and ignore_dirs is a list of absolute dir paths (with os.sep-terminated).
    """
    with open(list_path, "r", encoding="utf-8", errors="replace") as f:
        raw_lines = f.readlines()

    base_dir = os.path.dirname(os.path.abspath(list_path))

    entries = []
    ignore_files = set()
    ignore_dirs = []

    for line in raw_lines:
        raw = line.rstrip("\n")
        s = raw.strip()
        if not s:
            continue  # skip empty
        if s.startswith("#"):
            continue  # allow comments in list

        lowered = s.lower()
        if lowered.startswith("except:"):
            path_part = s[len("except:"):].strip()
            if not path_part:
                continue
            abs_ignored = normalize_path(path_part, base_dir)
            # If it's clearly a dir path in filesystem, treat as dir; if file, treat as file.
            # If it doesn't exist, infer by trailing slash or common patterns; else default to dir if endswith os.sep.
            if os.path.isdir(abs_ignored) or path_part.endswith(("/", "\\")):
                # Normalize with trailing separator for prefix match
                dir_path = abs_ignored
                if not dir_path.endswith(os.sep):
                    dir_path = dir_path + os.sep
                ignore_dirs.append(dir_path)
            elif os.path.isfile(abs_ignored):
                ignore_files.add(abs_ignored)
            else:
                # If unknown, be conservative: if it has an extension, assume file; else assume dir
                if os.path.splitext(abs_ignored)[1]:
                    ignore_files.add(abs_ignored)
                else:
                    dir_path = abs_ignored
                    if not dir_path.endswith(os.sep):
                        dir_path = dir_path + os.sep
                    ignore_dirs.append(dir_path)
            continue

        # Regular entry
        abs_entry = normalize_path(s, base_dir)
        entries.append(abs_entry)

    return entries, ignore_files, ignore_dirs


def path_is_ignored(path: str, ignore_files: set, ignore_dirs: list) -> bool:
    """
    Return True if the absolute path is ignored by exact file match or by being inside an ignored directory.
    """
    apath = os.path.abspath(path)
    if apath in ignore_files:
        return True
    apath_dir_pref = apath
    # Ensure directory prefix matching uses trailing separator on ignored dirs
    for d in ignore_dirs:
        # d is guaranteed to end with os.sep
        if apath == d[:-1] or apath.startswith(d):
            return True
    return False


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print("Usage: python cpfiles.py filespaths.txt [output.txt]")
        print("  filespaths.txt: text file with one file or folder path per line")
        print("  output.txt: optional output path (default: prompt.txt)")
        print("  Lines starting with 'except:' define ignore paths (files or directories).")
        sys.exit(1)

    list_path = sys.argv[1]
    out_path = sys.argv[2] if len(sys.argv) >= 3 else "prompt.txt"

    if not os.path.isfile(list_path):
        print(f"Error: list file not found: {list_path}", file=sys.stderr)
        sys.exit(1)

    # Parse list: inclusions and ignores
    entries, ignore_files, ignore_dirs = collect_entries_and_ignores(list_path)

    if not entries:
        print("Warning: no paths found in the list.", file=sys.stderr)

    # Prepare to write output
    wrote_count = 0
    seen_files = set()  # avoid duplicate files

    def should_skip_file(path: str) -> bool:
        # Skip compiled Python files and other cache artifacts
        lower = path.lower()
        return lower.endswith(".pyc") or lower.endswith(".pyo")

    def write_one_file(path: str, out_handle):
        nonlocal wrote_count
        try:
            content = read_file_text(path)
        except Exception as e:
            print(f"Warning: could not read {path}: {e}", file=sys.stderr)
            return
        fence = choose_fence(content)
        out_handle.write(f"{path}:\n")
        out_handle.write(f"{fence}\n")
        out_handle.write(content)
        if not content.endswith("\n"):
            out_handle.write("\n")
        out_handle.write(f"{fence}\n\n")
        wrote_count += 1

    with open(out_path, "w", encoding="utf-8") as out:
        out.write("Here are the files for my simulation environment setup:\n")

        for entry in entries:
            # Skip if the entry itself is ignored
            if path_is_ignored(entry, ignore_files, ignore_dirs):
                continue

            if os.path.isfile(entry):
                if should_skip_file(entry):
                    continue
                abs_path = os.path.abspath(entry)
                if abs_path in seen_files:
                    continue
                if path_is_ignored(abs_path, ignore_files, ignore_dirs):
                    continue
                seen_files.add(abs_path)
                write_one_file(entry, out)

            elif os.path.isdir(entry):
                # Walk directory recursively; sort for deterministic order
                for root, dirs, files in os.walk(entry):
                    # Exclude __pycache__ (and optionally other hidden dirs)
                    dirs[:] = [d for d in dirs if d != "__pycache__"]
                    # Apply ignore filters to dirs to avoid descending into them
                    filtered_dirs = []
                    for d in dirs:
                        full_dir = os.path.abspath(os.path.join(root, d))
                        if path_is_ignored(full_dir, ignore_files, ignore_dirs):
                            continue
                        filtered_dirs.append(d)
                    dirs[:] = filtered_dirs

                    dirs.sort()
                    files.sort()
                    for fname in files:
                        # Skip compiled python files
                        if fname.lower().endswith((".pyc", ".pyo")):
                            continue
                        fpath = os.path.join(root, fname)
                        # Only process regular files
                        if not os.path.isfile(fpath):
                            continue
                        abs_path = os.path.abspath(fpath)
                        if abs_path in seen_files:
                            continue
                        if path_is_ignored(abs_path, ignore_files, ignore_dirs):
                            continue
                        seen_files.add(abs_path)
                        write_one_file(fpath, out)
            else:
                print(f"Warning: skipping missing path: {entry}", file=sys.stderr)

    if wrote_count > 0:
        print(f"Wrote {out_path} with {wrote_count} files.")
    else:
        print("No files were written. Check warnings above.", file=sys.stderr)


if __name__ == "__main__":
    main()
