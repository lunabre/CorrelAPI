from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
#import ast

import pandas as pd

app = Flask(__name__)
api = Api(app)


## API endpoints
class Values(Resource):
	# GET
	def get(self):
		data = pd.read_csv('var_values.csv')
		data = data.to_dict()
		return {'data':data}, 200



class Correls(Resource):
	
	def get(self):
		data = pd.read_csv('var_correlations.csv')
		data = data.to_dict()
		return {'data':data}, 200
	
	# POST with param = rolling_window	
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('correl_window', required = False)
		args = parser.parse_args()
		
		from correl_pkg.main import get_correl
		
		# try:
			# w_ = args['correl_window']
			# data = get_correl(w_)
		# except:
			# data = get_correl()
		w_ = int(args['correl_window'])
		data = get_correl(w_)
		data.to_csv('var_correlations.csv')
		data = data.to_dict()
		
		return {'data':data}, 200
	
api.add_resource(Values, '/values')
api.add_resource(Correls, '/correl')

if __name__ == '__main__':
    app.run()