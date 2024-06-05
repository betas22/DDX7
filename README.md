# Trabajo práctico - Procesamiento Digital de Señales (UNTREF)

La idea del trabajo es que completen los distintos scripts siguiendo las ideas del trabajo de Caspe, variaciones de ellas o ideas propias. Es muy importante que respeten los tipos de dato y las cantidades de variables de entrada y salida que se especifican en cada parte del esqueleto; todo está documentado, pero ante la duda consulten antes de dar cosas por sentado.

El orden de las tareas que deberían llevar a cabo es:

- A partir del archivo `requirements.txt` incluido en el esqueleto, generar un entorno de [conda](https://docs.conda.io/en/latest/) para poder tener instaladas las librerías necesarias para el trabajo. Si llegan a necesitar otras librerías, avisen. Esto lo pueden hacer con el comando 

    ```bash
    conda install --file requirements.txt
    ```

- Dentro del repositorio que les pasamos, copien la carpeta `Dataset_URMP`.

- Completar las funciones en `spectral_ops.py` dentro de la carpeta `ddx7`. Comprobar su correcto funcionamiento (ver archivos en la carpeta `tests_spectral_ops`, dentro de la carpeta `ddx7`) y luego generar los datos corriendo el archivo `create_data.py` en la carpeta dataset.

- Completar las STFT multiresolución en `ddx7/core.py`

- Completar la función de síntesis FM en `ddx7/core.py`

- Entrenar el modelo ejecutando `train.py`.

- Si todo corrió bien, borren las carpetas que se generaron en la carpeta dataset cuando corrieron `create_data.py`, muevan las carpetas que están en la carpeta `dataset_full` a la carpeta `Dataset_URMP` y repitan todo el proceso (corran `create_data.py`, entrenen el modelo con `train.py`). Atención: esto puede tardar mucho, en el orden de días, no teman y tengan paciencia.

- Empezar a proponer pruebas, ¿qué pasa si cambio la función de costo? ¿y si modifico el algoritmo para encontrar la frecuencia fundamental del audio? ¿la ponderación A propuesta en el cálculo de loudness aporta algo útil? Vayan cambiando bloques del modelo y entrenando distintas versiones, estudiando cómo varían los resultados en cada una de ellas. Propongan alguna métrica que permita analizar qué tan parecida es la señal estimada por el sistema a la señal de referencia.

- Escriban el informe, dándole especial atención al análisis de los resultados obtenidos en las distintas pruebas que realicen.

## Recomendaciones
- Si trabajan con Git y GitHub, tengan cuidado con las cosas que trackean. Por ejemplo con los datasets. Para evitar que Git "vea" a los datasets, deben agregar esas carpetas al archivo `.gitignore`. Git y GitHub son para tracker cambios en el código, no en los datos. GitHub no está pensado para ser un servicio de almacenamiento de datos en la nube, está pensado para almacenar repositorios de Git.

## Datasets
- [Dataset_URMP](https://drive.google.com/drive/folders/1tu5-rpUMGE9BfsPXGD80qV_xPPueaxy1) (para probar que las funciones que implementaron se ejecutan correctamente)
- [dataset_full](https://drive.google.com/drive/folders/1NSMF7oC5T0zei1AnticsQKJR1LXO5ApS) (para entrenar el modelo final)
