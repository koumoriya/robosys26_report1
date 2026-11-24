#!/bin/bash

ng () {
	echo ${1}行目のテスト失敗
	res=1
}

res=0
out=$(python3 ./unitconv.py 120 mm cm)
[ "${out}" = 12.0 ] || ng "$LINENO"
[ "${res}" = 0 ] && echo OK
exit $res

