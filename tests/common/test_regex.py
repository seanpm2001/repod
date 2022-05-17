from re import Match, fullmatch

from repod.common import regex


def test_absolute_dir(absolute_dir: str) -> None:
    assert isinstance(fullmatch(regex.ABSOLUTE_DIR, absolute_dir), Match)


def test_invalid_absolute_dir(invalid_absolute_dir: str) -> None:
    assert not isinstance(fullmatch(regex.ABSOLUTE_DIR, invalid_absolute_dir), Match)


def test_architectures(arch: str) -> None:
    assert isinstance(fullmatch(regex.ARCHITECTURES, arch), Match)


def test_invalid_architectures(arch: str) -> None:
    assert not isinstance(fullmatch(regex.ARCHITECTURES, "foo"), Match)


def test_buildenvs(buildenv: str) -> None:
    assert isinstance(fullmatch(regex.BUILDENVS, buildenv), Match)


def test_invalid_buildenvs(invalid_buildenv: str) -> None:
    assert not isinstance(fullmatch(regex.BUILDENVS, invalid_buildenv), Match)


def test_email(email: str) -> None:
    assert isinstance(fullmatch(regex.EMAIL, email), Match)


def test_invalid_email(invalid_email: str) -> None:
    assert not isinstance(fullmatch(regex.EMAIL, invalid_email), Match)


def test_epoch(epoch: str) -> None:
    assert isinstance(fullmatch(regex.EPOCH, epoch), Match)


def test_invalid_epoch(invalid_epoch: str) -> None:
    assert not isinstance(fullmatch(regex.EPOCH, invalid_epoch), Match)


def test_options(option: str) -> None:
    assert isinstance(fullmatch(regex.OPTIONS, option), Match)


def test_invalid_options(invalid_option: str) -> None:
    assert not isinstance(fullmatch(regex.OPTIONS, invalid_option), Match)


def test_package_name(package_name: str) -> None:
    assert isinstance(fullmatch(regex.PACKAGE_NAME, package_name), Match)


def test_invalid_package_name(invalid_package_name: str) -> None:
    assert not isinstance(fullmatch(regex.PACKAGE_NAME, invalid_package_name), Match)


def test_packager_name(packager_name: str) -> None:
    assert isinstance(fullmatch(regex.PACKAGER_NAME, packager_name), Match)


def test_invalid_packager_name(invalid_packager_name: str) -> None:
    assert not isinstance(fullmatch(regex.PACKAGER_NAME, invalid_packager_name), Match)


def test_pkgrel(pkgrel: str) -> None:
    assert isinstance(fullmatch(regex.PKGREL, pkgrel), Match)


def test_invalid_pkgrel(invalid_pkgrel: str) -> None:
    assert not isinstance(fullmatch(regex.PKGREL, invalid_pkgrel), Match)


def test_sha256(sha256sum: str) -> None:
    assert isinstance(fullmatch(regex.SHA256, sha256sum), Match)
    assert not isinstance(fullmatch(regex.SHA256, sha256sum[0:-2]), Match)


def test_version(version: str) -> None:
    assert isinstance(fullmatch(regex.VERSION, version), Match)


def test_invalid_version(invalid_version: str) -> None:
    assert not isinstance(fullmatch(regex.VERSION, invalid_version), Match)