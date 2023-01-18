import utils
import read_csv
import charts


def run():
    country = input('Type Country =>')
    data = read_csv.read_csv('./app/data.csv')
    
    #Grafica de poblacion en formato de barras
    country_dict = utils.pupulation_by_country(data, country)
    population = utils.get_population(country_dict)
    labels = population.keys()
    values = population.values()
    charts.generate_bar_chart(labels= labels, values= values)
    
    # Grafica de porcentajes de poblacion mundial
    dict_pct = utils.get_percentages_population(data)
    labels_pct = dict_pct.keys()
    values_pct = dict_pct.values()
    charts.generate_pie_chart(labels= labels_pct, values= values_pct)
if __name__ == '__main__':
    run()
    
   