def nome_aleatório():
    """
        Retorna um nome duplo aleatório escolhido na lista dafunção

    """
    from random import randint, sample
    nome = ['Nehaleen', 'Zahir', 'Sheenbrehl', 'Raadik', 'Tirillia', 'Firlans', 'Rathmys', 'Magnus', 'Dandallion', 'Cleef',
                'Urhan', 'Ejamar', 'Ushan', 'Ugovras', 'Igoxium', 'Ataz', 'Azadium', 'Oharad',
                'Olozor', 'Oligron', 'Ophior', 'Equam', 'Grijahr', 'Aharis', 'Aqinn',
                'Aharise', 'Anydae', 'Atosh', 'Neharise', 'Estrea', 'Nubis', 'Rephaen', 'Udephyx', 'Ewaelle',
                'Nughis', 'Chodeis', 'Asizith', 'Zivia', 'Phazohra', 'Nivile', 'Omiharise', 'Adric', 'Oriseus', 'Hardalis',
                'Shandra', 'Artorius', 'Bolthorn', 'Hrothmar', 'Thrael', 'Harlech', 'Franmar', 'If', 'Tyunn', 'Aun', 'Tyor', 'Grirn'
                'Vorrus', 'Grafralf', 'Raslerd', 'Sguf', 'Smik', 'Fralf', 'Brelgaumm', 'Ghortmir', 'Rhendraek', 'Relpamm',
                'Nerer', 'Norngest', 'Hofnolsaern', 'Gwo', 'Kiog', 'Gweih', 'Teigde', 'Fulhif', 'Velfhus', 'Algra', 'Ghindrin',
                'Murkuta', 'Soymalhu', 'Trul', 'Grun', 'Rhi', 'Asvah', 'Grergi', 'Gridieh', 'Trifoth', 'Fraeymuh', 'Edemont',
                'Herlendal', 'Sadreen', 'Joran', 'Cortter', 'Sherisya', 'Phareman', 'Thybaut', 'Gautzelin', 'Godfree', 'Girardus',
                'Gerould', 'Gualterius', 'Gocelinus', 'Lambin', 'Tobye', 'Conayn', 'Joppa', 'Hamlyn', 'Percival', 'Americus',
                'Reginalde', 'Nicky', 'Theodoric', 'Carle', 'Huchon', 'Mold', 'Thomas', 'Elizabetha', 'Swetelove', 'Gisella',
                'Evelot', 'Mahaut', 'Joetta', 'Jessimond', 'Aalis', 'Willem', 'Ardalan', 'Mathurin', 'Orean', 'Bareris', 'The Magnificent',
                'The Crow', 'The Dread', 'The Dire One', 'The Venom Tongue', 'Raveneye', 'Proudstrike', 'Hell Grim',
                'Fuse Hand', 'Bonebane', 'The Cursed', 'The Wild', 'The Delirious', 'The Marked One', 'The Legionnaire', 'Skullblood',
                'Greatpelt', 'Thunderscar', 'Shieldbolt', 'Shadowblood', 'Conrad del Río', 'Davie', 'Moyse', 'Garner',
                'Dandi', 'Willelm', 'Ivon', 'Bartholomew', 'Valter', 'Gregory', 'Tybalt', 'Auguinare', 'Dickory', 'Steuan',
                'Harry', 'Gualtie', 'Tibbott', 'Geoff', 'Amaury', 'Jervis', 'Eyjolf', 'Halfdan', 'Hovarth', 'Frith', 'Svanni',
                'Ysjra', 'Svenhylde', 'Hrurior', 'Skaldr', 'Svepul', 'Skaronul', 'Geimadra',
                'Frileif', 'Regigabi', 'Hivif', 'Sanrun', 'Hervif', 'Goronul', 'Gerun', 'Mipul', 'Rogjold', 'Ald', 'Skondul',
                'Thrugin', 'Sind', 'Satha', 'Svarja', 'Sannhildr', 'Santa', 'Hladmadra', 'Vala', 'Skolmold',
                'Aravilar', 'Saevel', 'Silveth', 'Vlondril', 'Callendra', 'Neldor', 'Beistina', 'Mitalar', 'Leokalyn', 'Alabyran', 'Herra',
                'Thallan', 'Venwarin', 'Thuridan', 'Wysaro', 'Gaelin', 'Wysanorin', 'Aimon', 'Wysamoira', 'Akkar', 'Zyllana',
                'Pirphal', 'Caiwarin', 'Beldroth', 'Triszumin', 'Folre', 'Lusandoral', 'Iefyr', 'Quinorin', 'Luirlan', 'Trisro',
                'Kieran', 'Balrieth', 'Gaeleath', 'Traphine', 'Thuridan', 'Aolis', 'Olamaris', 'Elkhazel',
                'Theris', 'Delmuth', 'Phifir', 'Travaran', 'Iangolor', 'Saria', 'Carlynn', 'Annallee', 'Dorsys', 'Tiriana', 'Qirel',
                'Itylara', 'Farna', 'Ildilyntra', 'Raloydark', 'Ilsevel', 'Aralar', 'Daethie', 'Trisxina', 'Immianthe',
                'Gilbanise', 'Daethie', 'Sylbalar', 'Lensa', 'Kylantha', 'Farric', 'Merlara', 'Genlar', 'Yathanae', 'Yelbella',
                'Nushala', 'Elgella', 'Ratha', 'Venthana', 'Nalaea', 'Luharice', 'Ashera', 'Valxina', 'Faylen', 'Envalur',
                'Tarasynora', 'Glynxisys', 'Alyndra', 'Valwraek', 'Rurik', 'Wulgar', 'Morgrym', 'Ingra', 'Sambril', 'Gardrotir',
                'Blazingmaul' 'Arabor', 'Lug', 'Kragflayer', 'Bandraed', 'Hillbane', 'Elkdraic', 'Bonearm', 'Kuvreal', 'Goldriver',
                'Orirerlun', 'Dragonshield', 'Bebaic', 'Cavethane', 'Grotmec', 'Bottleblade', 'Lorgruth', 'Cragthane',
                'Grournirlun', 'Silverthane', 'Runmin', 'Blazingguard', 'Duldrur', 'Beastbasher', 'Glammag', 'Lightbrow', 'Adduk', 'Blackgrip',
                'Dhummorli', 'Keghand', 'Umizzumri', 'Flatshoulder', 'Reinmeac', 'Redfury', 'Dosonlir', 'Brickshoulder',
                'Hakkouth', 'Ashmail', 'Lokdrel', 'Blessedbender', 'Thargreasli', 'Befaetalin', 'Strongbreaker',
                'Bubrawynn', 'Merryriver', 'Brutatrud', 'Bloodhelm', 'Dhuznaegar', 'Greyarm', 'Groubaelynn', 'Axefury',
                'Arakhusli', 'Darkbuster', 'Koleagith', 'Frostshield', 'Brubrure', 'Orcspine', 'Thumwuhulda', 'Heavybuster', 'Aradmogith',
                'Merrymaul', 'Nazmaginn', 'Blazingrock', 'Ruldrutalyn', 'Orehide', 'Khourgatalyn', 'Warmrock', 'Karfisli',
                'Orcmace', 'Ufrubo', 'Snowguard', 'Kandritelyn', 'Treasurebranch', 'Brolmeatelin', 'Warmdelver', 'Douraela',
                'Wraithheart', 'Asseagit', 'Wyvernbeard', 'Artemis', 'Sven', 'Flint', 'Aurus', 'Filgore', 'Sardes', 'Stark', 'Brovos', 'Bravos',
                'Rhanna', 'Raegar', 'Netril', 'Beldar', 'Slinker', 'Morgan', 'Vonn', 'Sylr', 'Jalls', 'Jarls', 'Storm', 'Arty', 'Jammem', 'Bosk',
                'Deric', 'Stone', 'Verona', 'Seloron', 'Halu', 'Eldar', 'Feanor', 'Tholl', 'Traal', 'Brodkon', 'Bret', 'Halk', 'Errol',
                'Helm', 'Sington', 'Rolf', 'Palmer', 'Arum', 'Guildegard', 'Mira', 'Jillian', 'Mara', 'Tara', 'Theory', 'Mythvalley',
                'Monnhide', 'Hide', 'Valindra', 'Dust', 'Dusk', 'Dusksword', 'Riccon', 'Valan', 'Elistrae', 'Matthaus', 'Matheus', 'Crypto',
                'Stevan', 'Jargus', 'Jalin', 'Maraud', 'Von', 'Van', 'Allan', 'Alonso', 'Elder', 'Ash', 'Vanguard']
    nomealeatorio = sample(nome, k=len(nome))
    personagem = nomealeatorio[0:2]
    return personagem


