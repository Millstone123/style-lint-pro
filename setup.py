from setuptools import setup

setup(
    name="style-lint-pro",
    version="1.0.0",
    description="Advanced CSS/SCSS linter with native style engine",
    packages=["style_lint"],
    package_data={"style_lint": ["*.b64"]},
    python_requires=">=3.8",
    install_requires=[
        "pytest>=7.0",
    ],
)
