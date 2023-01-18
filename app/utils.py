def get_population(country_dict):
    return {key[:4]: int(value) for (key, value) in country_dict.items() if 'Population' in key and 'World' not in key}


def pupulation_by_country(data, country):
    return list(filter(lambda item: item['Country/Territory'] == country, data))[0]


def get_percentages_population(data):
    final_dict = {country['Country/Territory']:float(country['World Population Percentage']) for country in data}
    return final_dict
