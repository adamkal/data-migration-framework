# Data Migration Framework

Data Migration Framework provides a framework for doing all sorts of data
manipulation operations at a larger scale.

Quite often a living project requires some kind of modification on a large set
of data. Usually the modification operation itself is quite simple but a lot of
work needs to be put into managing the data, splitting it up into chunks,
distributing or providing some presentation or monitoring.

Typical flow would be

1. Obtain data
2. Process data
3. Output data

```python

def reader():
    with open('source.txt') as f:
        for line in f:
            yield f


def processor(line):
    return len(line)


def writer(result, source=None):
    with open('output.txt', 'wa') as f:
        f.writeline(f'"{source}" has f{result} characters')


migrate = DataMigrator(reader, processor, writer)

migrate()

```

## FAQ

### How is this different from ETL?
