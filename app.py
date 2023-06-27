import pyodbc
import json
from flask import Flask, render_template, request
import os

app = Flask(__name__)


app.secret_key = 'your secret key'

server = 'mysqlserver-rv.database.windows.net'
username = 'azureuser'
password = 'Mavbgl@656'
database = 'demodb'
driver= '{ODBC Driver 18 for SQL Server}'

dir_path = os.path.dirname(os.path.realpath(__file__)) + '/tmp'
print(dir_path)
UPLOAD_FOLDER = dir_path
ALLOWED_EXTENSIONS = set(['txt', 'csv'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
conn = pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+',1433;DATABASE='+database+';UID='+username+';PWD='+ password+ ';Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
cur = conn.cursor()

# Route for the main page
@app.route('/')
def index():
    return render_template('index.html')

# Route for generating the chart
@app.route('/generate_chart', methods=['POST'])
def generate_chart():
    # Get the user-selected interval or attributes from the form

    selected_attributes = request.form.getlist('attributes')
    selected_plot = request.form.getlist('chart')

    print("Selected plot: ", selected_plot)
    # Connect to the database


    # Execute the SQL query
    query = "SELECT name, cost FROM datas;"
    print(query)
    cur.execute(query)

    # Fetch all rows
    rows = cur.fetchall()

    # Close the cursor and the connection


    # Prepare data for the selected attributes
    chart_data = []
    for row in rows:
        data_point = {}
        data_point['name'] = row[0]
        # data_point['cost'] = row[1]
        for i, attribute in enumerate(['cost']):
            if attribute in selected_attributes:
                data_point[attribute] = str(row[i+1])
        print("DATA: ",data_point)
        chart_data.append(data_point)
    chart_data = sorted(chart_data, key=lambda x: int(x['cost']))
    print("CHART DATA",chart_data)
    # Render the template with the chart data and selected attributes
    if (selected_plot[0] == 'ScatterPlot'):
        return render_template('chart.html', chart_data=json.dumps(chart_data), selected_attributes=selected_attributes)
    if (selected_plot[0] == 'BarChart'):
        return render_template('histplot.html', chart_data=json.dumps(chart_data), selected_attributes=selected_attributes)
    if (selected_plot[0] == 'PieChart'):
        return render_template('piechart.html', chart_data=json.dumps(chart_data), selected_attributes=selected_attributes)
    return render_template('retry.html')


@app.route('/largest', methods=['POST'])
def largest():
    largest = request.form.get('largest')
    selected_attributes = request.form.getlist('attributes')
    selected_plot = request.form.getlist('chart')

    print(largest)
    query = "select top " + largest +"cost from datas;"

    print(query)
    cur.execute(query)

    # Fetch all rows
    rows = cur.fetchall()

    chart_data = []
    for row in rows:
        data_point = {}
        data_point['name'] = row[0]
        # data_point['cost'] = row[1]
        for i, attribute in enumerate(['cost']):
            if attribute in selected_attributes:
                data_point[attribute] = str(row[i+1])
        print("DATA: ",data_point)
        chart_data.append(data_point)
    chart_data = sorted(chart_data, key=lambda x: int(x['cost']))
    print("CHART DATA",chart_data)
    # Render the template with the chart data and selected attributes

    return render_template('piechart.html', chart_data=json.dumps(chart_data), selected_attributes=selected_attributes)
    


if __name__ == '__main__':
    app.run()
