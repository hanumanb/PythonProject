"""Generators are memory-efficient for large streams."""
def read_in_batches(items, batch_size):
    for start in range(0, len(items), batch_size):
        yield items[start:start + batch_size]

records = range(1, 11)
for batch in read_in_batches(list(records), 3):
    print("Batch:", batch)
