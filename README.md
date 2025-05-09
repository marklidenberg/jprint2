# jprint2

Print any Python object as JSON. Built on top of [jsons](https://github.com/ramonhagenaars/jsons) for formatting and [pygments](https://pygments.org/) for colorizing.

## Basic usage 

```python

from jprint2 import jprint, jformat, set_defaults

# - Print json

jprint({"name": "Mark", "age": 30}) # {"name": "Mark", "age": 30}

# - Keeps strings by default as is to preserve json objects

jprint("Mark") # Mark
jprint('{"name": "Mark"}') # {"name": "Mark"}
jprint('{"name": "Mark"}', keep_strings=False)  # "{\"name\": \"Mark\"}"

# - Set defaults of your liking

set_defaults(
	indent=2, 
	sort_keys=True
)

# - Format json

my_json_string = jformat({"name": "Mark", "age": 30})

# - Override defaults

jprint({"name": "🧙‍♂️", "age": 30}, ensure_ascii=True) # {"name": "\ud83e\uddd9\u200d\u2642\ufe0f", "age": 30}

```

![Example output](docs/jprint.png "Example output")

## License

MIT License

## Author

Mark Lidenberg [marklidenberg@gmail.com](mailto:marklidenberg@gmail.com)