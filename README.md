# Siniestros Viales Misiones

Proyecto desarrollado para la extracción de informaciones al respecto de los siniestros viales ocurridos en Misiones, raspados de la la página del diário Primera Edición, usando framework ollama de Inteligencia Artifical (LLM).

# Corriendo:

`source .venv/bin/activate`

`ollama-batch -f primera_edicion_siniestros_viales_2024.json --prompt-file prompt_v3.txt --json-property=cuerpo -m deepseek-r1:8b > result.json`

```
for model in deepseek-r1:8b gemma3:4b; do
    ollama-batch -f primera_edicion_siniestros_viales_2024.json --prompt-file prompt_v3.txt --json-property=cuerpo -m $model > result_"$model".json;
    done
```