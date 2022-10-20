# Tarea 01: Análisis de Tópicos comunales
### INFO279 - Tratamiento Automático del Lenguaje (TAL)

En esta tarea se compone de un notebook con los códigos necesarios para realizar el procesamiento de los textos y la elección de los mejores modelos, los cuales son escogidos de acuerdo a su mejor valor de coherencia y la cantidad total de noticias (evitando que coincidan siempre que sea posible).

__Análisis general__:
> Dentro de los tópicos encontrados queda bastante clara la similitud de tópicos entre la mayoría de comunas en Chiloé. Aquí también es bastante común que se nombre a las vías y peajes.
> En general, las palabras más interesantes para identificar problemáticas parecen ser: "necesidad", "problema", "consejeros", "dirigentes", "luz", "viviendas", "campamentos", , "imputado". En esta misma línea, quizá se podría tener una lista previamente creada con conceptos claves, principalmente en el ámbito delictual (como para identificar autoridades que se han involucrado en algún delito) y sus diversas maneras de realizarse, considerando también por ejemplo los delitos ambientales.
> Los tópicos relacionados con el COVID suelen clasificarse con separaciones bastante claras, como por ejemplo las noticias que se refieren a los contagios y las que se refieren a vacunación. También hay tópicos relacionados con cambio de fase en el plan paso a paso, el uso de camas críticas o ventiladores, y la actualización de protocolos.
> Respecto a la elección de los mejores modelos de acuerdo a su métrica de coherencia, parece ser que por sobre el valor (0.5) los tópicos son bastante robustos individualmente, por lo que podría ser mejor opción escoger una menor cantidad de tópicos (sacrificando un poco de coherencia).

__Análisis detallado__:
> A continuación se detallan los tópicos por regiones, las cuales en su título indican la cantidad de noticias clasificadas para la comuna. En el listado que se les añade solo se nombrarán los tópicos más relevantes (no todos).

"ancud" (69):
1. dosis - años (20%) - hechos - tribunales
2. agua(s) - camiones - crisis - ficha
3. obras - obras complementarias - licitación - observaciones - retrasos - hospital
4. casos - camas - ventilación mecánica - cuidados intensivos
5. personas en situación de calle

"castro" (144):
1. camas - red - provincia - ventilación mecánica - virus - coronavirus
2. noche - delitos - artistas - alcohol
3. millones - pesos - peaje - ruta - inversión
5. servicios - denuncia - compras - espera - hospital - sumario
6. mujer - víctima - kilos - gravedad - falta
7. curso - pérdida - asilo - cuidado - refugio
8. investigación - joven - homicidio
> En Castro destacan varios crímenes cometidos, lo que se podría correlacionar a la existencia de alguna entidad de justicia en esta ciudad (ya que además es capital).

"chonchi" (23):
1. proyecto - millones - obras - conservación - agricultores - alcalde
1. vía - peaje - salida - sur - ministros - recursos
1. accidente - personas - accidente de tránsito
1. bomberos - carro - millones - materiales - carro multipropósito
1. educación - estudiantes - articulación - convenio - instituciones - especialidad

> En Chonchi parecen encontrarse tópicos redundantes de las inversiones viales, que podrían simplificarse en uno solo. También destaca la inversión en diversas áreas.
    
"curaco de vélez" (12):
1. rezadoras/es - herramientas - patrimonio
2. familias - niños - computadores - clases - casas - pandemia
3. curso - personas - capacitación
> Usando 6 tópicos se observa que el ámbito educacional es lo más nombrado, y se refiere a temas como las clases en casa durante pandemia, y cursos de capacitación.

"dalcahue" (14):
1. millones de pesos - sindicato - turismo - pesca artesanal - organización - cultivo - fomento - proyectos
1. estudiantes - conectividad - tecnología - educación
1. residuos - comunidad - valorización - campaña - manejo
1. vehículos - ruta - accidente - corte - horas
1. mujeres - pesca artesanal - programa - emprendimientos 

