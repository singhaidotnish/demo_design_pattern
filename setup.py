import setuptools

from setup_utils import get_requirements, get_dev_requirements

requirements = get_requirements()
dev_requirements = get_dev_requirements()

setuptools.setup(
    name='demo_design_pattern',
    version='0.1',
    description='demo of simple api',
    python_requires='==3.9.*',
    package_dir={"": "src"},
    packages=setuptools.find_packages("src"),
    install_requires=[requirements],
    extras_require={"dev": [dev_requirements]}
)