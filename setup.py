"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['main.py']
DATA_FILES = []
OPTIONS = {'argv_emulation': True,
           'iconfile': './icon.icns'}

setup(
    app=APP,
    name="Odoo Client",
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
