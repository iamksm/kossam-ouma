# Kossam Ouma
This is my portfolio


**Setting up Pre-Commit**

1. Install Pre-commit

       pip install pre-commit
       pre-commit --version

+ run pre-commit install to set up the git hook scripts


       pre-commit install


2. Ensure Hooks are Updated then run

+ Update your hooks to the latest version automatically by running pre-commit autoupdate. By default, this will bring the hooks to the latest tag on the default remote branch.


      pre-commit autoupdate


+ it's usually a good idea to run the hooks against all of the files when adding new hooks (usually pre-commit will only run on the changed files during git hooks)


      pre-commit run -vv --all-files

+ To run individual hooks use


      pre-commit run <hook_id>.


3. The pre-commit config file (.pre-commit-config.yaml) describes what repositories and hooks that are installed.Install black and set the default config file to be pyproject.toml. This will enable you to run black command before commiting your changes.

+ pip install black then check the version


      pip install black
      black --version


+ Then use our config file and run on gateway and tests


      black --config pyproject.toml integration_gateway/ tests/
