# Siniestros Viales Misiones

Proyecto desarrollado para la extracción de informaciones al respecto de los siniestros viales ocurridos en Misiones, raspados de la la página del diário Primera Edición, usando framework ollama de Inteligencia Artifical (LLM).

# Atención

Es importante tener el ollama instalados con los modelos LLM descargados y configurados.

# Organziando ambiente de trabajo:

Creando ambiente virtual

`python -m venv .venv`

Activando el ambiente virtual creado

`source .venv/bin/activate`

En su primer uso, conviene actualizar el `pip`:
`pip install --upgrade pip`

# Corriendo el script

`ollama-batch -f primera_edicion_siniestros_viales_2024.json --json-append id --prompt-file prompt_v3.txt --json-property=cuerpo -m deepseek-r1:8b > result.json`

```
for model in deepseek-r1:8b gemma3:4b llama3.2 test_wqp_deepseek:latest; do
    ollama-batch -f primera_edicion_siniestros_viales_2024.json --prompt-file prompt_v3.txt --json-property=cuerpo -m $model > result_"$model".json;
    done
```
