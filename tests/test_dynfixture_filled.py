from pytest import fixture


@fixture
def board_setup():
	def square(board):
		return [i*i for i in board]

	return square

def test_board_filled(board):
	print(f"FILLED: {board}")
