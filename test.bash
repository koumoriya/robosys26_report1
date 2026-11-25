#!/bin/bash
# SPDX-FileCopyrightText: 2026 kou Moriyama
# SPDX-License-Identifier: BSD-3-Clause

ng () {
	echo ${1}行目のテスト失敗
	res=1
}

res=0

out=$(./unitconv.py 120 mm cm)
[ "${out}" = 12.0 ] || ng "$LINENO"

out=$(./unitconv.py 1 inch mm)
[ "${out}" = 25.4 ] || ng "$LINENO"

out=$(./unitconv.py 1 ft cm)
[ "${out}" = 30.48 ] || ng "$LINENO"

err=$(./unitconv.py 120 mm yd 2>&1)
status=$?
test "$status" -ne 0 || ng "$LINENO"
test -n "$err" || ng "$LINENO"

err=$(./unitconv.py abc mm cm 2>&1)
status=$?
test "$status" -ne 0 || ng "$LINENO"
test -n "$err" || ng "$LINENO"

err=$(./unitconv.py 120 mm 2>&1)
status=$?
test "$status" -ne 0 || ng "$LINENO"
test -n "$err" || ng "$LINENO"

[ "${res}" = 0 ] && echo OK
exit $res

