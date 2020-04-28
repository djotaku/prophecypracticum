# Prophecy Practicum

[![Documentation Status](https://readthedocs.org/projects/prophecy-practicum/badge/?version=latest)](https://prophecy-practicum.readthedocs.io/en/latest/?badge=latest) ![Lint, PyTest, MyPy](https://github.com/djotaku/prophecypracticum/workflows/Lint,%20PyTest,%20MyPy/badge.svg)

Documentation at: https://prophecy-practicum.readthedocs.io/en/latest/

This package has two submodules: engine and web. Most of the logic should happen in the engine and the web will present submodule will provide the user interface (and maybe a JSON API)

engine.controller.py will have the admin commands so it will create engine.user.py Users. In the finished product this will be from an admin page in the web interface. Then those Users will then create engine.prophecy Prophecy objects. Again, in the finished product this will be done via the web interface.

Validation prior to web submodule creation will come from engine.controller.py unit tests. 

This project should follow https://www.semver.org principles:

Given a version number MAJOR.MINOR.PATCH, increment the:

    MAJOR version when you make incompatible API changes,

    MINOR version when you add functionality in a backwards compatible manner, and

    PATCH version when you make backwards compatible bug fixes.
