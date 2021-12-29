#!/usr/bin/env python3

_ODDMOD = r'999---'  # /\w[\w-]*/. used as mod names in */go.mod. safe?


def main():
    from os.path import relpath  # wiser than Path.relative_to
    from pathlib import Path

    seen, pkgs = set(), []
    base = Path(__file__).resolve().parent
    base = Path(relpath(base, Path.cwd()))

    def report(todo):
        from sys import stderr
        print(r'+ %s' % todo, file=stderr)
    def rm(pathobj):
        report(r'rm %s' % pathobj)
        try:
            pathobj.unlink()
        except FileNotFoundError:
            pass
    def call(command, cwd):
        from subprocess import call
        report(r'%(cwd)s$ %(command)s' % locals())
        status = call(command, shell=True, cwd=cwd)
        if status != 0:
            raise SystemExit(status)

    for y in sorted(base.glob(r'**/*.go')):
        y = y.parent
        if y in seen:
            continue
        seen.add(y)
        pkgs.append(y)
        rm(y / r'go.mod')
        call(r'go mod init %s' % _ODDMOD, cwd=y)

    pkg0 = pkgs[0]
    (pkg0 / r'go.mod').touch()
    impl = pkg0.name
    for y in pkgs[1:]:
        call(r'go mod edit -replace 0=../%s' % impl, cwd=y)
        call(r'go mod tidy', cwd=y)
    call(r'go run .', cwd=pkgs[1])
    call(r'go test ./...', cwd=pkgs[2])


if __name__ == r'__main__':
    main()
