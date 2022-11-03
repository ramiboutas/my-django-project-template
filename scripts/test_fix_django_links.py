from __future__ import annotations

from scripts.fix_django_links import main


def test_success(capsys, tmp_path):
    example = tmp_path / "example.md"
    example.write_text("See https://docs.djangoproject.com/en/stable/ref/utils/")

    exit_code = main([str(example)])

    assert exit_code == 1
    out, err = capsys.readouterr()
    assert out == f"Fixing {example}\n"
    assert err == ""
    assert (
        example.read_text() == "See https://docs.djangoproject.com/en/stable/ref/utils/"
    )


def test_no_change(capsys, tmp_path):
    example = tmp_path / "example.md"
    example.write_text("See https://docs.djangoproject.com/en/stable/ref/utils/")

    exit_code = main([str(example)])

    assert exit_code == 0
    out, err = capsys.readouterr()
    assert out == ""
    assert err == ""
    assert (
        example.read_text() == "See https://docs.djangoproject.com/en/stable/ref/utils/"
    )


def test_multiple_files(capsys, tmp_path):
    before = "See https://docs.djangoproject.com/en/stable/ref/utils/"
    example1 = tmp_path / "example1.md"
    example1.write_text(before)
    example2 = tmp_path / "example2.md"
    example2.write_text(before)

    exit_code = main([str(example1), str(example2)])

    assert exit_code == 1
    out, err = capsys.readouterr()
    assert out == f"Fixing {example1}\nFixing {example2}\n"
    assert err == ""
    after = "See https://docs.djangoproject.com/en/stable/ref/utils/"
    assert example1.read_text() == after
    assert example2.read_text() == after
