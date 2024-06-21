from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

#Load type effectiveness data
with open(r'C:\Users\Zach\Desktop\PokeRouge\PokeRogue-Helper\Pokemon-weakness-calculator\types_defending.json') as f:
    type_data = json.load(f)

@app.route('/')
def index():
        types = list(type_data.keys())
        return render_template('index.html',types=types)

@app.route('/calculate', methods=['POST'])
def calculate():
      types = request.json.get('types',[])
      result = {"2x": set(), "1x": set(), "0.5x": set(), "0x": set()}

      for t in types:
            for effectiveness, affected_types in type_data[t].items():
                  result[effectiveness].update(affected_types)
    
      return jsonify({k: list(v) for k,v in result.items()})

if __name__ == '__main__':
      app.run(debug=True)