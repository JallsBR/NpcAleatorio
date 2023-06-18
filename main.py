from flet import *
from utilitáriosRPG import *

def main(page: Page):
    page.window_width = 650.00
    page.window_height = 1030.00
    page.auto_scroll
    page.bgcolor='white'

    page.title = "Gerador de NPC"
    t = Text(value="  GERADOR DE NPCS", size=35, weight='bold')
    st = Text(value="    Para escolha aleatória, deixe o campo vazio\n", color="gray", size=15)
    page.controls.append(t)
    page.controls.append(st)
    page.update()
    nome = TextField(label='Nome', value='', scale=0.9)
    nd = TextField(label='Nível de desafio aproximado', value=0, scale=0.9)
    ca = TextField(label='CA', value=0, scale=0.9)
    pv = TextField(label='PV', value=0, scale=0.9)
    raça = TextField(label='Raça', value='', scale=0.9)
    tendencia = TextField(label='Tendência', value='', scale=0.9)
    força = TextField(label='Força', value=0, scale=0.9)
    destreza = TextField(label='Destreza', value=0, scale=0.9)
    constituição = TextField(label='Constituição', value=0, scale=0.9)
    sabedoria = TextField(label='Sabedoria', value=0, scale=0.9)
    inteligência = TextField(label='Inteligência', value=0, scale=0.9)
    carisma = TextField(label='Carisma', value=0, scale=0.9)
    classe = TextField(label='Classe de conjuração', value='', scale=0.9)
    cd = TextField(label='CD', value=0, scale=0.9)
    magia = Checkbox(label='Magia', scale=0.9)
    resultado = TextField(label='NPC GERADO', min_lines=1, max_lines=9, multiline=True, scale=0.95)
    npc_gerado = {'teste':0}


    def clicar_gerar(e):
        #Resgatando valores do formulário
        resultado.value = ''
        page.update()
        npc_gerado['Nome'] = str(nome.value).strip().capitalize()
        npc_gerado['ND'] = int(nd.value)
        npc_gerado['Classe de Armadura'] = int(ca.value)
        npc_gerado['PV'] = int(pv.value)
        npc_gerado['Raça'] = str(raça.value.strip().capitalize())
        npc_gerado['Tendência'] = str(tendencia.value.strip().capitalize())
        npc_gerado['Atributos'] = {}
        npc_gerado['Atributos']['Força'] = int(força.value)
        npc_gerado['Atributos']['Destreza'] = int(destreza.value)
        npc_gerado['Atributos']['Constituição'] = int(constituição.value)
        npc_gerado['Atributos']['Sabedoria']  = int(sabedoria.value)
        npc_gerado['Atributos']['Inteligência'] = int(inteligência.value)
        npc_gerado['Atributos']['Carisma']  = int(carisma.value)
        npc_gerado['Classe'] = str(classe.value.strip().capitalize())
        npc_gerado['CD'] = int(cd.value)
        npc_gerado['Magia'] = magia.value

        personagem = npc(nd=npc_gerado['ND'], nome_npc=npc_gerado['Nome'], raça=npc_gerado['Raça'],tendencia=npc_gerado['Tendência'],
                         força = npc_gerado['Atributos']['Força'], destreza = npc_gerado['Atributos']['Destreza'],
                         constituição = npc_gerado['Atributos']['Constituição'], inteligencia= npc_gerado['Atributos']['Inteligência'],
                         sabedoria=npc_gerado['Atributos']['Sabedoria'], carisma=npc_gerado['Atributos']['Carisma'],
                         ca= npc_gerado['Classe de Armadura'], pv = npc_gerado['PV'], magia= npc_gerado['Magia'],
                         classe=npc_gerado['Classe'], cd= npc_gerado['CD']
                         )
        #print(personagem)

        for k, v in personagem.items():
            resultado.value+=(f'{k} : {v} \n')


        page.update()

    gerar = FilledButton(text='                                                   Gerar NPC                                                   ', on_click=clicar_gerar, )


    page.add(
            Row(controls=[nome, nd,]),
            Row(controls=[ca, pv]),
            Row(controls=[raça, tendencia]),
            Row(controls=[força, destreza]),
            Row(controls=[constituição, sabedoria]),
            Row(controls=[inteligência, carisma]),
            Row(controls=[classe, cd]),
            Row(controls=[magia, gerar]),
            Column(controls=[resultado]),
            Row(controls=[Text(value='por Oswaldo Jales    ', size=12, color='blue')], alignment=MainAxisAlignment.END )
            )



app(target=main)
