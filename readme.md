Your goat project
readme for checkehr
Two versions of the TDD tutorial

At the terminal, try to use tmux
then attach a session called `checkEHR`
the session should be split into two panes
in each pane you need to activate the virtual environment `source venv/bin/activate`
in the left hand pane, then 

```bash
export FLASK_APP=app
export FLASK_DEBUG=1
flask run
```

in the right hand pane, then run your tests

```bash
pytest
python functional_tests.py
```

or run a flask shell instance

```bash
export FLASK_APP=app
export FLASK_DEBUG=1
flask shell
```

## Useful documentation

- http://selenium-python.readthedocs.io/index.html

## Non-localised todos

- [ ] @TODO: (2018-07-27) create a 'checkEHR' class that inherits from FlaskCloudant and has relevant properties; define the characteristics of your application in this class rather than in the db, then you can always change the backend db