from random import choice, choices, randint, random, sample, shuffle


def npc(nome_npc=""):

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

    raças = ['Humano', 'Humano', 'Humano', 'Humano', 'Humano', 'Humano', 'Humano', 'Humano', 'Humano', 'Humano', 'Elfo', 'Elfo',
             'Elfo', 'Elfo', 'Meio-elfo', 'Anão', 'Anão', 'Anão', 'Draconato', 'Gnomo', 'Gnomo', 'Halfling', 'Halfling',
             'Tiefling', 'Meio-Orc', 'Orc', 'Genasi', 'Goblin']
    raçasaleatoria = sample(raças, k=len(raças))
    tendência = ['Caótico e bom', 'Caótico e neutro', 'Caótico e mal', 'Neutro e bom', 'Neutro e neutro', 'Neutro e mal',
                 'Leal e bom', 'Leal e neutro', 'Leal e mal']
    tendenciaaleatoria = sample(tendência, k=len(tendência))

    # print(len(nome)) = 383
    nomelen = int(len(nome))

    personagem = nomealeatorio[0:2]
    if nome_npc != "":
        nome_npc = personagem
    força = destreza = constituição = inteligencia = sabedoria = carisma = 0

    ca = randint(10, 18)
    pv = randint(3, 30)

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

    proef = 2

    bfor = (força - 10) // 2
    bdes = (destreza - 10) // 2
    bcon = (constituição - 10) // 2
    bint = (inteligencia - 10) // 2
    bsab = (sabedoria - 10) // 2
    bcar = (carisma - 10) // 2

    save = [f'For {bfor + proef}', f'Des {bdes + proef}', f'Cons {bcon + proef}', f'Int {bint + proef}',
            f'Sab {bsab + proef}', f'Car {bcar + proef}']
    savelen = 5

    # randomizar lista de saves
    savesaleatorios = sample(save, k=len(save))
    todaspericias = [f'Acrobacia {bdes + proef}', f'Adestrar Animais {bsab + proef}', f'Arcanismo {bint + proef}',
                     f'Atletismo {bfor + proef}', f'Enganação {bcar + proef}', f'Furtividade {bdes + proef}',
                     f'História {bint + proef}', f'Intimidação {bcar + proef}', f'Intuição {bsab + proef}',
                     f'Investigação {bint + proef}',
                     f'Medicina {bsab + proef}', f'Natureza {bint + proef}', f'Percepção {bsab + proef}',
                     f'Performance {bcar + proef}', f'Persuasão {bcar + proef}',
                     f'Prestidigitação {bdes + proef}', f'Religião {bint + proef}', f'Sobrevivência {bsab + proef}']
    # randomizar lista de pericias
    periciasaleatorias = sample(todaspericias, k=len(todaspericias))

    armaslista = [f'Adaga. Ataque Corpo-a-Corpo ou a distância com Arma: +{proef + bdes} para atingir, alcance 6/18 m, um alvo.Acerto: {bdes + 3}(1d4 + {bdes}) de dano perfurante.',
                  f'Lança. Ataque Corpo-a-Corpo ou a distância com Arma: +{proef + bdes} para atingir, alcance 6/18 m, um alvo.Acerto: {bdes + 5}(1d8 + {bdes}) de dano perfurante.',
                  f'Espada Curta. Ataque Corpo-a-Corpo com Arma: +{proef+bfor} para atingir, alcance 1,5m, um alvo.Acerto: {bfor+4}(1d6 + {bfor}) de dano perfurante.',
                  f'Maça. Ataque Corpo-a-Corpo com Arma: +{proef + bfor} para atingir, alcance 1,5m, um alvo.Acerto: {bfor + 4}(1d6 + {bfor}) de dano contundente.',
                  f'Espada Longa. Ataque Corpo-a-Corpo com Arma: +{proef + bfor} para atingir, alcance 1,5m, um alvo.Acerto: {bfor + 5}(1d8 + {bfor}) de dano perfurante.',
                  f'Arco Longo.Ataque à Distância com Arma: +{proef+bdes} para atingir, distância 45 / 180m, um alvo.Acerto: {5+bdes}(1d8 + {bdes}) de dano perfurante.']
    ataques = sample(armaslista, k=len(armaslista))

    aptidão_magica = randint(1, 15)
    if aptidão_magica == 15 and inteligencia > 7:
        truques = randint(1, 3)
        magias1 = randint(0, 3)
        if magias1 > 1:
            magias2 = (randint(0, 2))
            if magias2 > 1:
                magias3 = randint(0, 1)
        caster = randint(1, 5)
        tipomagico = ''
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

    npc_gerado = {'Nome': personagem,
                  'Raça': raçasaleatoria[0:1],
                  'Tendência': tendenciaaleatoria[0:1],
                  'PV': pv+bcon,
                  'Classe de Armadura': ca+bdes,
                  'Força': força,
                  'Bônus Força': (força - 10) // 2,
                  'Destreza': destreza,
                  'Bônus Destreza': (destreza - 10) // 2,
                  'Constituição': constituição,
                  'Bônus de Constituição': (constituição - 10) // 2,
                  'Inteligência': inteligencia,
                  'Bônus Inteligencia': (inteligencia - 10) // 2,
                  'Sabedoria': sabedoria,
                  'Bônus Sabedoria': (sabedoria - 10) // 2,
                  'Carisma': carisma,
                  'Bônus de Carisma': (carisma - 10) // 2,
                  'Saves': savesaleatorios[0:randint(2, 3)],
                  'Perícias': periciasaleatorias[0: randint(2, 3)],
                  'Ataque1': ataques[0:1],
                  'Ataque2': ataques[2:3]}

    if aptidão_magica == 15:
        npc_gerado['Tipo de magia'] = tipomagico
        npc_gerado['Truques'] = truques
        if magias1 > 1:
            npc_gerado['1Círculo'] = magias1
            if magias2 > 1:
                npc_gerado['2Círculo'] = magias2
                if magias3 > 1:
                    npc_gerado['3Círculo'] = magias3
    return npc_gerado
