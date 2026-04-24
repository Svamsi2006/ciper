import sys


VALID_OPERATIONS = {"add", "sub", "mul", "div"}


def calculate(operation: str, first: float, second: float) -> float:
	if operation == "add":
		return first + second
	if operation == "sub":
		return first - second
	if operation == "mul":
		return first * second
	if operation == "div":
		if second == 0:
			raise ValueError("Division by zero is not allowed.")
		return first / second
	raise ValueError("Invalid operation. Use: add, sub, mul, div")


def read_number(prompt: str) -> float:
	while True:
		raw = input(prompt).strip()
		try:
			return float(raw)
		except ValueError:
			print("Please enter a valid number.")


def print_help() -> None:
	print("Calculator modes:")
	print("1) Interactive mode (default): python app.py")
	print("2) One-shot mode: python app.py <add|sub|mul|div> <num1> <num2>")
	print("Examples:")
	print("  python app.py add 10 5")
	print("  python app.py")


def run_one_shot(args: list[str]) -> int:
	if len(args) != 3:
		print("Usage: python app.py <add|sub|mul|div> <num1> <num2>")
		return 1

	operation = args[0].lower()
	if operation not in VALID_OPERATIONS:
		print("Invalid operation. Use: add, sub, mul, div")
		return 1

	try:
		first = float(args[1])
		second = float(args[2])
		result = calculate(operation, first, second)
	except ValueError as error:
		print(f"Error: {error}")
		return 1

	print(f"Result: {result}")
	return 0


def run_interactive() -> int:
	print("Docker Calculator (interactive)")
	print("Type add, sub, mul, div or type exit to quit.")

	while True:
		operation = input("Operation: ").strip().lower()

		if operation in {"exit", "quit", "q"}:
			print("Goodbye!")
			return 0

		if operation not in VALID_OPERATIONS:
			print("Invalid operation. Choose: add, sub, mul, div")
			continue

		first = read_number("First number: ")
		second = read_number("Second number: ")

		try:
			result = calculate(operation, first, second)
		except ValueError as error:
			print(f"Error: {error}")
			continue

		print(f"Result: {result}")


def main() -> int:
	args = sys.argv[1:]

	if len(args) == 0:
		return run_interactive()

	if len(args) == 1 and args[0] in {"-h", "--help"}:
		print_help()
		return 0

	return run_one_shot(args)


if __name__ == "__main__":
	raise SystemExit(main())
