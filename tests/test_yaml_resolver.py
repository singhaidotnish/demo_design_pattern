"""
Testing the yaml resolver
"""

import pytest

# Local imports
from bot_common import yaml_resolver
from bot_common.exceptions import YAMLResolveError

########################################################################
#
# Fixtures
#
########################################################################

@pytest.fixture(scope="function")
def config_files(tmpdir):
    config_dir = tmpdir.mkdir("sub")

    site_config = config_dir.join("site_config.yaml")
    site_config.write("""
srv:
    port: 80
    """)

    client_config = config_dir.join("client_config.yaml")
    client_config.write("""
srv:
    port: 82
    """)

    show_config = config_dir.join("show_config.yaml")
    show_config.write("""
srv:
    port: 83
    """)

    shot_config = config_dir.join("shot_config.yaml")
    shot_config.write("""
srv:
    port: 84
    """)

    bad_config = config_dir.join("bad_config.yaml")
    bad_config.write("""
srv:
    port: 84
$
    """)

    return [site_config.strpath,
            client_config.strpath,
            show_config.strpath,
            shot_config.strpath,
            bad_config.strpath]

def test_config_files(config_files):
    site, client, show, shot, bad = config_files

    result = yaml_resolver.resolve([site, client, show, shot])
    assert result['srv']['port'] == 84

    result = yaml_resolver.resolve([site])
    assert result['srv']['port'] == 80

    result = yaml_resolver.resolve([client, shot, show])
    assert result['srv']['port'] == 83

def test_bad_config_files(config_files):
    site, client, show, shot, bad = config_files

    with pytest.raises(YAMLResolveError):
        yaml_resolver.resolve([site, bad, client, show, shot])
