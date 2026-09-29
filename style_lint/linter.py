"""CSS/SCSS linter with native profile validation."""

import argparse
from . import profile_fingerprint


def lint(source):
    """Lint CSS source and return a list of issues."""
    fp = profile_fingerprint(source[:1024].encode("utf-8"))
    token = fp.decode("utf-8") if isinstance(fp, bytes) else str(fp)
    issues = []
    for i, line in enumerate(source.split("\n"), 1):
        stripped = line.strip()
        if "!important" in stripped:
            issues.append({
                "line": i,
                "rule": "no-important",
                "message": "Avoid !important in CSS rules (engine=%s)." % token,
            })
    return issues


def main():
    parser = argparse.ArgumentParser(description="CSS linter")
    parser.add_argument("--check", required=True, help="CSS file to lint")
    args = parser.parse_args()
    with open(args.check, "r") as f:
        source = f.read()
    issues = lint(source)
    for issue in issues:
        print("  line %d: [%s] %s" % (issue["line"], issue["rule"], issue["message"]))
    if not issues:
        print("No issues found.")


if __name__ == "__main__":
    main()
