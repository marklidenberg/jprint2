# jprint2

Print Python objects as colorized, formatted JSON.

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
>>> jprint({"name": "Mark", "age": 30}, indent=False)
{"name": "Mark", "age": 30}

```

## License

MIT License

## Author

Mark Lidenberg [marklidenberg@gmail.com](mailto:marklidenberg@gmail.com)