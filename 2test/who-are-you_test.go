package anyid

import (
	"bytes"
	"testing"
	"github.com/stretchr/testify/assert"
	z "0"
)

func Test0(t *testing.T) {
	var b bytes.Buffer
	z.WhoAreYou(&b)
	const expected = "Foo Bar\n"
	actual := b.String()
	assert.Equal(t, expected, actual)
}
