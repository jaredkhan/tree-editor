from setuptools import find_packages, setup

setup(
    name="tree-editor",
    version="0.1.0",
    author="Jared Khan",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    setup_requires=[],
    install_requires=[],
    python_requires=">3.6",
    entry_points={
        'console_scripts': ['tree-edit=tree_editor:main'],
    }
)
