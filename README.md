# A Golang Demo: Virtual Method Dispatching (simplest)

This demo shows you a **Template Method Pattern** of the simplest form in Go.

**Virtual Method Dispatching** in Go is not so trivial.
I hope this demo helps you understand the how.

1. [0impl/who-are-you.go](0impl/who-are-you.go)
   - one interface, one base struct, two derived structs
   - method defs for these structs
1. [1demo/who-are-you-demo.go](1demo/who-are-you-demo.go)
   - main() that prints the output from the template method to the stdout
1. [2test/who-are-you_test.go](2test/who-are-you_test.go)
   - Test0() that tests the output from the template method

## [demo.py](demo.py)

This Python program does:
1. create:
   1. 0impl/go.mod (empty)
   1. 1demo/go.mod
   1. 2test/go.mod
1. run 1demo/who-are-you-demo.go
1. run 2test/who-are-you_test.go

## Running from GUI

.vscode/*.json are ready for you.

## FYI

https://github.com/x19290/go-elementary.pkg-mod.git
