from flask import Flask, request, jsonify, render_template, json
from main import ler_dados, autualizar_nota, criar_novo_usuario_e_nota, deletar_usuario
from tabelas import Usuario, Nota

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        data = request.get_data()
        usuario_e_nota = json.loads(data)

        user = Usuario(
                        nome = usuario_e_nota["usuario"],
                        email = "email@email.com",
                        senha_hash="senha")
        note = Nota(
                        titulo = usuario_e_nota["titulo"],
                        conteudo =usuario_e_nota["nota"])
        criar_novo_usuario_e_nota(user, note)
        return jsonify({"message": "Usuario e nota criados com sucesso!"}), 201
    else:
        return jsonify({'error': 'Pagina nao encontrada!'}), 404
             
if __name__ == "__main__":
    app.run() 