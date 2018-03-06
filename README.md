# orbistats

## Getting Started

Copy the `orbi` directory into your python project.

## Example

```python
from orbi import orbi

while True:
    # Take a sample of the stats
    first_stats_dict = orbi.statistics(orbi_username, orbi_password)
    first_numbers_dict = {k: float(v) for k, v in first_stats_dict.iteritems() if is_number(v)}

    # After a short time, take another sample
    time.sleep(1)
    second_stats_dict = orbi.statistics(orbi_username, orbi_password)
    second_numbers_dict = {k: float(v) for k, v in second_stats_dict.iteritems() if is_number(v)}

    # Compute how much each stat has changed
    diff_dict = {k: (second_numbers_dict[k] - first_numbers_dict[k]) for k, v in first_numbers_dict.iteritems()}

    # Do something with the stats...
    print diff_dict
```