def raça_aleatória(raça = ''):
    """
        Retorna uma raçã aleatóroria
    """
    from random import choice
    if raça != '':
        raça = raça.strip().title()
    raças = ['Humano', 'Humano', 'Humano', 'Humano', 'Humano', 'Humano', 'Humano', 'Humano', 'Humano', 'Humano', 'Elfo',
             'Elfo',
             'Elfo', 'Elfo', 'Meio-elfo', 'Anão', 'Anão', 'Anão', 'Draconato', 'Gnomo', 'Gnomo', 'Halfling', 'Halfling',
             'Tiefling', 'Meio-Orc', 'Orc', 'Genasi', 'Goblin']
    escolhe_raça= choice(raças)
    if raça != '':
        escolhe_raça = raça
    return escolhe_raça


def tendência_aleatória():
    """
        Retorna tendência/alinhamento aleatório
    """
    from random import choice, sample
    tendência = ['Caótico e bom', 'Caótico e neutro', 'Caótico e mal', 'Neutro e bom', 'Neutro e neutro', 'Neutro e mal',
                'Leal e bom', 'Leal e neutro', 'Leal e mal']
    escolher_tendencia = choice(tendência)
    return escolher_tendencia


def gerar_atributos(força = 0, destreza = 0,constituição = 0,inteligencia = 0, sabedoria = 0, carisma = 0 ):
    """
        Gera atributos aleatorios ou formata atributos com seus respectivos bônus

    """
    from random import randint, sample
    while True:
        atributo = (randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6))
        if força == 0:
            força = atributo[0] + atributo[1] + \
                    atributo[2] + atributo[3] - min(atributo)
        elif destreza == 0:
            destreza = atributo[0] + atributo[1] + \
                       atributo[2] + atributo[3] - min(atributo)
        elif constituição == 0:
            constituição = atributo[0] + atributo[1] + \
                           atributo[2] + atributo[3] - min(atributo)
        elif inteligencia == 0:
            inteligencia = atributo[0] + atributo[1] + \
                           atributo[2] + atributo[3] - min(atributo)
        elif sabedoria == 0:
            sabedoria = atributo[0] + atributo[1] + \
                        atributo[2] + atributo[3] - min(atributo)
        elif carisma == 0:
            carisma = atributo[0] + atributo[1] + \
                      atributo[2] + atributo[3] - min(atributo)
        else:
            break

    proef = randint(2, 6)

    bfor = (força - 10) // 2
    bdes = (destreza - 10) // 2
    bcon = (constituição - 10) // 2
    bint = (inteligencia - 10) // 2
    bsab = (sabedoria - 10) // 2
    bcar = (carisma - 10) // 2

    return {'Força': [força, (força - 10) // 2],
            'Destreza': [destreza, (destreza - 10) // 2],
            'Constituição': [constituição, (constituição - 10) // 2],
            'Inteligência': [inteligencia, (inteligencia - 10) // 2],
            'Sabedoria': [sabedoria, (sabedoria - 10) // 2],
            'Carisma': [carisma, (carisma - 10) // 2]}


def saves_aleatorios(proef=2, bfor=0, bdes=0, bcon=0, bint=0, bsab=0, bcar=0):
    """
        Retorna salvagardas aleatóroria
    :param proef: Bônus de proeficiência
    :param bfor: Bônus de Força
    :param bdes: Bônus de Destreza
    :param bcon: Bônus de Constituição
    :param bint: Bônus de Inteligência
    :param bsab: Bônus de Sabedoria
    :param bcar: Bônus de Carisma

    """
    from random import randint, sample
    save = [f'For {bfor + proef}', f'Des {bdes + proef}', f'Cons {bcon + proef}', f'Int {bint + proef}',
            f'Sab {bsab + proef}', f'Car {bcar + proef}']
    savelen = 5
    # randomizar lista de saves
    savesaleatorios = sample(save, k=len(save))
    return {'Saves': savesaleatorios[0:randint(2, 3)]}


def aptidão_mágica(magia=False, classe=''):
    """
        Randomiza a possibilidade de um personagem conter magia
    :param magia: Pro padrão está em False, se modificado para True o personagem possui magias
    :param classe: Especifica uma determinada classe

    """

    from random import randint, sample
    aptidão_magica = randint(1, 15)
    magias1 = magias2 = magias3 = magias4= magias5 =0
    if magia:
        aptidão_magica = 15
    if aptidão_magica == 15:
        truques = randint(1, 3)
        magias1 = randint(0, 3)
        if magias1 > 1:
            magias2 = (randint(0, 3))
            if magias2 > 1:
                magias3 = randint(0, 3)
                if magias3 > 1:
                    magias4 = randint(0, 3)
                    if magias4 > 1:
                        magias5 = randint(0, 3)
        caster = randint(1, 7)
        tipomagico = None
        if classe != '':
            tipomagico = classe
        else:
            if caster == 1:
                tipomagico = 'Clérigo'
            if caster == 2:
                tipomagico = 'Mago'
            if caster == 3:
                tipomagico = 'Druida'
            if caster == 4:
                tipomagico = 'Bardo'
            if caster == 5:
                tipomagico = 'Paladino'
            if caster == 6:
                tipomagico = 'Bruxo'
            if caster == 7:
                tipomagico = 'Feiticeiro'

    if aptidão_magica == 15:
        feitiços = {'Aptidão Mágica': aptidão_magica,'Classe': tipomagico, 'Truques': truques }
        feitiços['Magias1'] = 0
        feitiços['Magias2'] = 0
        feitiços['Magias3'] = 0
        feitiços['Magias4'] = 0
        feitiços['Magias5'] = 0
        if magias1 > 0:
            feitiços['Magias1']=1
            feitiços['1Círculo'] = magias1
            if magias2 > 0:
                feitiços['Magias2'] = 1
                feitiços['2Círculo'] = magias2
                if magias3 > 0:
                    feitiços['Magias3'] = 1
                    feitiços['3Círculo'] = magias3
                    if magias4 > 0:
                        feitiços['Magias4'] = 1
                        feitiços['4Círculo'] = magias4
                        if magias5 > 0:
                            feitiços['Magias5'] = 1
                            feitiços['5Círculo'] = magias5
    if aptidão_magica == 15:
        return feitiços
    else:
        return {'Aptidão Mágica': 0}


def pericias_aleatorias (proef=2, bfor=0, bdes=0, bcon=0, bint=0, bsab=0, bcar=0):
    """
        Retorna pericias aleatórias
    :param proef: Bônus de proeficiência
    :param bfor: Bônus deForça
    :param bdes: Bônus de Destreza
    :param bcon: Bônus de Constituição
    :param bint: Bônus de Inteligência
    :param bsab: Bônus de Sabedoria
    :param bcar: Bônus de Carisma

    """
    from random import randint, sample
    todaspericias = [f'Acrobacia {bdes + proef}', f'Adestrar Animais {bsab + proef}', f'Arcanismo {bint + proef}',
                     f'Atletismo {bfor + proef}', f'Enganação {bcar + proef}', f'Furtividade {bdes + proef}',
                     f'História {bint + proef}', f'Intimidação {bcar + proef}', f'Intuição {bsab + proef}',
                     f'Investigação {bint + proef}',
                     f'Medicina {bsab + proef}', f'Natureza {bint + proef}', f'Percepção {bsab + proef}',
                     f'Performance {bcar + proef}', f'Persuasão {bcar + proef}',
                     f'Prestidigitação {bdes + proef}', f'Religião {bint + proef}', f'Sobrevivência {bsab + proef}']
    # randomizar lista de pericias
    periciasaleatorias = sample(todaspericias, k=len(todaspericias))
    return {'Perícias': periciasaleatorias[0: randint(2, 4)]}


def ataques_aleatorios(proef=2, bfor=0, bdes=0, bônusataque=0, bonusdano = 0):
    """
        Randomiza 2 armas e seus ataques
    :param proef: Bônus de proeficiência
    :param bfor: Bônus de Força
    :param bdes: Bônus de Destreza
    :param bônusataque: Bônus de ataque
    :param bonusdano: Bônus de dano
    :return:
    """
    from random import randint, sample
    armaslista = [
        f'Adaga. Ataque Corpo-a-Corpo ou a distância com Arma: +{proef + bdes + bônusataque} para atingir, alcance 6/18 m, um alvo.Acerto: {bdes + bonusdano + 3}(1d4 + {bdes + bonusdano}) de dano perfurante.',
        f'Lança. Ataque Corpo-a-Corpo ou a distância com Arma: +{proef + bdes + bônusataque} para atingir, alcance 6/18 m, um alvo.Acerto: {bdes + bonusdano + 5}(1d8 + {bdes + bonusdano}) de dano perfurante.',
        f'Espada Curta. Ataque Corpo-a-Corpo com Arma: +{proef + bfor+ bônusataque} para atingir, alcance 1,5m, um alvo.Acerto: {bfor + bonusdano + 4}(1d6 + {bfor + bonusdano}) de dano perfurante.',
        f'Maça. Ataque Corpo-a-Corpo com Arma: +{proef + bfor + bônusataque} para atingir, alcance 1,5m, um alvo.Acerto: {bfor+ bonusdano + 4}(1d6 + {bfor + bonusdano}) de dano contundente.',
        f'Espada Longa. Ataque Corpo-a-Corpo com Arma: +{proef + bfor+ bônusataque} para atingir, alcance 1,5m, um alvo.Acerto: {bfor + bonusdano + 5}(1d8 + {bfor + bonusdano}) de dano perfurante.',
        f'Arco Longo.Ataque à Distância com Arma: +{proef + bdes + bônusataque} para atingir, distância 45 / 180m, um alvo.Acerto: {5 + bdes + bonusdano}(1d8 + {bdes + bonusdano}) de dano perfurante.']
    ataques = sample(armaslista, k=len(armaslista))
    return {'Ataque1': ataques[0:1], 'Ataque2': ataques[2:3]}


def livro_nd (nd_pretendido = 0):
    """
        Consulta de um ND segundo o livro do mestre
    :param nd_pretendido: nd a ser retornado

    """
    from random import randint
    nd_livro = [{'ND': 0, 'Proef': 2, "CA": 13, 'PV': randint(1, 6), 'Pvmin': 1, 'Pvmax': 6, 'Bônus Ataque': 3,
                 'Dano Rodada': randint(0, 1), 'Danomin': 0, 'Danomax': 1, 'CD': 13},
                {'ND': 1 / 8, 'Proef': 2, "CA": 13, 'PV': randint(7, 35), 'Pvmin': 7, 'Pvmax': 35, 'Bônus Ataque': 3,
                 'Dano Rodada': randint(2, 3), 'Danomin': 2, 'Danomax': 3, 'CD': 13},
                {'ND': 1 / 4, 'Proef': 2, "CA": 13, 'PV': randint(36, 49), 'Pvmin': 36, 'Pvmax': 49, 'Bônus Ataque': 3,
                 'Dano Rodada': randint(4, 5), 'Danomin': 4, 'Danomax': 5, 'CD': 13},
                {'ND': 1 / 2, 'Proef': 2, "CA": 13, 'PV': randint(50, 70), 'Pvmin': 50, 'Pvmax': 70, 'Bônus Ataque': 3,
                 'Dano Rodada': randint(6, 8), 'Danomin': 6, 'Danomax': 8, 'CD': 13},
                {'ND': 1, 'Proef': 2, "CA": 13, 'PV': randint(71, 85), 'Pvmin': 71, 'Pvmax': 85, 'Bônus Ataque': 3,
                 'Dano Rodada': randint(9, 14), 'Danomin': 9, 'Danomax': 14, 'CD': 13},
                {'ND': 2, 'Proef': 2, "CA": 13, 'PV': randint(86, 100), 'Pvmin': 86, 'Pvmax': 100, 'Bônus Ataque': 3,
                 'Dano Rodada': randint(15, 20), 'Danomin': 15, 'Danomax': 20, 'CD': 13},
                {'ND': 3, 'Proef': 2, "CA": 13, 'PV': randint(101, 115), 'Pvmin': 101, 'Pvmax': 115, 'Bônus Ataque': 4,
                 'Dano Rodada': randint(21, 26), 'Danomin': 21, 'Danomax': 26, 'CD': 13},
                {'ND': 4, 'Proef': 2, "CA": 14, 'PV': randint(116, 130), 'Pvmin': 116, 'Pvmax': 130, 'Bônus Ataque': 5,
                 'Dano Rodada': randint(27, 32), 'Danomin': 27, 'Danomax': 32, 'CD': 14},
                {'ND': 5, 'Proef': 3, "CA": 15, 'PV': randint(131, 145), 'Pvmin': 131, 'Pvmax': 145, 'Bônus Ataque': 6,
                 'Dano Rodada': randint(33, 38), 'Danomin': 33, 'Danomax': 38, 'CD': 15},
                {'ND': 6, 'Proef': 3, "CA": 15, 'PV': randint(146, 160), 'Pvmin': 146, 'Pvmax': 160, 'Bônus Ataque': 6,
                 'Dano Rodada': randint(39, 44), 'Danomin': 39, 'Danomax': 44, 'CD': 15},
                {'ND': 7, 'Proef': 3, "CA": 15, 'PV': randint(161, 175), 'Pvmin': 161, 'Pvmax': 175, 'Bônus Ataque': 6,
                 'Dano Rodada': randint(45, 50), 'Danomin': 45, 'Danomax': 50, 'CD': 15},
                {'ND': 8, 'Proef': 3, "CA": 16, 'PV': randint(176, 190), 'Pvmin': 176, 'Pvmax': 190, 'Bônus Ataque': 7,
                 'Dano Rodada': randint(51, 56), 'Danomin': 51, 'Danomax': 56, 'CD': 16},
                {'ND': 9, 'Proef': 4, "CA": 16, 'PV': randint(191, 205), 'Pvmin': 191, 'Pvmax': 205, 'Bônus Ataque': 7,
                 'Dano Rodada': randint(57, 62), 'Danomin': 57, 'Danomax': 62, 'CD': 16},
                {'ND': 10, 'Proef': 4, "CA": 17, 'PV': randint(206, 220), 'Pvmin': 206, 'Pvmax': 220, 'Bônus Ataque': 7,
                 'Dano Rodada': randint(63, 68), 'Danomin': 63, 'Danomax': 68, 'CD': 16},
                {'ND': 11, 'Proef': +4, "CA": 17, 'PV': randint(221, 235), 'Pvmin': 221, 'Pvmax': 235,
                 'Bônus Ataque': 8, 'Dano Rodada': randint(69, 74), 'Danomin': 69, 'Danomax': 74, 'CD': 17},
                {'ND': 12, 'Proef': +4, "CA": 17, 'PV': randint(236, 250), 'Pvmin': 236, 'Pvmax': 250,
                 'Bônus Ataque': 8, 'Dano Rodada': randint(75, 80), 'Danomin': 75, 'Danomax': 80, 'CD': 17},
                {'ND': 13, 'Proef': +5, "CA": 18, 'PV': randint(251, 265), 'Pvmin': 251, 'Pvmax': 265,
                 'Bônus Ataque': 8, 'Dano Rodada': randint(81, 86), 'Danomin': 81, 'Danomax': 86, 'CD': 18},
                {'ND': 14, 'Proef': +5, "CA": 18, 'PV': randint(266, 280), 'Pvmin': 266, 'Pvmax': 280,
                 'Bônus Ataque': 8, 'Dano Rodada': randint(87, 92), 'Danomin': 87, 'Danomax': 92, 'CD': 18},
                {'ND': 15, 'Proef': +5, "CA": 18, 'PV': randint(281, 295), 'Pvmin': 281, 'Pvmax': 295,
                 'Bônus Ataque': 8, 'Dano Rodada': randint(93, 98), 'Danomin': 93, 'Danomax': 98, 'CD': 18},
                {'ND': 16, 'Proef': +5, "CA": 18, 'PV': randint(296, 310), 'Pvmin': 296, 'Pvmax': 310,
                 'Bônus Ataque': 9, 'Dano Rodada': randint(99, 104), 'Danomin': 99, 'Danomax': 104, 'CD': 18},
                {'ND': 17, 'Proef': +6, "CA": 19, 'PV': randint(311, 325), 'Pvmin': 311, 'Pvmax': 325,
                 'Bônus Ataque': 10, 'Dano Rodada': randint(105, 110), 'Danomin': 105, 'Danomax': 110, 'CD': 19},
                {'ND': 18, 'Proef': +6, "CA": 19, 'PV': randint(326, 340), 'Pvmin': 326, 'Pvmax': 340,
                 'Bônus Ataque': 10, 'Dano Rodada': randint(111, 116), 'Danomin': 111, 'Danomax': 116, 'CD': 19},
                {'ND': 19, 'Proef': +6, "CA": 19, 'PV': randint(341, 355), 'Pvmin': 341, 'Pvmax': 355,
                 'Bônus Ataque': 10, 'Dano Rodada': randint(117, 122), 'Danomin': 117, 'Danomax': 122, 'CD': 19},
                {'ND': 20, 'Proef': +6, "CA": 19, 'PV': randint(356, 400), 'Pvmin': 356, 'Pvmax': 400,
                 'Bônus Ataque': 10, 'Dano Rodada': randint(123, 140), 'Danomin': 123, 'Danomax': 140, 'CD': 19},
                {'ND': 21, 'Proef': +7, "CA": 19, 'PV': randint(401, 445), 'Pvmin': 401, 'Pvmax': 445,
                 'Bônus Ataque': 11, 'Dano Rodada': randint(141, 158), 'Danomin': 141, 'Danomax': 158, 'CD': 20},
                {'ND': 22, 'Proef': +7, "CA": 19, 'PV': randint(446, 490), 'Pvmin': 446, 'Pvmax': 490,
                 'Bônus Ataque': 11, 'Dano Rodada': randint(159, 176), 'Danomin': 159, 'Danomax': 176, 'CD': 20},
                {'ND': 23, 'Proef': +7, "CA": 19, 'PV': randint(491, 535), 'Pvmin': 491, 'Pvmax': 535,
                 'Bônus Ataque': 11, 'Dano Rodada': randint(177, 194), 'Danomin': 177, 'Danomax': 194, 'CD': 20},
                {'ND': 24, 'Proef': +7, "CA": 19, 'PV': randint(536, 580), 'Pvmin': 536, 'Pvmax': 580,
                 'Bônus Ataque': 11, 'Dano Rodada': randint(195, 212), 'Danomin': 195, 'Danomax': 212, 'CD': 21},
                {'ND': 25, 'Proef': +8, "CA": 19, 'PV': randint(581, 625), 'Pvmin': 581, 'Pvmax': 625,
                 'Bônus Ataque': 12, 'Dano Rodada': randint(213, 230), 'Danomin': 213, 'Danomax': 230, 'CD': 21},
                {'ND': 26, 'Proef': +8, "CA": 19, 'PV': randint(626, 670), 'Pvmin': 626, 'Pvmax': 670,
                 'Bônus Ataque': 12, 'Dano Rodada': randint(231, 248), 'Danomin': 231, 'Danomax': 248, 'CD': 21},
                {'ND': 27, 'Proef': +8, "CA": 19, 'PV': randint(671, 715), 'Pvmin': 671, 'Pvmax': 715,
                 'Bônus Ataque': 13, 'Dano Rodada': randint(249, 266), 'Danomin': 249, 'Danomax': 266, 'CD': 22},
                {'ND': 28, 'Proef': +8, "CA": 19, 'PV': randint(716, 760), 'Pvmin': 715, 'Pvmax': 760,
                 'Bônus Ataque': 13, 'Dano Rodada': randint(267, 284), 'Danomin': 267, 'Danomax': 284, 'CD': 22},
                {'ND': 29, 'Proef': +9, "CA": 19, 'PV': randint(761, 805), 'Pvmin': 761, 'Pvmax': 805,
                 'Bônus Ataque': 13, 'Dano Rodada': randint(285, 302), 'Danomin': 285, 'Danomax': 302, 'CD': 22},
                {'ND': 30, 'Proef': +9, "CA": 19, 'PV': randint(806, 850), 'Pvmin': 806, 'Pvmax': 850,
                 'Bônus Ataque': 14, 'Dano Rodada': randint(303, 320), 'Danomin': 303, 'Danomax': 320, 'CD': 23} ]

    if nd_pretendido == 0:
        nd_pretendido = nd_livro[0]
    elif nd_pretendido == 1/8:
        nd_pretendido = nd_livro[1]
    elif nd_pretendido == 1/4:
        nd_pretendido = nd_livro[2]
    elif nd_pretendido == 1/2:
        nd_pretendido = nd_livro[3]
    elif nd_pretendido > 30:
        nd_pretendido = 30
        nd_pretendido = nd_livro[nd_pretendido+3]
    else:
        nd_pretendido = nd_livro[nd_pretendido+3]
    return nd_pretendido


def nd_resultante (nd_ofensivo=0,  nd_defensivo=0, nd_pretendido=0):
    """
        Retorna ND alterado do ND pretendido com os ajustes de nd ofensivo e defensivo
    :param nd_ofensivo: calculo do nd ofencivo
    :param nd_defensivo:  calculo do nd defensivo
    :param nd_pretendido: retorno do ND correto

    """
    from random import randint
    from math import floor
    nd_livro = [{'ND': 0, 'Proef': 2, "CA": 13, 'PV': randint(1, 6), 'Pvmin': 1, 'Pvmax': 6, 'Bônus Ataque': 3,
                 'Dano Rodada': randint(0, 1), 'Danomin': 0, 'Danomax': 1, 'CD': 13},
                {'ND': 1 / 8, 'Proef': 2, "CA": 13, 'PV': randint(7, 35), 'Pvmin': 7, 'Pvmax': 35, 'Bônus Ataque': 3,
                 'Dano Rodada': randint(2, 3), 'Danomin': 2, 'Danomax': 3, 'CD': 13},
                {'ND': 1 / 4, 'Proef': 2, "CA": 13, 'PV': randint(36, 49), 'Pvmin': 36, 'Pvmax': 49, 'Bônus Ataque': 3,
                 'Dano Rodada': randint(4, 5), 'Danomin': 4, 'Danomax': 5, 'CD': 13},
                {'ND': 1 / 2, 'Proef': 2, "CA": 13, 'PV': randint(50, 70), 'Pvmin': 50, 'Pvmax': 70, 'Bônus Ataque': 3,
                 'Dano Rodada': randint(6, 8), 'Danomin': 6, 'Danomax': 8, 'CD': 13},
                {'ND': 1, 'Proef': 2, "CA": 13, 'PV': randint(71, 85), 'Pvmin': 71, 'Pvmax': 85, 'Bônus Ataque': 3,
                 'Dano Rodada': randint(9, 14), 'Danomin': 9, 'Danomax': 14, 'CD': 13},
                {'ND': 2, 'Proef': 2, "CA": 13, 'PV': randint(86, 100), 'Pvmin': 86, 'Pvmax': 100, 'Bônus Ataque': 3,
                 'Dano Rodada': randint(15, 20), 'Danomin': 15, 'Danomax': 20, 'CD': 13},
                {'ND': 3, 'Proef': 2, "CA": 13, 'PV': randint(101, 115), 'Pvmin': 101, 'Pvmax': 115, 'Bônus Ataque': 4,
                 'Dano Rodada': randint(21, 26), 'Danomin': 21, 'Danomax': 26, 'CD': 13},
                {'ND': 4, 'Proef': 2, "CA": 14, 'PV': randint(116, 130), 'Pvmin': 116, 'Pvmax': 130, 'Bônus Ataque': 5,
                 'Dano Rodada': randint(27, 32), 'Danomin': 27, 'Danomax': 32, 'CD': 14},
                {'ND': 5, 'Proef': 3, "CA": 15, 'PV': randint(131, 145), 'Pvmin': 131, 'Pvmax': 145, 'Bônus Ataque': 6,
                 'Dano Rodada': randint(33, 38), 'Danomin': 33, 'Danomax': 38, 'CD': 15},
                {'ND': 6, 'Proef': 3, "CA": 15, 'PV': randint(146, 160), 'Pvmin': 146, 'Pvmax': 160, 'Bônus Ataque': 6,
                 'Dano Rodada': randint(39, 44), 'Danomin': 39, 'Danomax': 44, 'CD': 15},
                {'ND': 7, 'Proef': 3, "CA": 15, 'PV': randint(161, 175), 'Pvmin': 161, 'Pvmax': 175, 'Bônus Ataque': 6,
                 'Dano Rodada': randint(45, 50), 'Danomin': 45, 'Danomax': 50, 'CD': 15},
                {'ND': 8, 'Proef': 3, "CA": 16, 'PV': randint(176, 190), 'Pvmin': 176, 'Pvmax': 190, 'Bônus Ataque': 7,
                 'Dano Rodada': randint(51, 56), 'Danomin': 51, 'Danomax': 56, 'CD': 16},
                {'ND': 9, 'Proef': 4, "CA": 16, 'PV': randint(191, 205), 'Pvmin': 191, 'Pvmax': 205, 'Bônus Ataque': 7,
                 'Dano Rodada': randint(57, 62), 'Danomin': 57, 'Danomax': 62, 'CD': 16},
                {'ND': 10, 'Proef': 4, "CA": 17, 'PV': randint(206, 220), 'Pvmin': 206, 'Pvmax': 220, 'Bônus Ataque': 7,
                 'Dano Rodada': randint(63, 68), 'Danomin': 63, 'Danomax': 68, 'CD': 16},
                {'ND': 11, 'Proef': +4, "CA": 17, 'PV': randint(221, 235), 'Pvmin': 221, 'Pvmax': 235,
                 'Bônus Ataque': 8, 'Dano Rodada': randint(69, 74), 'Danomin': 69, 'Danomax': 74, 'CD': 17},
                {'ND': 12, 'Proef': +4, "CA": 17, 'PV': randint(236, 250), 'Pvmin': 236, 'Pvmax': 250,
                 'Bônus Ataque': 8, 'Dano Rodada': randint(75, 80), 'Danomin': 75, 'Danomax': 80, 'CD': 17},
                {'ND': 13, 'Proef': +5, "CA": 18, 'PV': randint(251, 265), 'Pvmin': 251, 'Pvmax': 265,
                 'Bônus Ataque': 8, 'Dano Rodada': randint(81, 86), 'Danomin': 81, 'Danomax': 86, 'CD': 18},
                {'ND': 14, 'Proef': +5, "CA": 18, 'PV': randint(266, 280), 'Pvmin': 266, 'Pvmax': 280,
                 'Bônus Ataque': 8, 'Dano Rodada': randint(87, 92), 'Danomin': 87, 'Danomax': 92, 'CD': 18},
                {'ND': 15, 'Proef': +5, "CA": 18, 'PV': randint(281, 295), 'Pvmin': 281, 'Pvmax': 295,
                 'Bônus Ataque': 8, 'Dano Rodada': randint(93, 98), 'Danomin': 93, 'Danomax': 98, 'CD': 18},
                {'ND': 16, 'Proef': +5, "CA": 18, 'PV': randint(296, 310), 'Pvmin': 296, 'Pvmax': 310,
                 'Bônus Ataque': 9, 'Dano Rodada': randint(99, 104), 'Danomin': 99, 'Danomax': 104, 'CD': 18},
                {'ND': 17, 'Proef': +6, "CA": 19, 'PV': randint(311, 325), 'Pvmin': 311, 'Pvmax': 325,
                 'Bônus Ataque': 10, 'Dano Rodada': randint(105, 110), 'Danomin': 105, 'Danomax': 110, 'CD': 19},
                {'ND': 18, 'Proef': +6, "CA": 19, 'PV': randint(326, 340), 'Pvmin': 326, 'Pvmax': 340,
                 'Bônus Ataque': 10, 'Dano Rodada': randint(111, 116), 'Danomin': 111, 'Danomax': 116, 'CD': 19},
                {'ND': 19, 'Proef': +6, "CA": 19, 'PV': randint(341, 355), 'Pvmin': 341, 'Pvmax': 355,
                 'Bônus Ataque': 10, 'Dano Rodada': randint(117, 122), 'Danomin': 117, 'Danomax': 122, 'CD': 19},
                {'ND': 20, 'Proef': +6, "CA": 19, 'PV': randint(356, 400), 'Pvmin': 356, 'Pvmax': 400,
                 'Bônus Ataque': 10, 'Dano Rodada': randint(123, 140), 'Danomin': 123, 'Danomax': 140, 'CD': 19},
                {'ND': 21, 'Proef': +7, "CA": 19, 'PV': randint(401, 445), 'Pvmin': 401, 'Pvmax': 445,
                 'Bônus Ataque': 11, 'Dano Rodada': randint(141, 158), 'Danomin': 141, 'Danomax': 158, 'CD': 20},
                {'ND': 22, 'Proef': +7, "CA": 19, 'PV': randint(446, 490), 'Pvmin': 446, 'Pvmax': 490,
                 'Bônus Ataque': 11, 'Dano Rodada': randint(159, 176), 'Danomin': 159, 'Danomax': 176, 'CD': 20},
                {'ND': 23, 'Proef': +7, "CA": 19, 'PV': randint(491, 535), 'Pvmin': 491, 'Pvmax': 535,
                 'Bônus Ataque': 11, 'Dano Rodada': randint(177, 194), 'Danomin': 177, 'Danomax': 194, 'CD': 20},
                {'ND': 24, 'Proef': +7, "CA": 19, 'PV': randint(536, 580), 'Pvmin': 536, 'Pvmax': 580,
                 'Bônus Ataque': 11, 'Dano Rodada': randint(195, 212), 'Danomin': 195, 'Danomax': 212, 'CD': 21},
                {'ND': 25, 'Proef': +8, "CA": 19, 'PV': randint(581, 625), 'Pvmin': 581, 'Pvmax': 625,
                 'Bônus Ataque': 12, 'Dano Rodada': randint(213, 230), 'Danomin': 213, 'Danomax': 230, 'CD': 21},
                {'ND': 26, 'Proef': +8, "CA": 19, 'PV': randint(626, 670), 'Pvmin': 626, 'Pvmax': 670,
                 'Bônus Ataque': 12, 'Dano Rodada': randint(231, 248), 'Danomin': 231, 'Danomax': 248, 'CD': 21},
                {'ND': 27, 'Proef': +8, "CA": 19, 'PV': randint(671, 715), 'Pvmin': 671, 'Pvmax': 715,
                 'Bônus Ataque': 13, 'Dano Rodada': randint(249, 266), 'Danomin': 249, 'Danomax': 266, 'CD': 22},
                {'ND': 28, 'Proef': +8, "CA": 19, 'PV': randint(716, 760), 'Pvmin': 715, 'Pvmax': 760,
                 'Bônus Ataque': 13, 'Dano Rodada': randint(267, 284), 'Danomin': 267, 'Danomax': 284, 'CD': 22},
                {'ND': 29, 'Proef': +9, "CA": 19, 'PV': randint(761, 805), 'Pvmin': 761, 'Pvmax': 805,
                 'Bônus Ataque': 13, 'Dano Rodada': randint(285, 302), 'Danomin': 285, 'Danomax': 302, 'CD': 22},
                {'ND': 30, 'Proef': +9, "CA": 19, 'PV': randint(806, 850), 'Pvmin': 806, 'Pvmax': 850,
                 'Bônus Ataque': 14, 'Dano Rodada': randint(303, 320), 'Danomin': 303, 'Danomax': 320, 'CD': 23}]
    if nd_pretendido == 0:
        nd_pretendido = nd_livro[0]
    elif nd_pretendido == 1/8:
        nd_pretendido = nd_livro[1]
    elif nd_pretendido == 1/4:
        nd_pretendido = nd_livro[2]
    elif nd_pretendido == 1/2:
        nd_pretendido = nd_livro[3]
    elif nd_pretendido > 30:
        nd_pretendido = 30
        nd_pretendido = nd_livro[nd_pretendido+3]
    else:
        nd_pretendido = nd_livro[nd_pretendido+3]

    nd_resultante = floor(((nd_ofensivo + nd_defensivo) / 2) + nd_pretendido['ND'])
    if nd_resultante == 0:
        nd_resultante = nd_livro[0]
    elif nd_resultante == 1 / 8:
        nd_resultante = nd_livro[1]
    elif nd_resultante == 1 / 4:
        nd_resultante = nd_livro[2]
    elif nd_resultante == 1 / 2:
        nd_resultante = nd_livro[3]
    elif nd_resultante > 30:
        nd_resultante = 30
        nd_resultante = nd_livro[nd_resultante + 3]
    else:
        nd_resultante = nd_livro[nd_resultante + 3]

    return nd_resultante['ND']


def rolagem_de_dados(rolagens=1, lados=6, bonus=0):
    """
    Função para resolver parada de dados

        :param rolagens: numero de vezes que o dado será rolado
        :param lados: Numero de lados do dado
        :param bonus: Número a ser somado ao resultado
        :return: informação sobre a rolagem
    """
    global retorno
    from random import randint

    rolagem_final = []
    count = rolagens
    parada_de_dados = []


    while count != 0:
        dado = randint(1, lados)
        rolagem_final.append(dado)
        count -= 1

    if bonus != 0:
        retorno = f'{rolagem_final} + {bonus}, Total {sum(rolagem_final) + bonus}'
    else:
        retorno = f'{rolagem_final}, Total {sum(rolagem_final)}'

    return retorno


def vantagem(bonus=0):
    """
    Função para resolver parada de dados de vantagem

        :param bonus: Número a ser somado ao resultado
        :return: informação sobre a rolagem
    """
    global retorno
    from random import randint

    rolagem_final = []
    parada_de_dados = []

    dado1 = randint(1, 20)
    dado2 = randint(1, 20)
    vantagem = [dado1, dado2]
    rolagem_final.append(max(vantagem))
    parada_de_dados.append(vantagem)


    if bonus != 0:
        retorno = f'As jogadas foram{parada_de_dados}. Final {rolagem_final} + {bonus}, Total {sum(rolagem_final) + bonus}'
    else:
        retorno = f'As jogadas foram{parada_de_dados}. Final {rolagem_final}, Total {sum(rolagem_final)}'

    return retorno


def desvantagem(bonus=0):
    """
    Função para resolver parada de dados de desvantagem

        :param desvantagem: Se a funão vantagem ésetada como True, são jogados 2 dados de 20 lados e o resultado é o menor
        :return: informação sobre a rolagem
    """
    global retorno
    from random import randint

    rolagem_final = []
    parada_de_dados = []

    dado1 = randint(1, 20)
    dado2 = randint(1, 20)
    vantagem = [dado1, dado2]
    rolagem_final.append(min(vantagem))
    parada_de_dados.append(vantagem)


    if bonus != 0:
        retorno = f'As jogadas foram{parada_de_dados}. Final {rolagem_final} + {bonus}, Total {sum(rolagem_final) + bonus}'
    else:
        retorno = f'As jogadas foram{parada_de_dados}. Final {rolagem_final}, Total {sum(rolagem_final)}'

    return retorno


def calcular_nd(nome = 'Indefinido', nd_pretendido=0, ca=0, pv=0, b_ataque=0, dano_rodada=0, dano_area = False, n_ataques =1, cd=0, vôo=False, resist=False, imunidade=False, ação_ardilosa=False, aparar=False, matilha = False):
    """
    Faciclita a criação ou verificação do nível de desafio de um oponente

        nome = Nome da criatura/npc a ser analizado
        nd_pretendido - Refere-se ao Nível de desafio base
        ca - Refere-se a Classe de Armadura
        pv - Refere-se aos Pontos de Vida
        b_ataque - Refere-se ao Bônus de Ataque
        dano_rodada - Refere-se a quantidade máxima de dano causado
        dano_area - Refere-se a capacidade de causar dano em área
        n_ataques - Refere-se ao Número de Ataques
        cd - Refere-se a Dificuldade para testesde resistência de uma habilidade
        vôo - Refere-se acapacidade de Vôo de uma criatura. Por padão está em False, se alterado para True a criatura tem movimentação de vôo.
        resist - Refere-se as resistências a dano de uma criatura. Por padrão está em False, se alterado para True a criatura possui resistências.
        imunidade - Refere-se a Imunidades de uma criatura. Por padrão está em False, se alterado para True a criatura possui imunidade.
        ação_ardilosa - Refere-se ao bônus referente a uma Ação Ardilosa de uma criatura. Por padão está em False, se alterado para True a criatura possui esta habilidade.
        aparar- Refere-se a caacidade de usar a reação Aparar uma criatura. Por padão está em False, se alterado para True a criatura possui esta habilidade.
        matilha - Refere-se ao bônus referente a ataques em grupo de uma criatura. Por padão está em False, se alterado para True a criatura possui esta habilidade.

    """
    from random import randint
    from math import floor
    nd_defensivo = nd_ofensivo = nd_resultante = 0
    #Nd de Referência do Livro
    nd_livro = [  {'ND': 0, 'Proef': 2, "CA": 13, 'PV': randint(1, 6), 'Pvmin': 1, 'Pvmax': 6, 'Bônus Ataque': 3, 'Dano Rodada': randint(0, 1), 'Danomin': 0, 'Danomax': 1,'CD': 13},
        {'ND': 1/8, 'Proef': 2, "CA": 13, 'PV': randint(7, 35), 'Pvmin': 7, 'Pvmax': 35,'Bônus Ataque': 3, 'Dano Rodada': randint(2, 3),'Danomin': 2, 'Danomax': 3, 'CD': 13},
        {'ND': 1/4, 'Proef': 2, "CA": 13, 'PV': randint(36, 49), 'Pvmin': 36, 'Pvmax': 49,'Bônus Ataque': 3, 'Dano Rodada': randint(4, 5), 'Danomin': 4, 'Danomax': 5,'CD': 13},
        {'ND': 1/2, 'Proef': 2, "CA": 13, 'PV': randint(50, 70), 'Pvmin': 50, 'Pvmax': 70,'Bônus Ataque': 3, 'Dano Rodada': randint(6, 8), 'Danomin': 6, 'Danomax': 8,'CD': 13},
        {'ND': 1, 'Proef': 2, "CA": 13, 'PV': randint(71, 85), 'Pvmin': 71, 'Pvmax': 85,'Bônus Ataque': 3, 'Dano Rodada': randint(9, 14), 'Danomin': 9, 'Danomax': 14,'CD': 13},
        {'ND': 2, 'Proef': 2, "CA": 13, 'PV': randint(86, 100), 'Pvmin': 86, 'Pvmax': 100,'Bônus Ataque': 3, 'Dano Rodada': randint(15, 20), 'Danomin': 15, 'Danomax': 20,'CD': 13},
        {'ND': 3, 'Proef': 2, "CA": 13, 'PV': randint(101, 115), 'Pvmin': 101, 'Pvmax': 115,'Bônus Ataque': 4, 'Dano Rodada': randint(21, 26), 'Danomin': 21, 'Danomax': 26,'CD': 13},
        {'ND': 4, 'Proef': 2, "CA": 14, 'PV': randint(116, 130), 'Pvmin': 116, 'Pvmax': 130,'Bônus Ataque': 5, 'Dano Rodada': randint(27, 32), 'Danomin': 27, 'Danomax': 32,'CD': 14},
        {'ND': 5, 'Proef': 3, "CA": 15, 'PV': randint(131, 145), 'Pvmin': 131, 'Pvmax': 145,'Bônus Ataque': 6, 'Dano Rodada': randint(33, 38), 'Danomin': 33, 'Danomax': 38,'CD': 15},
        {'ND': 6, 'Proef': 3, "CA": 15, 'PV': randint(146, 160), 'Pvmin': 146, 'Pvmax': 160,'Bônus Ataque': 6, 'Dano Rodada': randint(39, 44), 'Danomin': 39, 'Danomax': 44,'CD': 15},
        {'ND': 7, 'Proef': 3, "CA": 15, 'PV': randint(161, 175), 'Pvmin': 161, 'Pvmax': 175,'Bônus Ataque': 6, 'Dano Rodada': randint(45, 50), 'Danomin': 45, 'Danomax': 50,'CD': 15},
        {'ND': 8, 'Proef': 3, "CA": 16, 'PV': randint(176, 190), 'Pvmin': 176, 'Pvmax': 190,'Bônus Ataque': 7, 'Dano Rodada': randint(51, 56), 'Danomin': 51, 'Danomax': 56,'CD': 16},
        {'ND': 9, 'Proef': 4, "CA": 16, 'PV': randint(191, 205), 'Pvmin': 191, 'Pvmax': 205,'Bônus Ataque': 7, 'Dano Rodada': randint(57, 62), 'Danomin': 57, 'Danomax': 62,'CD': 16},
        {'ND': 10, 'Proef': 4, "CA": 17, 'PV': randint(206, 220), 'Pvmin': 206, 'Pvmax': 220,'Bônus Ataque': 7, 'Dano Rodada': randint(63, 68), 'Danomin': 63, 'Danomax': 68,'CD': 16},
        {'ND': 11, 'Proef': +4, "CA": 17, 'PV': randint(221, 235), 'Pvmin': 221, 'Pvmax': 235,'Bônus Ataque': 8, 'Dano Rodada': randint(69, 74), 'Danomin': 69, 'Danomax': 74,'CD': 17},
        {'ND': 12, 'Proef': +4, "CA": 17, 'PV': randint(236, 250), 'Pvmin': 236, 'Pvmax': 250,'Bônus Ataque': 8, 'Dano Rodada': randint(75, 80), 'Danomin': 75, 'Danomax': 80,'CD': 17},
        {'ND': 13, 'Proef': +5, "CA": 18, 'PV': randint(251, 265), 'Pvmin': 251, 'Pvmax': 265,'Bônus Ataque': 8, 'Dano Rodada': randint(81, 86), 'Danomin': 81, 'Danomax': 86,'CD': 18},
        {'ND': 14, 'Proef': +5, "CA": 18, 'PV': randint(266, 280), 'Pvmin': 266, 'Pvmax': 280,'Bônus Ataque': 8, 'Dano Rodada': randint(87, 92), 'Danomin': 87, 'Danomax': 92,'CD': 18},
        {'ND': 15, 'Proef': +5, "CA": 18, 'PV': randint(281, 295), 'Pvmin': 281, 'Pvmax': 295,'Bônus Ataque': 8, 'Dano Rodada': randint(93, 98), 'Danomin': 93, 'Danomax': 98,'CD': 18},
        {'ND': 16, 'Proef': +5, "CA": 18, 'PV': randint(296, 310), 'Pvmin': 296, 'Pvmax': 310,'Bônus Ataque': 9, 'Dano Rodada': randint(99, 104), 'Danomin': 99, 'Danomax': 104,'CD': 18},
        {'ND': 17, 'Proef': +6, "CA": 19, 'PV': randint(311, 325), 'Pvmin': 311, 'Pvmax': 325,'Bônus Ataque': 10, 'Dano Rodada': randint(105, 110), 'Danomin': 105, 'Danomax': 110,'CD': 19},
        {'ND': 18, 'Proef': +6, "CA": 19, 'PV': randint(326, 340), 'Pvmin': 326, 'Pvmax': 340,'Bônus Ataque': 10, 'Dano Rodada': randint(111, 116), 'Danomin': 111, 'Danomax': 116,'CD': 19},
        {'ND': 19, 'Proef': +6, "CA": 19, 'PV': randint(341, 355), 'Pvmin': 341, 'Pvmax': 355,'Bônus Ataque': 10, 'Dano Rodada': randint(117, 122), 'Danomin': 117, 'Danomax': 122,'CD': 19},
        {'ND': 20, 'Proef': +6, "CA": 19, 'PV': randint(356, 400), 'Pvmin': 356, 'Pvmax': 400,'Bônus Ataque': 10, 'Dano Rodada': randint(123, 140), 'Danomin': 123, 'Danomax': 140,'CD': 19},
        {'ND': 21, 'Proef': +7, "CA": 19, 'PV': randint(401, 445), 'Pvmin': 401, 'Pvmax': 445,'Bônus Ataque': 11, 'Dano Rodada': randint(141, 158), 'Danomin': 141, 'Danomax': 158,'CD': 20},
        {'ND': 22, 'Proef': +7, "CA": 19, 'PV': randint(446, 490), 'Pvmin': 446, 'Pvmax': 490,'Bônus Ataque': 11, 'Dano Rodada': randint(159, 176), 'Danomin': 159, 'Danomax': 176,'CD': 20},
        {'ND': 23, 'Proef': +7, "CA": 19, 'PV': randint(491, 535), 'Pvmin': 491, 'Pvmax': 535,'Bônus Ataque': 11, 'Dano Rodada': randint(177, 194), 'Danomin': 177, 'Danomax': 194,'CD': 20},
        {'ND': 24, 'Proef': +7, "CA": 19, 'PV': randint(536, 580), 'Pvmin': 536, 'Pvmax': 580,'Bônus Ataque': 11, 'Dano Rodada': randint(195, 212), 'Danomin': 195, 'Danomax': 212,'CD': 21},
        {'ND': 25, 'Proef': +8, "CA": 19, 'PV': randint(581, 625), 'Pvmin': 581, 'Pvmax': 625,'Bônus Ataque': 12, 'Dano Rodada': randint(213, 230), 'Danomin': 213, 'Danomax': 230,'CD': 21},
        {'ND': 26, 'Proef': +8, "CA": 19, 'PV': randint(626, 670), 'Pvmin': 626, 'Pvmax': 670,'Bônus Ataque': 12, 'Dano Rodada': randint(231, 248), 'Danomin': 231, 'Danomax': 248,'CD': 21},
        {'ND': 27, 'Proef': +8, "CA": 19, 'PV': randint(671, 715), 'Pvmin': 671, 'Pvmax': 715,'Bônus Ataque': 13, 'Dano Rodada': randint(249, 266), 'Danomin': 249, 'Danomax': 266,'CD': 22},
        {'ND': 28, 'Proef': +8, "CA": 19, 'PV': randint(716, 760), 'Pvmin': 715, 'Pvmax': 760,'Bônus Ataque': 13, 'Dano Rodada': randint(267, 284), 'Danomin': 267, 'Danomax': 284,'CD': 22},
        {'ND': 29, 'Proef': +9, "CA": 19, 'PV': randint(761, 805), 'Pvmin': 761, 'Pvmax': 805,'Bônus Ataque': 13, 'Dano Rodada': randint(285, 302), 'Danomin': 285, 'Danomax': 302,'CD': 22},
        {'ND': 30, 'Proef': +9, "CA": 19, 'PV': randint(806, 850), 'Pvmin': 806, 'Pvmax': 850,'Bônus Ataque': 14, 'Dano Rodada': randint(303, 320), 'Danomin': 303, 'Danomax': 320,'CD': 23},]
    # Setup do ND pretendido
    if nd_pretendido == 0:
        nd_pretendido = nd_livro[0]
    elif nd_pretendido == 1/8:
        nd_pretendido = nd_livro[1]
    elif nd_pretendido == 1/4:
        nd_pretendido = nd_livro[2]
    elif nd_pretendido == 1/2:
        nd_pretendido = nd_livro[3]
    elif nd_pretendido > 30:
        nd_pretendido = 30
        nd_pretendido = nd_livro[nd_pretendido+3]
    else:
        nd_pretendido = nd_livro[nd_pretendido+3]
    # Setup das informações contidas
    if ca == 0:
        ca = nd_pretendido['CA']
    if pv == 0:
        pv = nd_pretendido['PV']
    if b_ataque == 0:
        b_ataque = nd_pretendido['Bônus Ataque']
    if dano_rodada ==0:
        dano_rodada = nd_pretendido['Dano Rodada']
    if cd == 0:
        cd = nd_pretendido['CD']

    # Início das Análise das capacidades
    nd_defensivo = 0
    nd_ofensivo = 0

    #Teste CA
    if ca > nd_pretendido['CA']:
        nd_defensivo += floor((ca - nd_pretendido['CA'])/2)
    if ca < nd_pretendido['CA']:
        nd_defensivo -= floor((nd_pretendido['CA'] - ca)/2)
    if vôo == True:
        nd_defensivo += 1
    if ação_ardilosa == True:
        nd_defensivo += 2
    if aparar == True:
        nd_defensivo += 1

    # Teste Pv
    count_pv = 0
    pv_efetivo = pv
    # VULNERABILIDADE, RESISTÊNCIA E IMUNIDADE A DANO
    # Nível de Desafio Pretendido     Multiplicador de PV por Resistências    Multiplicador de PV por Imunidades
    # 1–4                                             X 2                               X 2
    # 5–10                                            X 1,5                             X 2
    # 11–16                                           X 1,25                           X 1,5
    # 17 ou maior                                     X 1                              X 1,25

    if resist == True:
        if 0 <= nd_pretendido['ND'] <= 4:
            pv_efetivo = pv * 2
        elif 5 <= nd_pretendido['ND'] <= 10:
            pv_efetivo = pv * 1.5
        elif 11 <= nd_pretendido['ND'] <= 16:
            pv_efetivo = pv * 1.25
        elif nd_pretendido['ND'] > 17:
            pv_efetivo = pv * 1

    if imunidade == True:
        if 0 <= nd_pretendido['ND'] <= 4:
            pv_efetivo = pv * 2
        elif 5 <= nd_pretendido['ND'] <= 10:
            pv_efetivo = pv * 2
        elif 11 <= nd_pretendido['ND'] <= 16:
            pv_efetivo = pv * 1.5
        elif nd_pretendido['ND'] > 17:
            pv_efetivo = pv * 1.25

    if nd_pretendido['Pvmin']> pv_efetivo or pv_efetivo > nd_pretendido['Pvmax']:
        for c in  nd_livro:
            if c['Pvmin']<= pv_efetivo <= c['Pvmax']:
                if nd_pretendido['ND'] < c['ND']:
                    nd_defensivo += (c['ND'] - nd_pretendido['ND'])
                if nd_pretendido['ND'] > c['ND']:
                    if c['ND']==0 :
                        nd_defensivo -= (nd_pretendido['ND']) +4
                    elif count_pv == 1 :
                        nd_defensivo -= (nd_pretendido['ND']) +3
                    elif count_pv == 2 :
                        nd_defensivo -= (nd_pretendido['ND']) +2
                    elif count_pv == 3 :
                        nd_defensivo -= (nd_pretendido['ND']) +1
                    elif count_pv >= 4:
                        nd_defensivo -= (nd_pretendido['ND'] - c['ND'])
            count_pv +=1

    # Teste Ataque
    if matilha ==True:
        nd_ofensivo +=1

    if b_ataque > nd_pretendido['Bônus Ataque']:
        nd_ofensivo += floor((b_ataque - nd_pretendido['Bônus Ataque']) / 2)
    if b_ataque < nd_pretendido['Bônus Ataque']:
        b_ataque -= floor((nd_pretendido['Bônus Ataque'] - b_ataque) / 2)
    # Teste Dano 'Danomin' 'Danomax'
    count_dano = 0
    if nd_pretendido['Danomin']> dano_rodada or pv > nd_pretendido['Danomax']:
        for c in  nd_livro:
            if c['Danomin']<= dano_rodada <= c['Danomax']:
                if nd_pretendido['ND'] < c['ND']:
                    nd_ofensivo += (c['ND'] - nd_pretendido['ND'])
                if nd_pretendido['ND'] > c['ND']:
                    if c['ND']==0 :
                        nd_ofensivo -= (nd_pretendido['ND']) +4
                    elif count_dano == 1 :
                        nd_ofensivo -= (nd_pretendido['ND']) +3
                    elif count_dano == 2 :
                        nd_ofensivo -= (nd_pretendido['ND']) +2
                    elif count_dano == 3 :
                        nd_ofensivo -= (nd_pretendido['ND']) +1
                    elif count_dano >= 4:
                        nd_ofensivo -= (nd_pretendido['ND'] - c['ND'])
            count_dano +=1
    # Teste CD
    if cd > nd_pretendido['CD']:
        nd_ofensivo += (cd - nd_pretendido['CD'])
    if cd < nd_pretendido['CD']:
        b_ataque -= (nd_pretendido['CD'] - cd)

    #Resultados
    nd_resultante = floor(((nd_ofensivo + nd_defensivo) / 2) + nd_pretendido['ND'])
    if nd_resultante == 0:
        nd_resultante = nd_livro[0]
    elif nd_resultante == 1/8:
        nd_resultante = nd_livro[1]
    elif nd_resultante == 1/4:
        nd_resultante = nd_livro[2]
    elif nd_resultante == 1/2:
        nd_resultante = nd_livro[3]
    elif nd_resultante > 30:
        nd_resultante = 30
        nd_resultante = nd_livro[nd_resultante+3]
    else:
        nd_resultante = nd_livro[nd_resultante+3]
    #Criação do Retorno
    criação = {'Nome': nome, 'CA':ca, 'PV': pv, 'Proeficiência': nd_resultante['Proef'], 'Bônus Ataque': b_ataque,
               'Dano Rodada': dano_rodada, 'Números de ataques': n_ataques, 'Dano por ataque': dano_rodada/n_ataques,
               'CD': cd}
    if  dano_area == True:
        criação['Dano em área']= floor(dano_rodada/2)
    if vôo == True:
        criação['Vôo'] = 'Ativo'
    if resist == True:
        criação['Resistência'] = 'Ativo'
    if imunidade == True:
        criação['Imunidade'] = 'Ativo'
    if ação_ardilosa == True:
        criação['Ação Ardilosa'] = 'Ativo'
    if aparar == True:
        criação['Aparar'] = 'Ativo'
    if matilha == True:
        criação['Matilha'] = 'Ativo'
    criação['ND'] = nd_resultante['ND']

    return criação


def npc(nd =0 ,nome_npc="", raça = '', tendencia='', força = 0 ,destreza = 0, constituição = 0, inteligencia = 0 ,sabedoria = 0 , carisma = 0, ca = 0, pv = 0, magia =False, classe = '', cd = 0 ):
    from random import randint, sample
    from math import floor
    if nd ==0:
        nd = randint(0, 5)
    nd = livro_nd(nd)

    if nome_npc =='':
        nome_npc = nome_aleatório()
    if raça == '':
        raça = raça_aleatória()
    if tendencia =='':
        tendencia = tendência_aleatória()
    personagem = nome_npc
    atributos = gerar_atributos(força, destreza, constituição, inteligencia, sabedoria, carisma)
    força= atributos['Força'][0]
    bfor= atributos['Força'][1]
    destreza= atributos['Destreza'][0]
    bdes = atributos['Destreza'][1]
    constituição= atributos['Constituição'][0]
    bcon = atributos['Constituição'][1]
    inteligencia= atributos['Inteligência'][0]
    bint = atributos['Inteligência'][1]
    sabedoria= atributos['Sabedoria'][0]
    bsab = atributos['Sabedoria'][1]
    carisma= atributos['Carisma'][0]
    bcar = atributos['Carisma'][1]
    proef = nd['Proef']

    if ca == 0:
        ca = randint(nd['CA']-1, nd['CA']+2)
    if pv == 0:
        pv = nd['PV']
    if cd == 0:
        cd = nd['CD']

    save = saves_aleatorios(proef= nd['Proef'] , bfor= atributos['Força'][1] , bdes=atributos['Destreza'][1], bcon=atributos['Constituição'][1], bint=atributos['Inteligência'][1], bsab=atributos['Sabedoria'][1], bcar=atributos['Carisma'][1])

    perícias = pericias_aleatorias(proef= nd['Proef'] , bfor= atributos['Força'][1] , bdes=atributos['Destreza'][1], bcon=atributos['Constituição'][1], bint=atributos['Inteligência'][1], bsab=atributos['Sabedoria'][1], bcar=atributos['Carisma'][1])

    n_de_ataques = floor(nd['Dano Rodada']/7)

    bônusataque = bonusdano = 0
    if n_de_ataques >3:
        n_de_ataques = floor(nd['Dano Rodada']/12)
        bônusataque = 2
        bonusdano = 4
        if n_de_ataques > 3:
            n_de_ataques = floor(nd['Dano Rodada']/16)
            bônusataque = 4
            bonusdano = 8

    if bônusataque > 0:
        ataques = ataques_aleatorios(proef=nd['Proef'], bfor=atributos['Força'][1], bdes=atributos['Destreza'][1], bônusataque= bônusataque , bonusdano= bonusdano)
    else:
        ataques =ataques_aleatorios(proef= nd['Proef'] , bfor= atributos['Força'][1] , bdes=atributos['Destreza'][1])

    if magia:
        if classe == '':
            feitiços = aptidão_mágica(magia=True)
        else:
            feitiços = aptidão_mágica(magia=True, classe = classe)
    else:
        feitiços = aptidão_mágica()

    npc_gerado = {'Nome': personagem,
                  'Raça': raça,
                  'Tendência': tendencia,
                  'Proeficiência': nd['Proef'],
                  'PV': pv,
                  'Classe de Armadura': ca,
                  'Atributos': {'Força': [força, (força - 10) // 2],
                  'Destreza': [destreza, (destreza - 10) // 2],
                  'Constituição': [constituição, (constituição - 10) // 2],
                  'Inteligência': [inteligencia, (inteligencia - 10) // 2],
                  'Sabedoria': [sabedoria, (sabedoria - 10) // 2],
                  'Carisma': [carisma, (carisma - 10) // 2]},
                  'Saves': save,
                  'Perícias': perícias,
                  'Número de ataques': n_de_ataques,
                  'Ataque1': ataques['Ataque1'],
                  'Ataque2': ataques['Ataque2'],
                  'CD': cd}

    nd = calcular_nd(nome=npc_gerado['Nome'], nd_pretendido=1, pv=npc_gerado['PV'], ca=npc_gerado['Classe de Armadura'],
                     b_ataque= max(nd['Proef'] + bfor + bônusataque, nd['Proef'] + bdes + bônusataque), dano_rodada=npc_gerado['Número de ataques']*(6+bonusdano))

    if feitiços['Aptidão Mágica'] == 15:
        npc_gerado['Tipo de magia'] = feitiços['Classe']
        npc_gerado['Truques'] = feitiços['Truques']
        if feitiços['Magias1'] > 0:
            npc_gerado['1° Círculo'] = feitiços['Magias1']
            if feitiços['Magias2']> 0:
                npc_gerado['2° Círculo'] =  feitiços['Magias2']
                if feitiços['Magias3']> 0:
                    npc_gerado['3° Círculo'] =  feitiços['Magias3']
                    if feitiços['Magias4'] > 0:
                        npc_gerado['4° Círculo'] = feitiços['Magias4']
                        if feitiços['Magias5'] > 0:
                            npc_gerado['5° Círculo'] = feitiços['Magias5']

    npc_gerado['ND'] = nd['ND']
    return npc_gerado



