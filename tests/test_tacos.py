import glob

def test_recipes_exist():
    # at least one recipe file must be present
    assert len(glob.glob("tacos_*.txt")) >= 1

def test_recipes_not_empty():
    for path in glob.glob("tacos_*.txt"):
        with open(path, encoding="utf-8") as f:
            assert f.read().strip() != "", path + " is empty"

def test_ouledfayet_has_tortilla():
    with open("tacos_ouledfayet.txt", encoding="utf-8") as f:
        assert "pain tortilla" in f.read()
