def transform_data(entry):
    if 'category' in entry and isinstance(entry['category'], str):
        entry['category'] = entry['category'].upper()
    if 'value' in entry and isinstance(entry['value'], (int, float)):
        entry['value'] *= 10
    return entry
