from setuptools import setup

test_deps = [
    'pytest>=4',
    'pytest-cov>=2.6.0',
    'pytest-flake8',
]

setup(
    name='UBS',
    version='0.0.1',
    extras_require={
        'test': test_deps,
    },
    install_requires=[
        "tornado",
        "numpy",
        "requests",
        # "torch",
        "pandas",
        "scipy",
        # "redis",
        "pymysql",
        # 'pyzmq',
        # 'plotly',
        # 'kaleido',
        "xlrd==1.2.0",
        # "pyexcel-xls",
        # "openpyxl",
        "matplotlib",
        # "dataclasses",
        # "pnglatex",
        # "pillow>=6.2.0",
        # "aiofiles",
        # "html2image",
        # "imgkit"
    ],  # And any other dependencies foo needs
    entry_points={
    },
)
