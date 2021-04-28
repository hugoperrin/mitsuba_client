# mitsuba_client module

Python client for Mitsuba renderer designed ro automate certain routine tasks.
This will wrap the mitsuba renderer python bindings with an API tailored for my other other projects.

For dependencies, they are specified with poetry's pyproject.toml.

We recommend installing it in a fresh python environment:

``` bash
pip install pip --upgrade; pip install poetry
poetry install
```

To allow mitsuba bindings to work, you'll need to compile it the right way.

Follow the tutorial there, but be mindful of the intricacies of the integration to the right pyenv. It will not create any wheel to install it with, and therefore if you do not want to use the python global setting, you will need to adjust one step of the process.

For Linux, activate your python environment before compiling, and instead of doing:

``` bash
cmake -GNinja ..
```

You will need to do instead:

``` bash
 cmake -GNinja .. -DPYTHON_EXECUTABLE:FILEPATH=$(which python)
```

This will ensure it targets the right environment.
To enable auto completion for it inside of your IDE, launch the idea with the right paths sourced.
Changes to the mitsuba library must be done to enable full autocompletion however as most IDE do not do the kind of dynamic resolve needed.
This module, by wrapping it all ensures that we can have autocomplete in other projects though.
