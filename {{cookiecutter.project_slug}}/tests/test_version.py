import {{ cookiecutter.project_slug }} as p


def test_version():
    assert len(p.version) > 0

