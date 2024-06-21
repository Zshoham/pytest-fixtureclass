from pytest import fixture


def default_board_setup(board):
	return [i + 1 for i in board]


def pytest_generate_tests(metafunc):
	for name in metafunc.fixturenames:
		import ipdb; ipdb.set_trace()
		if name == "board_setup" and "board_setup" not in metafunc._arg2fixturedefs:
			metafunc.parametrize(name, [default_board_setup])
	

@fixture
def __base_board__():
	return [1, 2, 3, 4]

@fixture
def board(__base_board__, board_setup):
	return board_setup(__base_board__)

