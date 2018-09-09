import datamigration


def test_simple():
    source = [(1, 1), (2, 3), (5, 8), (13, 21, 34)]
    output = []

    def loader():
        for data in source:
            yield data

    def process(data):
        return sum(data)

    def dumper(result):
        output.append(result)

    migrate = datamigration.Migrator(loader, process, dumper)

    migrate()

    assert output == [2, 5, 13, 68]
