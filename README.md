# ExtrAI - EXTRacción Automática de Información por LLM

Proyecto desarrollado para la extracción automatica de informaciones al respecto de los siniestros viales ocurridos en Misiones, raspados de la la página del diário Primera Edición, usando framework [`ollama`](https://ollama.com/) de Inteligencia Artifical (LLM).

# Atención

Es importante tener el [ollama instalado](https://ollama.com/download) con los [modelos LLM](https://ollama.com/search) descargados y configurados.

# Organziando ambiente de trabajo:

Haciendo el clone del proyecto:
`git clone git@github.com:TUSIGyT/ExtrAI.git`

Accediendo a la carpeta:
`cd ExtrAI`

## Con [`venv`](https://docs.python.org/3/library/venv.html)
Creando ambiente virtual

`python -m venv .venv`

Activando el ambiente virtual creado

`source .venv/bin/activate`

En su primer uso, conviene actualizar el `pip`:
`pip install --upgrade pip`

Instalando dependencias:
`pip install -r requirements.txt`

## Con [`poetry`](https://python-poetry.org/)

`poetry install`
Despues de activar el ambiente virtual, basta correr el modelo.

# Entendiendo el proyecto

El ExtrAI está basado en [ollama-batch](https://github.com/emi420/ollama-batch) para correr modelos de LLM con el mismo prompt para distintas notícias almacenadas en JSON.
Para eso, es importante disponer de los siguientes elementos:
- [`Noticias`](./src/extrai/news/sample_primera_edicion_siniestros_viales_2024.json) - Conjunto de noticias organizadas en una lista de json;
- [`Prompt`](./src/extrai/prompts/prompt_v3.txt) - Archivo .txt con la consigna al modelo LLM;

Resultado
- [`Results`](./src/extrai/results/deepseek-r1:8b_result.json) - Resultado de la extracción de información por LLM;

Es probable que haya que desarrollar un paso posterior para limpieza del resultado, como suele pasar con `deepseek`.
Por eso se ha creado el [`data-cleaning`](./src/extrai/post-processing/data_cleaning.py).

# Corriendo el modelo

`poetry run ollama-batch -f /news/sample_primera_edicion_siniestros_viales_2024.json --json-append id --prompt-file src/extrai/prompts/prompt_v3.txt --json-property=cuerpo -m deepseek-r1:8b > /results/deepseek-r1:8b_result.json`

```
for model in deepseek-r1:8b gemma3:4b llama3.2 test_wqp_deepseek:latest; do
    poetry run ollama-batch -f /news/sample_primera_edicion_siniestros_viales_2024.json --prompt-file src/extrai/prompts/prompt_v3.txt --json-property=cuerpo -m $model > /results/"$model"_result.json;
    done
```
