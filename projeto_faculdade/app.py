import flet as ft
from main import ler_dados, atualizar_nota, criar_novo_usuario_e_nota, deletar_usuario, login_de_usuario, matricular_aluno
from tabelas import Usuario, Nota

def main(page: ft.Page):
    page.title = "Sistema de Notas"
    page.window_width = 800
    page.window_height = 600

    def exibir_home(e=None):
        page.controls.clear()
        page.controls.append(
            ft.Column([
                ft.Text("Bem-vindo à Home!", size=24, weight="bold"),
                ft.ElevatedButton("Ver Usuários", on_click=mostrar_usuarios),
                ft.ElevatedButton("Cadastrar Usuário e Nota", on_click=exibir_formulario_cadastro),
                ft.ElevatedButton("Login", on_click=exibir_login),
            ])
        )
        page.update()

    def mostrar_usuarios(e=None):
        page.controls.clear()
        try:
            dados = ler_dados()
            lista = ft.Column([
                ft.Text("Usuários cadastrados", size=20, weight="bold"),
                *[ft.Text(str(usuario)) for usuario in dados]
            ])
        except Exception as ex:
            lista = ft.Text(f"Erro ao ler dados: {ex}", color="red")
        page.controls.append(lista)
        page.controls.append(ft.ElevatedButton("Voltar", on_click=exibir_home))
        page.update()

    def exibir_formulario_cadastro(e=None):
        nome = ft.TextField(label="Nome")
        email = ft.TextField(label="Email")
        senha = ft.TextField(label="Senha", password=True)
        titulo = ft.TextField(label="Título da Nota")
        nota = ft.TextField(label="Conteúdo da Nota")

        def enviar(e):
            try:
                user = Usuario(nome=nome.value, email=email.value, senha_hash=senha.value)
                note = Nota(titulo=titulo.value, conteudo=nota.value)
                criar_novo_usuario_e_nota(user, note)
                page.snack_bar = ft.SnackBar(ft.Text("Usuário e nota criados com sucesso!"), bgcolor="green")
            except Exception as ex:
                page.snack_bar = ft.SnackBar(ft.Text(f"Erro: {ex}"), bgcolor="red")
            page.snack_bar.open = True
            page.update()

        page.controls.clear()
        page.controls.append(
            ft.Column([
                ft.Text("Cadastrar Usuário e Nota", size=20, weight="bold"),
                nome, email, senha, titulo, nota,
                ft.Row([
                    ft.ElevatedButton("Cadastrar", on_click=enviar),
                    ft.ElevatedButton("Voltar", on_click=exibir_home),
                ])
            ])
        )
        page.update()

    def exibir_login(e=None):
        email = ft.TextField(label="Email")
        senha = ft.TextField(label="Senha", password=True)

        def logar(e):
            try:
                user = Usuario(email=email.value, senha_hash=senha.value)
                usuario_logado = login_de_usuario(user)
                page.snack_bar = ft.SnackBar(ft.Text(f"Login realizado com sucesso! Bem-vindo, {usuario_logado.nome}."), bgcolor="green")
            except Exception as ex:
                page.snack_bar = ft.SnackBar(ft.Text(f"Erro: {ex}"), bgcolor="red")
            page.snack_bar.open = True
            page.update()

        page.controls.clear()
        page.controls.append(
            ft.Column([
                ft.Text("Login de Usuário", size=20, weight="bold"),
                email, senha,
                ft.Row([
                    ft.ElevatedButton("Entrar", on_click=logar),
                    ft.ElevatedButton("Voltar", on_click=exibir_home),
                ])
            ])
        )
        page.update()

    exibir_home()

ft.app(target=main)