> Aquí lo relevante es identificar que hay interés por realizar campañas sobre el uso de residuos, o que un accidente que hubo provocó un corte en la carretera. Parecen sobras al menos dos temas. 

"puqueldón" (5):
> Todas las noticias parecen hablar de COVID, a pesar de que únicamente hay dos tópicos.

"queilén":
> No hay noticias de esta comuna.

"quemchi" (5):
1. trabajos - árbol - predio - muerte - cuerpo
2. construcción - pozo

"quellón" (45):
1. proyecto - isla - energía - calidad - niños
2. dosis - vacunas - mamá
3. vía - peaje - soluciones - licitación
4. casos - salud -  coronavirus
5. vehículo - conductor - víctima
6. hospital - equipos

> Muchos de los tópicos encontrados representaban a un pequeño % del los datos, por lo que aquí también podría haberse reducido la cantidad de tópicos.

"quinchao" (6):
1. casos nuevos - región
2. camas - pandemia

"calbuco" (11):
1. gente - luz - vida - pescadores - contaminación - dirigentes
2. agua - municipio - auditoría
3. clientes - lluvia
> Se identifica claramente un tópico relacionado a la solución de un conflicto y/o implementación a la comunidad. Las palabras "dirigentes" o "auditoria" parecen indicar bastante potencial de importancia.
> También contiene tópicos redundantes que podrían simplificarse en uno.

"cochamó" (11):
1. directora - turismo
2. ruta - situación - acuerdo
3. electricidad - vecinos - consejeros - necesidad - dirigentes
4. millones - obras
5. turismo - implementación - caminos - infraestructura

"fresia" (20):
1. alcalde - entrevista
2. salud - tratamiento - propuesta - casos
3. fase - cuarentena

> La mayoría de tópicos parecen hablar de COVID - pandemia, y algunos son bastante pequeños. También se debería reducir la cantidad de tópicos.

"frutillar" (20):
1. región - gobernador - candidato - vuelta - elección
2. viviendas - conjunta - comuna

> Aquí se podría deducir bastante información respecto a los candidatos para gobernador y los temas que estos han conversado con los medios (en forma de palabras claves). Muchos de los otros temas son pequeños y parecen sobrar.

"llanquihue" (84):
1. concejal - imputado - detención - investigación
1. vacunación - dosis
1. casos - provincia - contagios
1. pesca - capacidad - playa - comercio - praderas

"los muermos" (8):
1. niños - comuna - juego - región - patrimonio
2. danza - comunidad
3. jardines - infraestructura - problemas

> Se identifica un problema de infraestructura en jardines. Algunos tópicos también parecen redundantes

"maullín":
> No hay noticias de esta comuna.

"puerto montt" (310):
1. acuerdo - seguridad - pandemia - parte - vuelta - fase
1. personas - sector - conectividad
1. vacunación - camas - red - contagios
1. aspecto - movilidad - palabras - revisión - líder - dirigente - droga - gerente
1. gobernador - candidato - ideas - elección
1. salud - sistema - plan
1. vehículo - delito - instancias - robo
1. dosis - aire - clubes - recintos deportivos
1. tranquilidad - recuperación - residuos
1. aforo - protocolos

> El tema 4 parece ser un conjunto de conceptos (como algo más abstracto) más que un tópico.
> Por otro lado, los temas COVID parecen ser bastante heterogéneos entre sí, representando temas bastante específicos y dividiendo de manera bastante clara el set de noticias. Esto también podría motivar a reducir un poco la cantidad de tópicos, teniendo en cuenta que las problemáticas COVID no son tan necesarias de identificar asumiendo que existe un plan activo en paralelo que tiene esa responsabilidad.

"puerto varas" (107):
1. comunidad - colegio - alcalde - clases
1. casos - personas - ventiladores - dosis - vacunación
1. imputado - abuso - audiencia - abuso sexual
1. camas - personas - respiradores
1. guías - turismo - plan - programa - formalización
1. arma - arma de servicio - carabinero - control - funcionario - defensa - crimen - detención

