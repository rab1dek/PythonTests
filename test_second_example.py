def triangle_field(base, height):
    print((base * height)/2)

def test_triangle_field(capsys):
    base = 10
    height = 8

    triangle_field(base, height)
    out, err = capsys.readouterr()

    assert out == '40.0\n'