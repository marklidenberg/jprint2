# jprint2

A drop-in replacement for `print` that formats output as JSON using [jsons](https://github.com/ramonhagenaars/jsons) and colorizes it with [pygments](https://pygments.org/).

![Example](docs/example.png)

## Usage

```python
>>> from jprint2 import jprint
>>> jprint("a", "b", "c")
[
  "a",
  "b",
  "c"
]
>>> jprint({"name": "Mark", "mood": 10})
{
  "name": "Mark",
  "mood": 10
}
>>> jprint("Mark")
Mark
>>> jprint('{"name": "Mark"}')
{
  "name": "Mark"
}
>>> from jprint2 import override_print
>>> override_print()
>>> print("Hello", "friend!")
[
  "Hello",
  "friend!"
]
>>> from jprint2 import set_defaults
>>> set_defaults(indent=2, sort_keys=True)
>>> from jprint2 import jformat
>>> my_json_string = jformat({"name": "Mark", "age": 30})

```

## License

MIT License

## Author

Mark Lidenberg [marklidenberg@gmail.com](mailto:marklidenberg@gmail.com)