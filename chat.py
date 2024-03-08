import flet as ft

def main(page):
    text = ft.Text("Plus Chat")

    chat = ft.Column()
    
    def connect_message(message):
        print(message)
        chat.controls.append(ft.Text(message))
        page.update()

    page.pubsub.subscribe(connect_message)  

    def send_message(event):
        print("Enviar mensagem")
        page.pubsub.send_all(f"{userName.value}: {field_message.value}")
        field_message.value = ""
        page.update()

    field_message = ft.TextField(label="Write the mensage", on_submit=send_message)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=send_message)
    linha_enviar = ft.Row([field_message, botao_enviar])

    def enter_chat(event):
        print("Entrando no Chat")
        popup.open = False #fecha popoup
        page.remove(start_button) #tira o botão iniciar
        page.remove(text) #tira o título
        page.add(chat) #cria o chat
        page.pubsub.send_all(f"{userName.value} entrou no chat")

        page.add(linha_enviar)
        page.update() 

    titlePopup = ft.Text("Welcome")
    userName = ft.TextField(label="Write your name")
    enterButton = ft.ElevatedButton("Start chat", on_click=enter_chat)

    popup = ft.AlertDialog(
        open=False, 
        modal=True,
        title=titlePopup,
        content=userName,
        actions=[enterButton]
    )

    def openpopup(event):
        page.dialog = popup
        popup.open = True
        page.update()

    start_button = ft.ElevatedButton("Start Chat", on_click=openpopup)
    
    page.add(text)
    page.add(start_button)

ft.app(target=main, view=ft.WEB_BROWSER)