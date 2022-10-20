import geopandas as gpd
import matplotlib.pyplot as plt
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel, LdaModel
import pickle


def determineComuna(text, nlp, com_matcher, matcher, dic_prority, dic_loc_comunes):
    if not isinstance(text, str):
        print("Warning with text:", type(text), text)
        return ""
    doc = nlp(text.lower())

    # Primero intentar match exacto con comunas de Los Lagos
    matches = com_matcher(doc)
    counterd = {}
    for match_tag, start, end in matches:
        text = doc[start:end].text  # The matched span text
        if text in counterd:
            counterd[text] += 1
        else:
            counterd[text] = 1
    counterd = dict(sorted(counterd.items(), key=lambda x: x[1], reverse=True))
    for comuna, _ in counterd.items():
        return comuna

    # Ahora intenta con los filtros más complejos
    #       (requiere re-procesar el texto)
    rawmatches = matcher(doc)
    rmatches = {}
    matches = []

    # Adds a priority value to sort
    for match_id, a, b in rawmatches:
        match_tag = nlp.vocab.strings[match_id]
        priority = getPriority(match_tag, dic_prority)
        matches.append([match_tag, a, b, priority])
    matches = sorted(matches, key=lambda x: x[3], reverse=True)

    for match_tag, start, end, _ in matches:
        text = doc[start:end].text  # The matched span text
        # print(text)

        if match_tag == "regiones_conocidas":
            # Asumiré las noticias regionales para las capitales
            if "agos" in text:  # Los Lagos
                return "puerto montt"
            else:  # Los Ríos
                return "valdivia"
        elif match_tag == "cerca_ptomontt":
            return "puerto montt"
        elif match_tag in ["comuna", "region"]:
            if "de" in text:
                append_token = [text, doc[end].text]  # comuna de xxxx
                if doc[end].text in ["las", "los", "la", "el", "lo", "san", "puente", "del"]:  # comuna de los
                    end += 1
                    append_token.append(doc[end].text)  # comuna de los xxxx
                if doc[end].text in ["río"]:  # comuna de río
                    end += 1
                    append_token.append(doc[end].text)  # comuna de río xxxx
                return " ".join(append_token)
            else:
                return "puerto montt"  # Para casos como "de la comuna", refiriéndose a Pto. Montt
        elif match_tag == "localidades_comunes":
            return dic_loc_comunes[text]
        elif match_tag == "chile":
            return "chile"
    return ""


def dfUpdateComunas(df, nlp, com_matcher, matcher, dic_prority, dic_loc_comunes):
    res = df["text"].apply(determineComuna, args=[
                           nlp, com_matcher, matcher, dic_prority, dic_loc_comunes])
    df["comuna"] = res
    return df


def getPriority(tag, dic_prority):
    if tag in dic_prority:
        return dic_prority[tag]
    return 0


def territory_map(id_region: int = 10):
    # fuente: https://www.bcn.cl/siit/mapas_vectoriales
    territory = gpd.read_file(r'../shape/comunas.shp', encoding='utf-8')

    # Filtramos segun id_region: Ejemplo 14 para la region XIV (Los Rios)
    territory = territory[territory["codregion"] == id_region]

    # Obtenemos los datos de las Columnas "Comuna", "geometry"
    territory = territory[["Comuna", "geometry"]]

    return territory


def save_map(df, territory, image_name: str = "Mapa_Calor"):

    # Junta las tablas df y Pais
    territory = territory.merge(df, on="Comuna")

    # Inicializa matplotlib para la creacion del mapa
    fig, ax = plt.subplots(1, 1)
    max_presente = df.max()[1]  # valore maximo para la barra de calor
    territory.plot(column='Valor', ax=ax, edgecolor="gray",
                   cmap='OrRd', legend=False).set_axis_off()
    bar_info = plt.cm.ScalarMappable(
        cmap="Reds", norm=plt.Normalize(vmin=0, vmax=max_presente))
    bar_info._A = []
    cbar = fig.colorbar(bar_info)

    # Guardar imagen en nombre_imagen
    plt.savefig('.//{}.svg'.format(image_name),
                bbox_inches="tight", transparent=True)

### NO CAMBIAR ESTA CELDA###


def compute_coherence_values(dictionary, corpus, texts, limit, start=2, step=3):
    """
    Compute c_v coherence for various number of topics

    Parameters:
    ---------u
    dictionary : Gensim dictionary
    corpus : Gensim corpus
    texts : List of input texts
    limit : Max num of topics

    Returns:
    -------
    model_list : List of LDA topic models
    coherence_values : Coherence values corresponding to the LDA model with respective number of topics
    """
    coherence_values = []
    model_list = []
    for num_topics in range(start, limit, step):
        # print(num_topics)

        model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                                id2word=dictionary,
                                                num_topics=num_topics,
                                                random_state=100,
                                                update_every=1,
                                                chunksize=100,
                                                passes=10,
                                                alpha='auto',
                                                per_word_topics=True)

        model_list.append(model)
        coherencemodel = CoherenceModel(
            model=model, texts=texts, dictionary=dictionary, coherence='c_v')
        coherence_values.append(coherencemodel.get_coherence())
    return [model_list, coherence_values]


def text_to_list(noticia, nlp, matcher):
    list_of_words = []

    try:
        doc = nlp(noticia)

        for token in doc:
            if (token.pos_ == "NOUN"):
                list_of_words.append(token.text)

        for ent in doc.ents:
            if (ent.label_ == "PER" and " " in ent.text):
                list_of_words.append(ent.text)

        matches = matcher(doc)

        for match_id, start, end in matches:
            span = doc[start:end]  # The matched span
            list_of_words.append(span.text)

    except Exception as e:
        print(e)
        print("Noticia:\n", noticia)

    return list_of_words


def openModels(comunas):
    models = {}
    id2ws = {}
    datas = {}
    for comuna in comunas:
        try:
            model = LdaModel.load(f"./modelos/{comuna}", mmap='r')
            #print("Founded", comuna)
            models[comuna] = model

            id2word = corpora.Dictionary.load(f"./modelos/{comuna}.id2word")
            id2ws[comuna] = id2word

            dataset = pickle.load(open(f"./modelos/{comuna}_dataset", 'rb'))
            datas[comuna] = dataset
        except:
            print(comuna, "not founded")
    return [models, id2ws, datas]
