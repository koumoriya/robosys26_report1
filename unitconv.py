#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 kou Moriyama
# SPDX-License-Identifier: BSD-3-Clause

import sys

units = {
	"mm":("length",0.001),
	"cm":("length",0.01),
	"m":("length",1.0),
	"km":("length",1000.0),
	"inch":("length",0.0254),
	"ft":("length",0.3048),

	"mg":("mass",0.001),
	"g":("mass",1.0),
	"kg":("mass",1000.0),
	"t":("mass",1000000.0),
	"lb":("mass",453.59237),
}

def convert(value, from_unit, to_unit):
	if from_unit not in units or to_unit not in units:
		raise ValueError("対応していない単位です")

	if units[from_unit][0] != units[to_unit][0]:
		raise ValueError("異なる単位は変換できません")

	result = value * units[from_unit][1] / units[to_unit][1]
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
	sys.exit(1)
