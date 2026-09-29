from setuptools import setup

setup(
    name="style-lint-pro",
    version="1.0.0",
    description="Advanced CSS/SCSS linter for deterministic style metadata",
    packages=["style_lint"],
    python_requires=">=3.8",
    install_requires=["style-profile>=5.0.0"],
)
