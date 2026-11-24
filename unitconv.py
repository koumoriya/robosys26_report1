#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 koumoriya
# SPDX-License-Identifier: MIT

import sys

units = {
	"mm":0.001,
	"cm":0.01,
	"m":1.0,
	"km":1000.0,
}

def convert(value, from_unit, to_unit):
	if from_unit not in units or to_unit not in units:
		raise ValueError("対応していない単位")

	result = value * units[from_unit] / units[to_unit]
	return result

if len(sys.argv) != 4:
	print("使い方：python3 unitconv.py 数値 変換前単位 変換後単位", file=sys.stderr)
	sys.exit(1)
try:
	value = float(sys.argv[1])
	from_unit = sys.argv[2]
	to_unit = sys.argv[3]

	result = convert(value, from_unit, to_unit)
	print(result)

except ValueError as e:
	print(e, file=sys.stderr)
	sys.exit
