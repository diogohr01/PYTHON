import mysql.connector
from flask import Flask, jsonify, request

mydb = mysql.connector.connect(
    host='127.17.0.1',
    user='diogo',
    password='9745',
    database='livraria',
    port='3307'
    
)

app = Flask(__name__)


'''livros = [
    {
        'id': 1,
        'titulo': 'Mal amado',
        'autor': 'carazinho',
    },
    {
        'id': 2,
        'titulo': 'Mal amado 2',
        'autor': 'carazinho 2',
    },
    {
        'id': 3,
        'titulo': 'Mal amado 3',
        'autor': 'carazinho 3',
    }
]'''

#consultar todos os livros
@app.route('/livros', methods=['GET'])
def obter_livros():
    my_cursor = mydb.cursor()
    my_cursor.execute('SELECT * FROM livros')
    todos_livros = my_cursor.fetchall()
    livros = []
    for livro in todos_livros:
        livros.append({
            'id': livro[0],
            'titulo': livro[1],
            'autor': livro[2]
        })
    return jsonify(livros)

#consultar livro por id
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    my_cursor = mydb.cursor()
    my_cursor.execute('SELECT * FROM livros WHERE id = %s', (id,))
    livro = my_cursor.fetchone()
    if livro:
        return jsonify({
            'id': livro[0],
            'titulo': livro[1],
            'autor': livro[2]
        })
    else:
        return jsonify({'mensagem': 'Livro não encontrado'}), 404


if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)

#consultar por id
'''
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
    return jsonify({'mensagem': 'Livro não encontrado'}), 404

#mudar algum livro 
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)    
            return jsonify(livros[indice])
   
 #criar novo livro
 
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():   
     novo_livro = request.get_json()
     livros.append(novo_livro)
     return jsonify(livros)
     
#deletar um livro    
@app.route('/livros', methods=['DELETE']) 
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
            
        return jsonify(livros)
 
 
if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)
    '''