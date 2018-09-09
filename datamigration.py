def Migrator(source, processor, output):
    def migrator():
        for item in source():
            output(processor(item))

    return migrator
