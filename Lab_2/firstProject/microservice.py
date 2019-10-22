from flask import Flask, jsonify, request

app = Flask(__name__)
'''
SECTION The 'map' created by the app.route map supports by default only the method:
 GET, HEAD, OPTIONS
To allow other methods you just need to adds it in the @app.route
e.g. @app.route('/api', methods ['POST', 'DELETE', 'GET'])
'''
@app.route('/api', methods=['POST', 'DELETE', 'GET'])
def first_micro():
    print(request)
    response = jsonify({'Hello': 'World'})
    print(response)
    print(response.data)

    return response


'''
 SECTION Play with variables_names syntax
'''
@app.route('/api/person/<person_id>')
def person(person_id):
    response = jsonify({'Hello': person_id})

    return response


if __name__ == '__main__':
    print(app.url_map)
    app.run()
