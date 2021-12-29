package anyid

import (
	"io"
	"fmt"
)

func WhoAreYou(w io.Writer) {
	fmt.Fprintln(
		w,
		(&foo{}).init().whoAreYou(),
		(&bar{}).init().whoAreYou(),
	)
}

type vtbl interface {
	name() string
}

type base struct {
	vtbl
}

type foo struct {
	base
}

type bar struct {
	base
}

func (self *base) whoAreYou() string {
	return self.name()
}

func (self *foo) name() string { return "Foo" }
func (self *bar) name() string { return "Bar" }

/* NO!
func (self *base) init() *base {
	self.vtbl = self
	return self
}
*/

// REQUIRED!
func (self *foo) init() *foo {
	self.vtbl = self
	return self
}

// REQUIRED!
func (self *bar) init() *bar {
	self.vtbl = self
	return self
}
