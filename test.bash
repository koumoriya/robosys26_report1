#!/bin/bash

ng () {
	echo ${1}行目のテスト失敗
	res=1
}

res=0

out=$(./unitconv.py 120 mm cm)
[ "${out}" = 12.0 ] || ng "$LINENO"

err=$(./unitconv.py 120 mm inch 2>&1)
status=$?
test "$status" -ne 0 || ng "$LINENO"
test -n "$err" || ng "$LINENO"

err=$(./unitconv.py abc mm cm 2>&1)
status=$?
test "$status" -ne 0 || ng "$LINENO"
test -n "$err" || ng "$LINENO"

[ "${res}" = 0 ] && echo OK
exit $res

