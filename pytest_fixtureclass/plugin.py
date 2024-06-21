from pytest import fixture
from makefun import create_function


def fixtureclass(cls: type):
    fixture_names = [name for name, _ in cls.__annotations__.items()]

    signature_params = ", ".join(fixture_names)
    setup_fixtures_signature = f"_auto_setup_fixtures(self, {signature_params})"

    def setup_fixtures_impl(self, **kwargs):
        for argname, argvalue in kwargs.items():
            setattr(self, argname, argvalue)

    _auto_setup_fixtures = create_function(
        setup_fixtures_signature, setup_fixtures_impl
    )
    _auto_setup_fixtures = fixture(_auto_setup_fixtures, autouse=True)

    setattr(cls, "_auto_setup_fixtures", _auto_setup_fixtures)
    return cls
