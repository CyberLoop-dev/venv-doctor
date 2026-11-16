#!/usr/bin/env python3
"""Diagnose the active Python interpreter and virtual environment."""
import argparse
import importlib.util
import json
import os
import site
import subprocess
import sys
import sysconfig


def diagnose(prefix, base_prefix, active):
    issues = []
    in_venv = os.path.normcase(os.path.realpath(prefix)) != os.path.normcase(os.path.realpath(base_prefix))
    if not in_venv:
        issues.append("Python is not running inside a virtual environment")
    if active:
        active_path = os.path.normcase(os.path.realpath(active))
        prefix_path = os.path.normcase(os.path.realpath(prefix))
        if active_path != prefix_path:
            issues.append("VIRTUAL_ENV does not match the running interpreter prefix")
    return in_venv, issues


def build_report():
    active = os.environ.get("VIRTUAL_ENV")
    in_venv, issues = diagnose(sys.prefix, sys.base_prefix, active)
    pip_available = importlib.util.find_spec("pip") is not None
    pip_result = subprocess.run(
        [sys.executable, "-m", "pip", "--version"],
        capture_output=True, text=True, timeout=5, check=False
    )
    if pip_result.returncode != 0:
        issues.append("python -m pip is unavailable or failed")
    try:
        site_paths = site.getsitepackages()
    except AttributeError:
        site_paths = []
    return {
        "python_executable": sys.executable,
        "python_version": sys.version.split()[0],
        "prefix": sys.prefix,
        "base_prefix": sys.base_prefix,
        "virtual_environment_active": in_venv,
        "VIRTUAL_ENV": active,
        "pip_module_available": pip_available,
        "pip_version_output": pip_result.stdout.strip() or pip_result.stderr.strip(),
        "purelib": sysconfig.get_paths().get("purelib"),
        "site_packages": site_paths,
        "issues": issues
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    try:
        report = build_report()
    except (OSError, subprocess.SubprocessError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(f"Python: {report['python_version']}")
        print(f"Executable: {report['python_executable']}")
        print(f"Virtual environment: {'active' if report['virtual_environment_active'] else 'not active'}")
        print(f"pip: {report['pip_version_output'] or 'unavailable'}")
        print(f"Purelib: {report['purelib']}")
        for issue in report["issues"]:
            print(f"warning: {issue}")
        if not report["issues"]:
            print("No common environment issues detected.")
    return 1 if report["issues"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
