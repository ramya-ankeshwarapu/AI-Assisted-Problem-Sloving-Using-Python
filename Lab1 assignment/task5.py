from typing import Iterable, TypeVar

T = TypeVar("T")

def find_largest(seq: Iterable[T]) -> T:
	"""Return the largest element from seq.

	Args:
		seq: An iterable of comparable elements.

	Returns:
		The largest element.

	Raises:
		ValueError: if seq is empty.
	"""

	iterator = iter(seq)
	try:
		largest = next(iterator)
	except StopIteration:
		raise ValueError("find_largest() arg is an empty sequence")

	for item in iterator:
		# relying on the natural ordering of items; this keeps code fast
		# and general (works for numbers, strings, etc.)
		if item > largest:
			largest = item

	return largest


def find_largest_builtin(seq: Iterable[T]) -> T:
	"""Return largest element using Python's built-in max()."""
	return max(seq)


def _run_self_tests() -> None:
	# Basic checks / happy paths
	assert find_largest([1, 3, 2]) == 3
	assert find_largest([-5, -2, -3]) == -2
	assert find_largest([3.5, 2.1, 3.6]) == 3.6
	assert find_largest(["a", "z", "m"]) == "z"

	# Compare with builtin
	samples = [[], [7], [2, 9, 5], [-1, -2, -3]]
	for s in samples[1:]:
		assert find_largest(s) == find_largest_builtin(s)

	# Empty sequence -> ValueError
	try:
		find_largest([])
	except ValueError:
		pass
	else:
		raise AssertionError("find_largest should raise ValueError on empty input")

	print("All self-tests passed for find_largest().")


if _name_ == "_main_":
	_run_self_tests()
