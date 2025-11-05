def reverse_string(s: Any) -> str:
	"""Return the reverse of the given value's string representation.

	Args:
		s: Any object that will be converted to a string and reversed.

	Returns:
		The reversed string.

	Examples:
		>>> reverse_string('hello')
		'olleh'
	"""
	# Coerce to str to handle non-string inputs safely, then reverse.
	return str(s)[::-1]


if _name_ == "_main_":
	# Quick demonstration and simple self-checks.
	examples = ["hello", "", "A", "racecar", 12345]
	# Basic assertions (act as tiny tests):
	assert reverse_string('abc') == 'cba'
	assert reverse_string('') == ''
	assert reverse_string(123) == '321'

	print("Demo: reverse_string outputs")
	for e in examples:
		print(f"Original: {e!r} -> Reversed: {reverse_string(e)!r}")