> Aquí llama bastante la atención que a turismo se le relacione una formalización, lo que motiva a que se analice el dataset en busca de esta noticia y su verdadera relación.
> Curiosamente, es una de las comunas donde existe una mayor cantidad de tópicos sobre delitos y/o seguridad.

"osorno" (260):
1. personas - casos - medidas - pandemia
1. trabajo - mujeres - adultos mayores
1. mesas - obras - seguridad - protocolos 
1. horas - accidente - clases - conductor - vehículo
1. provincia - camas
1. demanda - productores - negocio
1. camapaña - vacunación - kilómetros
1. variante - pase de movilidad
1. mar - playa - acceso - predio

> En Osorno es donde se identificaron la mayor cantidad de tópicos diferentes sobre COVID, lo que también podría relacionarse con la cantidad de contagios de la comuna en ese periodo de tiempo.
> También, el último tópico sobre el acceso privado a playas, a pesar de representar a pocas noticias, parece un problema bastante relevante y que puede ser solucionado estatalmente.

"puerto octay" (18):
1. cargos - agua - empresa - río - comunidad - daño ambiental
1. libros - vacunación - donación - trabajadores agrícolas 
1. comuna - turismo - costero
1. proyecto - lago - infraestructura
1. accidente - emergencia - lesiones - camioneta
1. camioneta - dueño
1. imputado

> Aquí hay 3 tópicos redundantes sobre accidentes en vehículo (que además están bastante sobrepuestos en su visualización), por lo que se podría reducir la cantidad de tópicos.

"purranque" (9):
1. usuarios - salud - lactancia - incendio
2. pacientes - patologías - estrategia - hospitales
3. vacunación - personas hospitalizadas
4. accidente - vehículo

> Aquí existen muchos tópicos de salud, por lo que evidentemente es algo relevante. Además, la cantidad de tópicos podría reducirse.

"puyehue" (27):
1. alcaldesa - consejales - millones
1. luz - corte
1. narcisos - bulbos - exportación - cultivo
1. violencia - mujeres - dolor - programa
1. río - aceite - crecida - aceite quemado - agua
1. pesca artesanal
1. parque - pandemia - acuario
1. fondos concursables

> Se identifica que el concepto "aceite quemado"-"agua" es bastante importante de analizar. También parecen redundar unos 2-3 tópicos.

"río negro" (11):
1. años - dosis - gestión - temas - virus
1. clases - educación - alumnos
1. faenas - suministro - calidad
1. incidencia - tasa - contagios
1. caso - accidente de tránsito

> Aquí parecen sobrar 1-2 tópicos, se podrían reducir.

"san juan de la costa" (10):
1. cuarentena - pescadores - medida - aforo - celebración
1. productos - programa - mar - resolución
1. hidatidosis - estudio - riesgo - perros
1. salud - país - casos - confinamiento
1. prueblo originario - incendio

> Aquí la pescas y producción agrícola parecen ser temas bastante relevantes.

"san pablo" (11):
1. día - feriado - descanso
1. proyecto - energía - aerogeneradores (bastante abajo)
1. familias - riesgo - derrumbe
1. camas - casos - vacuna
1. fiscalizaciones - movilidad

"chaitén" (15):
1. mejoramiento - proyecto - educación pública
1. gobernador - cargo - gestión
1. noche - árboles - temporal
1. operativo médico - examen - salud

> Si bien existen unos 2-3 tópicos redundantes, algunos de los identificados son problemáticas bastante claras.

"futaleufú":
> No hay noticias de esta comuna.

"hualaihué" (12):
1. medio - medidas - disminución - residuos
1. imputado - recurso - víctimas - prisión preventiva
1. niños - educación - programa
1. dosis - vacunación

"palena" (21):
1. brigada - sistema - emergencias - sistema frontal - presipitaciones
1. mujeres - niñas - género - igualdad
1. terreno - obra - vecinos - talleres
1. kayak - aguas - turismo
1. terreno - licitación

> Parecen sobrar al menos 2-3 tópicos que no parecen tener un significado en conjunto (no interpretable.)

Sebastián Pacheco Cáceres - 2022
